# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/master/containers/java/.devcontainer/base.Dockerfile
ARG JAVA_VERSION=8
FROM mcr.microsoft.com/vscode/devcontainers/java:0-${JAVA_VERSION}

ENV LANG C.UTF-8
# Install Maven
ARG MAVEN_VERSION=3.8.1
RUN su vscode -c "source /usr/local/sdkman/bin/sdkman-init.sh && sdk install maven \"${MAVEN_VERSION}\""

ARG NODE_VERSION=16
ENV NODE_VERSION=$NODE_VERSION
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash \
    && apt-get -y install --no-install-recommends\
    make \
    ca-certificates \
    software-properties-common \
    netbase \
    netcat \
    liblzma-dev \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev \
    default-mysql-client \
    default-libmysqlclient-dev \
    sqlite3=3.* \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

ARG PYTHON_VERSION=3.8.10
RUN set -ex \ 
    && curl -fSL "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
    && mkdir -p /usr/src/python \ && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \ 
    && rm python.tar.xz \
    && cd /usr/src/python \ 
    && ./configure --enable-shared --enable-unicode=ucs4 \ 
    && make -j$(nproc) \ 
    && make install \ 
    && ldconfig \ 
    && pip3 install --no-cache-dir --upgrade --ignore-installed pip \ 
    && rm -rf /usr/src/python ~/.cache

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \ 
    && ln -s idle3 idle \ 
    && ln -s pydoc3 pydoc \ 
    && ln -s python3 python \ 
    && ln -s python3-config python-config

# install python tools
ARG USERNAME=vscode
ENV PIPX_HOME=/usr/local/py-utils \
    PIPX_BIN_DIR=/usr/local/py-utils/bin
ENV PATH=${PATH}:${PIPX_BIN_DIR}
COPY docker/python-debian.sh /tmp/library-scripts/python-debian.sh
RUN bash /tmp/library-scripts/python-debian.sh "${PIPX_HOME}" "${USERNAME}"

# install golang tools
COPY docker/go-debian.sh /tmp/library-scripts/go-debian.sh
ENV GO111MODULE=auto
ARG GO_VERSION=1.15
ENV GO_VERSION=${GO_VERSION}
RUN bash /tmp/library-scripts/go-debian.sh "${GO_VERSION}" "/usr/local/go" "${GOPATH}" "${USERNAME}" "true" \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*
COPY docker/install-go-deps.sh /tmp/library-scripts/install-go-deps.sh
RUN PATH=$PATH:/usr/local/go/bin bash /tmp/library-scripts/install-go-deps.sh

WORKDIR /workspace
USER vscode

# install nodejs tools
RUN echo 'export PATH=`yarnpkg global bin`:$PATH' >> ~/.bashrc
RUN sudo npm install -g @vue/cli
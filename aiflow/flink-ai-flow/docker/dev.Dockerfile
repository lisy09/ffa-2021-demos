ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# install python dependencies for flink-ai-flow
WORKDIR /workspace
COPY requirements-dev.txt requirements-dev.txt
RUN pip3 install -r requirements-dev.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install flink-ai-flow
COPY . /tmp/aiflow-source
WORKDIR /tmp/aiflow-source
RUN sudo chown -R vscode:vscode /tmp/aiflow-source \
    && make install-local && rm -rf /tmp/aiflow-source

WORKDIR /workspace
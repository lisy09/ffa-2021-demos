ARG PYTHON_VERSION=3.8.10
FROM python:${PYTHON_VERSION}-slim-buster AS builder

RUN python3 -m pip install wheel \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends npm \
    && npm install --global yarn \
    && mkdir /tmp/dist

WORKDIR /flink-ai-flow

COPY . /flink-ai-flow
RUN bash build_ai_flow_package.sh wheel && cp dist/* /tmp/dist
RUN cd lib/notification_service && python3 setup.py bdist_wheel && cp dist/* /tmp/dist
RUN cd lib/airflow && python3 setup.py bdist_wheel && cp dist/* /tmp/dist

FROM python:${PYTHON_VERSION}-slim-buster

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

# AIFlow
ARG AIRFLOW_HOME=/usr/local/airflow
ENV AIRFLOW_HOME=${AIRFLOW_HOME}
ARG AIFLOW_HOME=/usr/local/aiflow
ENV AIFLOW_HOME=${AIFLOW_HOME}
COPY ./examples ${AIFLOW_HOME}/examples

COPY --from=builder /tmp/dist /tmp/dist
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends default-libmysqlclient-dev curl ssh vim unzip gcc \
    && pip install --no-cache-dir /tmp/dist/* \
    && apt-get purge --auto-remove -yqq gcc \
    && apt-get autoremove -yqq --purge \
    && apt-get clean

RUN groupadd -r aiflow && useradd -r -g aiflow aiflow
RUN chown -R aiflow:aiflow ${AIFLOW_HOME} \
    && mkdir -p ${AIRFLOW_HOME} && chown -R aiflow:aiflow ${AIRFLOW_HOME}
USER aiflow
WORKDIR ${AIFLOW_HOME}

EXPOSE 8000 8080 50051
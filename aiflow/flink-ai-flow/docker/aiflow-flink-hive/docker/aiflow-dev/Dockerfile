ARG FLINK_IMAGE_BASE
ARG DEV_IMAGE_BASE
FROM ${FLINK_IMAGE_BASE} as flink-base
FROM ${DEV_IMAGE_BASE}

USER root

ARG DEFAULT_USER=vscode
ENV DEFAULT_USER=${DEFAULT_USER}

# install flink binary
COPY --from=flink-base /opt/flink /opt/flink
ENV FLINK_HOME=/opt/flink
ENV PATH=${PATH}:${FLINK_HOME}/bin

# install hadoop & hive
ARG HADOOP_VERSION
COPY --from=flink-base /opt/hadoop-${HADOOP_VERSION} /opt/hadoop-${HADOOP_VERSION}
COPY --from=flink-base /opt/hive /opt/hive
ENV HADOOP_HOME /opt/hadoop-${HADOOP_VERSION}
ENV HIVE_HOME /opt/hive
ENV PATH ${HADOOP_HOME}/bin:$HIVE_HOME/bin:$PATH
RUN ln -s ${HADOOP_HOME}/etc/hadoop /etc/hadoop

ENV HADOOP_CLASSPATH ${HADOOP_HOME}/etc/hadoop:${HADOOP_HOME}/share/hadoop/common/lib/*:${HADOOP_HOME}/share/hadoop/common/*:${HADOOP_HOME}/share/hadoop/hdfs:${HADOOP_HOME}/share/hadoop/hdfs/lib/*:${HADOOP_HOME}/share/hadoop/hdfs/*:${HADOOP_HOME}/share/hadoop/mapreduce/*:${HADOOP_HOME}/share/hadoop/yarn:${HADOOP_HOME}/share/hadoop/yarn/lib/*:${HADOOP_HOME}/share/hadoop/yarn/*

RUN chown -R ${DEFAULT_USER}:${DEFAULT_USER} ${FLINK_HOME} ${HADOOP_HOME} ${HIVE_HOME}

COPY config-hive.sh /config-hive.sh
RUN chmod a+x /config-hive.sh

USER ${DEFAULT_USER}
ENTRYPOINT ["/config-hive.sh"]
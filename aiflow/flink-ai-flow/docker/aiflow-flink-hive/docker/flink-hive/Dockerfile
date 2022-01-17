ARG HIVE_IMAGE_BASE
ARG FLINK_IMAGE_BASE=flink:1.13.2
FROM ${HIVE_IMAGE_BASE} as hive-base

FROM $FLINK_IMAGE_BASE

ARG HADOOP_VERSION
COPY --from=hive-base /opt/hadoop-${HADOOP_VERSION} /opt/hadoop-${HADOOP_VERSION}
COPY --from=hive-base /opt/hive /opt/hive
ENV HADOOP_HOME /opt/hadoop-${HADOOP_VERSION}
ENV HIVE_HOME /opt/hive
ENV PATH ${HADOOP_HOME}/bin:$HIVE_HOME/bin:$PATH
RUN ln -s ${HADOOP_HOME}/etc/hadoop /etc/hadoop

ARG FLINK_HIVE_CONNECTOR_URL=https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-hive-2.3.6_2.11/1.13.0/flink-sql-connector-hive-2.3.6_2.11-1.13.0.jar
ENV FLINK_HIVE_CONNECTOR_URL=${FLINK_HIVE_CONNECTOR_URL}
RUN wget ${FLINK_HIVE_CONNECTOR_URL} -P ${FLINK_HOME}/lib/
COPY lib/* ${FLINK_HOME}/lib/

COPY config-hive.sh /config-hive.sh
RUN chmod +x /config-hive.sh

ENV HADOOP_CLASSPATH ${HADOOP_HOME}/etc/hadoop:${HADOOP_HOME}/share/hadoop/common/lib/*:${HADOOP_HOME}/share/hadoop/common/*:${HADOOP_HOME}/share/hadoop/hdfs:${HADOOP_HOME}/share/hadoop/hdfs/lib/*:${HADOOP_HOME}/share/hadoop/hdfs/*:${HADOOP_HOME}/share/hadoop/mapreduce/*:${HADOOP_HOME}/share/hadoop/yarn:${HADOOP_HOME}/share/hadoop/yarn/lib/*:${HADOOP_HOME}/share/hadoop/yarn/*

ENTRYPOINT ["/config-hive.sh"]
CMD ["help"]
ARG HADOOP_BASE_IMAGE_FULL
FROM ${HADOOP_BASE_IMAGE_FULL}

ARG HIVE_VERSION=2.3.9
ENV HIVE_VERSION ${HIVE_VERSION}
ENV HIVE_HOME /opt/hive
ENV PATH $HIVE_HOME/bin:$PATH
ENV HIVE_URL https://downloads.apache.org/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz

ARG POSTGRESQL_JDBC_URL=https://jdbc.postgresql.org/download/postgresql-42.2.23.jar
ENV POSTGRESQL_JDBC_URL ${POSTGRESQL_JDBC_URL}

WORKDIR /opt

#Install Hive and PostgreSQL JDBC
RUN apt-get update && apt-get install -y wget procps && \
    wget ${HIVE_URL} && \
    tar -xzvf apache-hive-$HIVE_VERSION-bin.tar.gz && \
    mv apache-hive-$HIVE_VERSION-bin hive && \
    wget ${POSTGRESQL_JDBC_URL} -O $HIVE_HOME/lib/postgresql-jdbc.jar && \
    rm apache-hive-$HIVE_VERSION-bin.tar.gz && \
    apt-get --purge remove -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD hive-conf/hive-site.xml $HIVE_HOME/conf

COPY startup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/startup.sh

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
CMD startup.sh
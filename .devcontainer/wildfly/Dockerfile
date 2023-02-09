FROM quay.io/wildfly/wildfly:27.0.0.Final-jdk11

ARG MAVEN_VERSION="3.9.0"
ARG WILDFLY_USER="admin"
ARG WILDFLY_PASSEORD="admin"

USER jboss
RUN $JBOSS_HOME/bin/add-user.sh -u $WILDFLY_USER -p $WILDFLY_PASSEORD --silent

USER root
RUN yum install -y curl git wget jq openssh net-tools \
  && curl -sSL -o /opt/maven.tar.gz https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
  && tar -xzf /opt/maven.tar.gz -C /opt/ \
  && cp -s /opt/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/
ENTRYPOINT [ "bash" ]
FROM maven:3.8.6-openjdk-11 AS builder

WORKDIR /workspace
COPY src/ /workspace/src/
COPY pom.xml /workspace/
RUN mvn package

FROM quay.io/wildfly/wildfly:27.0.0.Final-jdk11

USER jboss
COPY --from=builder --chown=jboss:jboss /workspace/target/*.war $JBOSS_HOME/standalone/deployments/
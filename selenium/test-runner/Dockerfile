FROM python:3.9-alpine

WORKDIR /workspace
COPY ./*.py /workspace/
RUN apk add jq \
  && pip install selenium pytest
ENTRYPOINT [ "pytest" ]
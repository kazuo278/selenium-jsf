FROM python:3.9-alpine

WORKDIR /workspace
COPY ./*.py /workspace/
COPY ./entrypoint.sh /entrypoint.sh
RUN apk add jq \
  && pip install selenium pytest \
  && chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
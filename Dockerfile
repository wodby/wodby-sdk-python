FROM python:3.5-alpine

ENV PATH="/root/.local/bin:${PATH}"

RUN set -e; \
    apk add --no-cache --update bash make jq; \
    mkdir -p /opt/sdk /opt/sdk-req; \
    pip install --user --no-warn-script-location yq twine

WORKDIR /opt/sdk

COPY ./src/requirements.txt /opt/sdk-req/
RUN pip install -r /opt/sdk-req/requirements.txt
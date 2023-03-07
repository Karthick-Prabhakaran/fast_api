# syntax = docker/dockerfile:1.4

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app
ENV PYTHONPATH=/usr/lib/python3/dist-packages
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app ./app

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
apt-get install -y google-chrome-stable
EOF

RUN apt-get install xvfb


RUN <<EOF
apt-get install -y chromium-browser
apt-get install -y libglib2.0-0
apt-get install -y libnss3
apt-get install -y libgconf-2-4
apt-get install -y libfontconfig1
EOF


RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /



FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install dependencies
RUN apt-get update && apt-get install -y curl apt-transport-https ca-certificates gnupg

# Install Microsoft package repository GPG key and feed
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
    && echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" > /etc/apt/sources.list.d/azure-functions.list

# Install Azure Functions Core Tools v4
RUN apt-get update && apt-get install -y azure-functions-core-tools-4

WORKDIR /workspace

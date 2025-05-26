FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install Azure Functions Core Tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg         && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg         && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list         && apt-get update && apt-get install -y azure-functions-core-tools-4

WORKDIR /workspace

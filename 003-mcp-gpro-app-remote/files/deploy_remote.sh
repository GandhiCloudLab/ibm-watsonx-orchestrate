#!/usr/bin/env bash

MCP_NAME="mcp_gpro_remote"
MCP_DESC="MCP Gpro from Remote Server (code engine)"
PROXY_SRC="./mcp-proxy/src"
APP_URL="https://mcp-gpro-app.xxxxxxxx.us-east.codeengine.appdomain.cloud/mcp"

orchestrate toolkits remove -n "${MCP_NAME}"
orchestrate toolkits import \
  --kind mcp \
  --name "${MCP_NAME}" \
  --description "${MCP_DESC}" \
  --package-root "${PROXY_SRC}" \
  --command "[\"python\", \"-m\", \"mcp_proxy\", \"--transport\", \"streamablehttp\", \"${APP_URL}\"]" \
  --tools "*"
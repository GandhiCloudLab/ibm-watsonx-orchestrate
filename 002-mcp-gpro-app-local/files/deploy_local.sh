
### Importing local MCP toolkits
### https://developer.watson-orchestrate.ibm.com/tools/toolkits/local_mcp_toolkits

orchestrate toolkits remove -n mcp_gpro_local

orchestrate toolkits import \
    --kind mcp \
    --name mcp_gpro_local \
    --description "MCP Gpro in local at WxO Instance" \
    --package-root ./mcp_gpro_local \
    --command '["python", "app.py"]' \
    --tools "*" 
# Deploying and Accessing Local MCP Server toolkit - GPro app

## 1. Set up ADK

The detailed info is available [here](../001-setting-up-adk) 

## 2. Importing local MCP toolkits

1. Goto the [files](./files) folder of this repo 

2. Run the below command.

  ```
  ./deploy_local.sh
  ```

  You might have got the output like this.

  ```
  [ERROR] - This functionality is only available for Local Environments
  [INFO] - Successfully imported tool kit mcp_gpro_local
  ```

## 3. Create Agent and import tool from MCP

1. Click on **Build** >  **Agent Builder**
  <img src="images/img21.png">

2. Click on **Create Agent**
  <img src="images/img22.png">

3. Enter the **Name :** 

4. Enter the **Description :** `The MCP Gpro Agent assists with finding weather for the given city using the tool available.`

5. Click on **Create→** button
  <img src="images/img23.png">

6. Click on **Toolset** menu
  <img src="images/img24.png">
  You can see the tools section is empty.

7. Click on **Add tool** button
  <img src="images/img25.png">

8. Choose **Add from file or MCP server**
  <img src="images/img26.png">

9. Choose **Import from MCP server**
  <img src="images/img27.png">

10. Choose **mcp_gpro_local** and click on **Close** icon on the top
  <img src="images/img28.png">

11. Switch on **Activation toggle** for the selected tool **mcp_gpro_local** and click on **Close** icon on the top
  <img src="images/img29.png"
  You can see the tool  **mcp_gpro_local: weather** got added to the agent.
  <img src="images/img30.png">

12. In the preview chat window, you can type your question related to weather of a city and get the answers. (Mock weather data only)
  <img src="images/img31.png">

13. Click on **Deploy** button
  <img src="images/img32.png">

14. Choose the **mcp_gpro_local** agent
  <img src="images/img33.png">

15. In the chat window, you can type your question related to weather of a city and get the answers. (Mock weather data only)
  <img src="images/img34.png">

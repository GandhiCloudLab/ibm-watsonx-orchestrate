# Deploying and Accessing Remote MCP Server toolkit - Gpro app

## 1. Set up ADK

The detailed info is available [here](../001-setting-up-adk)

## 2. Importing remote MCP toolkits using ADK CLI

1. Download all files and subfolders from [here](./files)

2. A simple app is available at the folder **./mcp_gpro_remote**. Deploy this app in IBM Code Engine or in some remote system.

3. Update the APP_URL property of the **./deploy_remote.sh** file with the above url. Don't forget to end the url with **mcp**.
  ```
  APP_URL="https://mcp-gpro-app.xxxxxxxx.us-east.codeengine.appdomain.cloud/mcp"
  ```

3. Run the below command.
  ```
  ./deploy_remote.sh
  ```

  You might have got the output like this.
  ```
  [ERROR] - This functionality is only available for Local Environments
  [INFO] - Successfully imported tool kit mcp_gpro_remote
  ```

## 3. Importing remote MCP toolkits using ADK CLI

1. Goto the [files](./files) folder of this repo 

2. Run the below command.

  ```
  ./deploy_remote.sh
  ```

  You might have got the output like this.

  ```
  [ERROR] - This functionality is only available for Local Environments
  [INFO] - Successfully imported tool kit mcp_gpro_remote
  ```

## 4. Create Agent and import tool from MCP

1. Click on **Create Agent**
  <img src="images/img11.png">

2. Enter the **Name :**

3. Enter the **Description :** `The MCP Gpro Remote Agent assists with finding price for the given product using the tool available.`

4. Click on **Create→** button
  <img src="images/img12.png">

5. Click on **Toolset** menu

6. Click on **Add tool** button

  <img src="images/img13.png">

7. Choose **Add from file or MCP server**
  <img src="images/img14.png">

8. Choose **Import from MCP server**
  <img src="images/img15.png">

10. Choose **mcp_gpro_remote** and click on **Close** icon on the top
  <img src="images/img16.png">

11. Switch on **Activation toggle** for the selected tool **mcp_gpro_remote:price** and click on **Close** icon on the top
  <img src="images/img17.png"

  You can see the tool  **mcp_gpro_remote: price** got added to the agent.

12. In the preview chat window, you can type your question related to price of a product and get the answers. (Mock price data only)

13. Click on **Deploy** button

  <img src="images/img18.png">

14. Click on **Deploy** button

  <img src="images/img19.png">

15. The Agent builder screen show the **mcp_gpro_remote** agent.
  <img src="images/img20.png">

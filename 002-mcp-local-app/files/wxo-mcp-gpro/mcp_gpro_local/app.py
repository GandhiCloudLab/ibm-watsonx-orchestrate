from fastmcp import FastMCP
import random

# Initialize FastMCP server
mcp = FastMCP("MCP Gpro Server")

@mcp.tool()
def weather(city = "Paris") -> dict:
    """
    Return the weather of the given city.
    
    Args:
        city: The city to find the weather (default: Paris)
    
    Returns:
        Current weather value
    """
    
    result = random.uniform(1, 30)

    resp = {"weather" : result, "city" : city}

    return resp

if __name__ == "__main__":

    mcp.run()
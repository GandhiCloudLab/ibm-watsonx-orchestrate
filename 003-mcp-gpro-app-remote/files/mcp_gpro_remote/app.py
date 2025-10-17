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

@mcp.tool()
def price(product = "Laptop") -> dict:
    """
    Return the price of the given product.
    
    Args:
        product: The product to find the price (default: Laptop)
    
    Returns:
        Current price value
    """
    
    result = random.uniform(1, 30)

    resp = {"price" : result, "product" : product}

    return resp

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

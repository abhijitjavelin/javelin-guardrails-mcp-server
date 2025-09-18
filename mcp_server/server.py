# javelin_server.py
import httpx
import os
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

try:
    # Load OpenAPI spec
    print("Loading OpenAPI spec...")
    openapi_url = "https://raw.githubusercontent.com/getjavelin/javelin-openapi/refs/heads/main/standalone-guardrails-openapi.json"
    response = httpx.get(openapi_url)
    response.raise_for_status()
    openapi_spec = response.json()
    print("✅ OpenAPI spec loaded")

    # Create HTTP client
    client = httpx.AsyncClient(
        base_url="https://api-dev.javelin.live",
        headers={"x-javelin-apikey": os.getenv("JAVELIN_API_KEY")}
    )
    print("✅ HTTP client created")

    # Create MCP server
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="Javelin Guardrails Server"
    )
    print("✅ MCP server created")

    if __name__ == "__main__":
        print("Starting server on http://localhost:8000...")
        mcp.run()

except Exception as e:
    print(f"❌ Error setting up server: {e}")
    import traceback
    traceback.print_exc()
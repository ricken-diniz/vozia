import json
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def airbnb_search(search_query, max: int = 3) -> None:
    
    async with AsyncExitStack() as stack:
        server_params = StdioServerParameters(
            command="npx",
            args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
        )

        stdio_transport = await stack.enter_async_context(stdio_client(server_params))
        stdio, write = stdio_transport

        client = await stack.enter_async_context(ClientSession(stdio, write))
        await client.initialize()
        
        response = await client.call_tool("airbnb_search", search_query)
        messages = []
        
        count = 0
        for item in json.loads(response.content[0].text)['searchResults']:
        
            messages.append(item)
            
            count += 1
            if count >= max:
                break

        return messages

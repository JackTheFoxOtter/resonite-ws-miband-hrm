from websockets.server import WebSocketServerProtocol
from websockets.typing import Data
from websockets import serve
import asyncio

server_port = 3228
client_port = 3229

async def main():
    async def client_handler(websocket : WebSocketServerProtocol):
        print("Client established connection!")

        async for message in websocket:
            print(f"Received message from client: '{message}'")

        print("Client connection ended!") 

    print(f"Serving client endpoint (Port: {client_port})...")
    client_endpoint = await serve(client_handler, 'localhost', client_port)

    async def server_handler(websocket : WebSocketServerProtocol):
        print("Server established connection!")
        
        async for message in websocket:
            print(f"Received message from server: '{message}'")

            for client in client_endpoint.websockets:
                await client.send(message)
            
        print("Server connection ended!") 

    print(f"Serving server endpoint (Port: {server_port})...")
    server_handler = await serve(server_handler, 'localhost', server_port)

    await asyncio.Future() # Run forever
    
if __name__ == '__main__':
    # Start
    asyncio.run(main())
from a2a.types import AgentCapabilities, AgentCard, AgentSkill, AgentInterface
from agent import AliceAgent
# import httpx
from a2a.server.request_handlers import DefaultRequestHandler
from agent_executor import AliceAgentExecutor
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.routes import create_agent_card_routes, create_jsonrpc_routes
from starlette.applications import Starlette
import uvicorn

# Step 3: Agent Card -> Just like visiting card of a person. It includes the description, capabilities, host_url.
def main(host="localhost", port= 10004):

    skills = AgentSkill(
        id = "schedule time for a trip plan",
        name = "Trip Palnning Tool",
        description = "Helps with finding Alice's availability for a trip",
        input_modes=['text', 'text/plain'],
        output_modes=['text','text/plain'],
        tags = ["scheduling","trip planner"],
        examples = ["Are you free on 2026-08-19"]
    )

    agent_card = AgentCard(
        name = "Alice Agent",
        description = "Helps in scheduling trip planning",
        version = "1.0.0",
        # which language does agent speaks: text, images, voice, etc
        default_input_modes= AliceAgent.SUPPORTED_CONTENT_TYPES, 
        default_output_modes= AliceAgent.SUPPORTED_CONTENT_TYPES,
        capabilities= AgentCapabilities(streaming=False, extended_agent_card=False),
        skills= skills,
        supported_interfaces=[
            AgentInterface(
                protocol_binding='JSONRPC',
                url=f"http://{host}:{port}",
                protocol_version=1.0
            )
        ]
    )

    # Step 4: Host the Agent
    # request handler -> entry point of another agent's request
    # create http client
    #httpx_client = httpx.AsyncClient()
    request_handler = DefaultRequestHandler(
        agent_executor = AliceAgentExecutor(),
        task_store = InMemoryTaskStore(),
        agent_card=agent_card,
        extended_agent_card=None
        # push_notifier = InMemoryPushNotifier(httpx_client)
    )

    # host the agent
    agent_card_route = create_agent_card_routes(agent_card)
    jsonrpc_routes = create_jsonrpc_routes(request_handler)
    # Recommendation: If you don't need a custom prefix, I'd omit it ->
    # create_jsonrpc_routes(request_handler, '/')

    app = Starlette(routes=agent_card_route + jsonrpc_routes)

    uvicorn.run(app.build(), host=host, port=port)

if __name__ =="__main__":
    main()
from agent import AliceAgent
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue

# Step 2: Agent Executor -> to wrap this functions invoking

class AliceAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = AliceAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        user_query = context.get_user_input()
        context_id = context.context_id
        response = await self.agent.get_response(
            query=user_query, 
            context_id=context_id
        )
        return response

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise NotImplementedError('Cancel is not supported.') 
import os
from dotenv import load_dotenv

from vanna import Agent, AgentConfig
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.integrations.google import GeminiLlmService

load_dotenv()

class DefaultUserResolver(UserResolver):
    def resolve(self, request):
        return User(id="default_user")

def create_agent():
    llm = GeminiLlmService(api_key=os.getenv("GOOGLE_API_KEY"))

    runner = SqliteRunner(database="clinic.db")

    tools = ToolRegistry()
    tools.register(RunSqlTool(runner))
    tools.register(VisualizeDataTool())
    tools.register(SaveQuestionToolArgsTool())
    tools.register(SearchSavedCorrectToolUsesTool())

    memory = DemoAgentMemory()

    agent = Agent(
        config=AgentConfig(),
        llm=llm,
        tools=tools,
        memory=memory,
        user_resolver=DefaultUserResolver()
    )

    return agent, memory

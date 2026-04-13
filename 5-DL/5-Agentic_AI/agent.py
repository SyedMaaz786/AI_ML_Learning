from agno.agent import Agent

from agno.models.google import Gemini
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

# def build_agent1():
#     return Agent(
#         model=Gemini(
#             id="gemini-2.5-flash-lite",
#         )
#     )
# gemini_agent = build_agent1()
# gemini_agent.print_response("What is AI?")


def build_agent2():
    return Agent(
        model=Groq(
            id="qwen/qwen3-32b",
        ),
        tools=[DuckDuckGoTools()]
    )
groq_agent = build_agent2()
groq_agent.print_response("What is happening in Iran today?")




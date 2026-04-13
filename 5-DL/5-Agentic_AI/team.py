from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

Eng_agent = Agent(name="English Agent", role="You answer questions in English")
Arabic_agent = Agent(name="Arabic Agent", role="You answer questions in Arabic")
Hindi_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team_leader = Team(
    name="Translation and Query answering Team",
    members=[Eng_agent, Arabic_agent, Hindi_agent],
    model=Groq(
            id="llama-3.3-70b-versatile",
        ),
    show_members_responses=True,
    instructions="""All member agents must respond to answer the query in thier specific language.
                    Do not route to just one agent. Output the response of all agents."""

)

team_leader.print_response("What is RAG?")


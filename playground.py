from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app

# Load environment variables from .env file
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# Set GROQ API key
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

# Try using mixtral-8x7b-32768 which has better tool calling support
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),  # Mixtral model
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],  # Changed to list
    show_tool_calls=True,  # Fixed parameter name
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"), 
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        ),
    ],
    instructions=["Use tables to display the data"],  # Already a list, good
    show_tool_calls=True,
    markdown=True,
)

# Create Playground instance with agents
app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
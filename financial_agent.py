from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")


web_search_agent = Agent(
    name="web search agent",
    role="search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["keep the source at the end of output"],
    show_tool_calls=True,
    markdown=True,
)

### finance agent

finance_agent = Agent(
    name="finance agent",
    role="get stock data",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=["always keep sources","use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
    )

multi_agent.print_response("summarize analyst recommendations and share the latest news for Google",stream=True)
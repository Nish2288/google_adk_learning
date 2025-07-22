from google.adk.agents import Agent
from datetime import datetime


def get_time() -> dict:
    """Get the current time"""
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="You are the root agent.",
    instruction="""You are helpful assistance that can use following tools:
    -get_time""",
    tools=[get_time],
)

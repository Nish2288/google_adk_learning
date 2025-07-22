from google.adk.agents import Agent


root_agent = Agent(
    name="hello_agent",
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""You are helpful agent ask the name of the user and then greet the user by name 
    and tell them current time.
""",
)

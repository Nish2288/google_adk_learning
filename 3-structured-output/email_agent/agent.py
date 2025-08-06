from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email")
    body: str = Field(description="The body of the email")


root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Generate professional email with subject and body",
    instruction=""" You are helpful email generation assistant.
    Your task is to generate professional email based on user request.

    GUIDELINES:
    - Write appropriate Subject line.
    - Write a well structured email body with:
        * Professional Greeting
        * Clear and concise main content.
        * Appropriate Closing
        * Your name as signature

    IMPORTANT: Your response must be valid JSON matching following structure:
    {
        "subject": "Subject line of email.",
        "body": "Email body with main content"
    }
    """,
    output_schema=EmailContent,
    output_key="email",
)

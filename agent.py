from pydantic_ai import Agent
from dotenv import load_dotenv

from prompts.generate_frontend_code import generate_frontend_code
from prompts.generate_frontend_tests import generate_frontend_tests
load_dotenv()
frontend_agent = Agent('openai:gpt-3.5-turbo')
test_agent = Agent('openai:gpt-3.5-turbo')

frontend_prompt = generate_frontend_code(
    component="ChatUI",
    framework="React",
    styling="CSS",
    features=["Auto-scroll on new messages", "Typing indicator"]
)
frontend_code = frontend_agent.run_sync(frontend_prompt)

print('frontend code', frontend_code.data)
test_prompt = generate_frontend_tests(frontend_code, framework="React")
test_cases = test_agent.run_sync(test_prompt)

print('test cases', test_cases.data)

from pydantic_ai import Agent
from dotenv import load_dotenv
import os
from prompts.generate_frontend_code import generate_frontend_code
from prompts.generate_css import generate_css

load_dotenv()

react_agent = Agent('openai:gpt-3.5-turbo')
css_agent = Agent('openai:gpt-3.5-turbo')

component_name = 'ChatUI'

frontend_prompt = generate_frontend_code(
    component=component_name,
    framework="React",
    styling="CSS",
    features=["Auto-scroll on new messages", "Typing indicator"]
)
frontend_code = react_agent.run_sync(frontend_prompt)

print('frontend code', frontend_code.data)
css_prompt = generate_css(frontend_code.data)
css = css_agent.run_sync(css_prompt)
# test_prompt = generate_frontend_tests(frontend_code, framework="React")
# test_cases = test_agent.run_sync(test_prompt)
#
# print('test cases', test_cases.data)


target_dir = './dynamic-react-ai/components'
component_file_name = "Dynamic.tsx"
style_file_name = 'styles.css'

os.makedirs(target_dir, exist_ok=True)

component_file_path = os.path.join(target_dir, component_file_name)
style_file_path = os.path.join(target_dir, style_file_name)
with open(component_file_path, "w") as file:
    file.write(frontend_code.data)
with open(style_file_path, "w") as file:
    file.write(css.data)

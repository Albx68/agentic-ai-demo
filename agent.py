from pydantic_ai import Agent

agent = Agent('openai:gpt-4o')

result_sync = agent.run_sync('What is the capital of Italy')
print('result_sync', result_sync.data)


async def main():
    result = await agent.run('What is the capital of France')
    print(result.data)

    async with agent.run_stream('What is the capital of the UK?') as response:
        print(await response.get_data())

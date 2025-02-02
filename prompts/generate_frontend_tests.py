def generate_frontend_tests(frontend_code, framework="React"):
    prompt = f"""
    Based on the following frontend component code:
    {frontend_code}

    Write test cases for this component. Ensure that the tests:
    - Verify user input handling (e.g., submitting a message).
    - Verify that messages are correctly displayed.
    - Test the functionality of the send button.
    - Test edge cases (e.g., sending an empty message).
    """
    return prompt

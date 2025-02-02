

def generate_css(frontend_code):
    prompt = f"""
    I have the following React component code. Please generate the CSS styles for it based on the class names and structure in the component. Make sure to:
    - Follow best practices for styling.
    - Make the design responsive (mobile-first).
    - Ensure that the component's interactive elements (like buttons) have hover and focus states.
    - Use Flexbox or Grid where applicable.
    - Remove any triple quotes or CSS identification, the output should only be css and nothing else

    Here is the React component code:

    {frontend_code}

    Please generate the CSS styles for the classes used in this component.
    """

    return prompt

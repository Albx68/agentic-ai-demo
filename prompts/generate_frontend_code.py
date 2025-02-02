def generate_frontend_code(component="ChatUI", framework="React", styling="CSS", features=None):
    if features is None:
        features = []
    features_str = "\n".join([f"- {feature}" for feature in features])

    prompt = f"""
    Create a reusable {component} component. The component should:
    - Be compatible with {framework} and {styling}.
    - Include the following features:
    {features_str}

    The component should:
    - Have a text input for user messages.
    - Display a list of chat messages.
    - Include a send button for sending messages.
    """

    return prompt

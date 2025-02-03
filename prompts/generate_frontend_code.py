def generate_frontend_code(component="ChatUI", framework="React", styling="CSS", features=None):
    if features is None:
        features = []
    features_str = "\n".join([f"- {feature}" for feature in features])

    prompt = f"""
    Create a reusable {component} component. The component should:
    - Be compatible with {framework} and {styling}.
    - Include the following features:
    {features_str}
    - Use standard typescript to the best of your ability
    - Make sure response contains only code so that the output can run directly without any modification
    - Remove JSX indicator and triple quotes
    - Make sure only exisiting imports are used

    """

    return prompt

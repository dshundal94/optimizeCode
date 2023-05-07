import openai
import os

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def optimize_code(file_contents):
    """
    Optimizes the given code for mobile apps using OpenAI's GPT-4 model.

    Args:
        file_contents (str): The code to be optimized.

    Returns:
        Tuple[str, str]: A tuple containing the optimized code and an explanation of the optimizations.
    """

    # Prompt for the original code
    prompt = f"Optimize the following code for mobile apps and explain the changes:\n\n{file_contents}\n\nOptimized code:\n"

    # Use OpenAI's GPT-4 to generate optimized code
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that optimizes code for mobile apps and explains the changes."},
            {"role": "user", "content": prompt},
        ],
    )

    optimized_code = response.choices[0].message['content'].strip()

    # Prompt for explanations of optimizations
    prompt = f"Explanations for the optimizations:\n"

    # Use OpenAI's GPT-4 to generate explanations for the optimizations
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    explanations = response.choices[0].message['content'].strip()

    return optimized_code, explanations

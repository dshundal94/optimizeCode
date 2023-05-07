import openai
import os

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_tests(file_contents):
    """
    Generates test cases for the given code using OpenAI's GPT-4 model.

    Args:
        file_contents (str): The code for which test cases need to be generated.

    Returns:
        str: The generated test cases.
    """

    # Messages for generating test cases
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates test cases for given code."},
        {"role": "user", "content": f"Generate test cases for the following code:\n\n{file_contents}"}
    ]

    # Use OpenAI's GPT-4 to generate test cases
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1024,
    )

    test_cases = response.choices[0].message['content'].strip()

    
    return test_cases

import openai
import os

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")
def generate_tests(file_contents):
    prompt = f"Generate test cases for the following code:\n\n{file_contents}\n\nTest cases:\n"

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    test_cases = response.choices[0].text.strip()
    return test_cases

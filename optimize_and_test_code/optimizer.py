import openai
import os

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def optimize_code(file_contents):
    prompt = f"Optimize the following code for mobile apps and explain the changes:\n\n{file_contents}\n\nOptimized code:\n"
    
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    optimized_code = response.choices[0].text.strip()

    prompt = f"Explanations for the optimizations:\n"

    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    explanations = response.choices[0].text.strip()
    return optimized_code, explanations

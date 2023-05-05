# Code Optimization and Testing with GPT-4

This project uses OpenAI's GPT-4 API to optimize and generate tests for code files in a given directory.

## Setup

1. Clone this repository:

```bash
git clone https://github.com/your_username/repository_name.git
cd repository_name


2. Install the required packages:

pip install -r requirements.txt

3.Set up your OpenAI API key as an environment variable:

For Linux or macOS:

export OPENAI_API_KEY="your_api_key_here"

For Windows (in the Command Prompt):

set OPENAI_API_KEY="your_api_key_here"

For Windows (in PowerShell):

$env:OPENAI_API_KEY="your_api_key_here"

Replace your_api_key_here with your actual OpenAI API key.

Usage
To optimize and generate tests for code files in a directory, run the following command:

python main.py

This will create a new directory with the optimized code and test files. The new directory will have the same name as the original directory, but with _GPT appended to the end.

The script processes files with specific extensions. By default, it processes .dart, .flutter, .js, and .py files. Modify the file_extensions list in main.py to include other file types if needed.

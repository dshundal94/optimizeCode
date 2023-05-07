# Code Optimization and Testing with GPT-4

This project uses OpenAI's GPT-4 API to optimize for code files in a given directory.

## Setup

1. Clone this repository:

    ```
    git clone https://github.com/dshundal94/optimizeCode.git
    cd optimizeCode
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key as an environment variable:

### For Linux or macOS:

    
    export OPENAI_API_KEY="your_api_key_here"
    

### For Windows (in the Command Prompt):

    
    set OPENAI_API_KEY="your_api_key_here"
    

### For Windows (in PowerShell):

    
    $env:OPENAI_API_KEY="your_api_key_here"
    

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

To optimize for code files in a directory, run the following command:

    
    python main.py


This will create a new directory with the optimized code. The new directory will have the same name as the original directory, but with `_GPT` appended to the end.

The script processes files with specific extensions. By default, it processes `.dart`, `.flutter`,

## Update the input and output directory paths

In main.py, you can change the input and output directory paths. By default, the input directory is ./input_directory, and the output directory is ./output_directory. Modify the following lines with your desired paths:

    
    input_directory = './input_directory'
    output_directory = './output_directory'
    




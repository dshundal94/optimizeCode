import os
from optimize_and_test_code.optimizer import optimize_code

def main(source_directory, file_extensions):
    destination_directory = f"{source_directory}_GPT"
    os.makedirs(destination_directory, exist_ok=True)

    for root, _, files in os.walk(source_directory):
        for file in files:
            if not any(file.endswith(extension) for extension in file_extensions):
                continue
            
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                contents = f.read().strip()

            if not contents:  # Skip empty files
                continue

            optimized_contents, _ = optimize_code(contents)

            new_root = root.replace(source_directory, destination_directory)
            os.makedirs(new_root, exist_ok=True)

            # Save the optimized code
            new_file_name = os.path.splitext(file)[0] + os.path.splitext(file)[1]
            new_file_path = os.path.join(new_root, new_file_name)
            with open(new_file_path, "w") as f:
                f.write(optimized_contents)
            print(f"Optimized {file_path} and {new_file_path}")

if __name__ == "__main__":
    source_directory = r"/Users/hundalitis/Documents/optimizeCode"
    file_extensions = [".dart", ".flutter", ".js", ".py"]
    main(source_directory, file_extensions)

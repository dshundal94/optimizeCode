from optimize_and_test_code.optimizer import optimize_code
from optimize_and_test_code.tests_generator import generate_tests
import os

def main(source_directory, file_extensions):
    destination_directory = f"{source_directory}_GPT"
    os.makedirs(destination_directory, exist_ok=True)

    for root, _, files in os.walk(source_directory):
        for file in files:
            if any(file.endswith(extension) for extension in file_extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    contents = f.read()

                optimized_contents, explanations = optimize_code(contents)
                test_cases = generate_tests(contents)

                new_root = root.replace(source_directory, destination_directory)
                os.makedirs(new_root, exist_ok=True)

                # Save the optimized code in a new file
                new_file_path = os.path.join(new_root, file)
                with open(new_file_path, "w") as f:
                    f.write(optimized_contents)
                print(f"Optimized {file_path} and saved to {new_file_path}")

                # Save the test cases in a new file
                test_file_path = new_file_path.replace(".dart", "_test.dart")
                with open(test_file_path, "w") as f:
                    f.write(test_cases)
                print(f"Generated test cases for {new_file_path} and saved to {test_file_path}")

                # Save the explanations in a new file
                explanations_file_path = new_file_path.replace(".dart", "_explanations.txt")
                with open(explanations_file_path, "w") as f:
                    f.write(explanations)
                print(f"Saved optimization explanations for {new_file_path} to {explanations_file_path}")

if __name__ == "__main__":
    source_directory = r"/Users/hundalitis/Documents/optimizeCode"
    file_extensions = [".dart", ".flutter", ".js", ".py"]  # Add more file extensions as needed
    main(source_directory, file_extensions)

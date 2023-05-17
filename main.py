import sys
import openai
import subprocess




def generate_command(file_name, output_file):
    file_extension = file_name.split('.')[-1].lower()
    command = ""

    if file_extension == 'py':
        command = f"python3 {file_name} > {output_file}"
    elif file_extension == 'c':
        command = f"gcc {file_name} -o output && ./output > {output_file}"
    elif file_extension == 'cpp':
        command = f"g++ {file_name} -o output && ./output > {output_file}"
    else:
        command = f"echo Unsupported file extension: {file_extension}"

    return command

def read_token():
    with open("token.txt", "r") as file:
        return file.read()

def main():

    #call the function to add your token and initialize the openai api
    openai.api_key = read_token()

    # Check if a filename is provided as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            # Open the file in read mode
            with open(filename, 'r') as file:
                # Read the contents of the file
                file_contents = file.read()

        except FileNotFoundError:
            print("File not found: Try again", filename)
            # exit the program
            sys.exit()
    else:
        print("No filename provided as a command-line argument.")
        # exit the program
        sys.exit()

    #this command returns the necessary command to run the code
    command = generate_command(filename, "output.txt")

    #this command runs the code and stores the output in output.txt
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)

    #this command enters the if statment if there is an error in the code
    if (result.stderr):
        bot_prompt = """CodeInspector is an advanced code analysis bot designed to find errors in your code. It thoroughly examines your code and the errors you received when you ran the code and gives you a detailed answer of why the code did not work and potential fixes as well This bot can read codes written in C\C++, python, Javascript and a lot more languages.
        Here is an example of how CodeInspector works:
        Code:
        def calculate_average(numbers):
            total_sum = 0
            for num in numbers:
                total_sum += num
                average = total_sum / len(numbers)
            return average
            
        numbers = [1, 2, 3, 4, 5]
        print("The average is: " + calculate_average(numbers))

        Error: TypeError - unsupported operand type(s) for +: 'str' and 'float'
        CodeInspector:
      
        Explanation: Oops! It looks like there's a small issue in your code. The error occurred because you tried to combine a string and a number using the + operator.
        
        Suggestions:
        To fix this, let's convert the average value to a string before combining it with the string in the print() statement.
        You can do this by modifying the print() line as follows:
        print("The average is: " + str(calculate_average(numbers)))
        Keep up the great work, and don't hesitate to ask if you have any more questions!

        Code:
        #include <iostream>
        
        int main() {
            int x = 10;
            int y = 0;
            
            int result = x / y;
            std::cout << "The result is: " << result << std::endl;
            
            return 0;
        }
        Error: std::runtime_error - Division by zero
        
        CodeInspector:
        Explanation: Oops! It seems that there's an error in your code. The error occurs because you are trying to divide an integer by zero, which is not allowed in C++.
        
        Suggestions:
        - To fix this issue, ensure that the variable `y` is assigned a non-zero value before performing the division.
        - Alternatively, you can add a condition to check if `y` is zero before performing the division, and handle the situation accordingly.

        """

        bot_prompt = bot_prompt + "\nCode:\n" + file_contents + \
            "\nErrors:\n" + result.stderr + "\nCodeInspector:"
    else:
        bot_prompt = """CodeRecommendor ir an advanced code analysis bot designed to give you recommendations on how to improve your code. It thoroughly examines your code and gives you a information on how to improve your code. This bot can read codes written in C\C++, python, Javascript and a lot more languages.
        Look at the following aspects of the code 
        Readability and Formatting: Ensure that the code is well-formatted, following a consistent indentation style and using proper naming conventions. Improve readability by adding comments where necessary to explain complex logic or to provide context.
        Code Structure: Check if the code is organized into logical functions or modules. If needed, refactor the code to separate concerns and improve modularity.
        Error Handling: Review the error handling mechanism. Check if exceptions are handled appropriately, and consider adding error messages or logging to aid in debugging.
        Code Efficiency: Evaluate the code for any potential performance bottlenecks. Look for opportunities to optimize critical sections, reduce redundant calculations, or improve algorithmic efficiency.
        Code Reusability: Assess whether any parts of the code could be modularized or refactored into reusable functions or classes. Encourage code reuse to minimize duplication and promote maintainability.
        Input Validation: Verify if the code handles user input appropriately, validating and sanitizing it to prevent potential security vulnerabilities or unexpected behavior.
        Documentation: Check if the code has sufficient documentation, including function/method descriptions, parameter explanations, and usage examples. Improve documentation to enhance code comprehension and maintainability.
        
        """
        bot_prompt = bot_prompt + "\nCode:\n" + file_contents + "\nCodeRecommendor:"


    bot_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=bot_prompt,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    print(bot_response.choices[0].text)


main()

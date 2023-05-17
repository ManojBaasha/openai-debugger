# Debug Wrapper with OpenAI API

This repository serves as a wrapper to facilitate code debugging using the OpenAI API. It provides a convenient way to interact with the API and debug your code effectively.

## Prerequisites

Before using this wrapper, ensure that you have the following:

1. Python installed on your system.
2. An OpenAI API key. If you don't have one, you can obtain it from the [OpenAI website](https://openai.com).

## Installation

1. Clone this repository to your local machine using the following command:

   ```shell
   git clone https://github.com/your-username/debug-wrapper.git

2. Navigate to the cloned repository:

   ```shell
   cd debug-wrapper

3. Create a file named token.txt in the repository's root directory and paste your OpenAI API key into it. Ensure that the key is the only content in the file.

## Usage
1. To debug your code using the OpenAI API, follow these steps:
2. Place the file you want to debug in the debug-wrapper directory.
3. Open the command line and navigate to the debug-wrapper directory.
4. Run the Python script debug.py with the second command-line argument as the filename of your code. The filename can be a Python, C, or C++ code.

   ```
   py debug.py <filename>
   
  This wrapper will use the OpenAI API to analyze and debug your code.
  
 ## Feedback and Issues
 If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository. Your feedback is valuable and helps to enhance the debugging experience.

Note: Be cautious not to commit and push your token.txt file to any public repository, as it contains your API key and should remain confidential. Ensure it is added to your repository's .gitignore file.

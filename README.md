# AI Prompt Generator

A compact, floating Streamlit web application that helps users generate prompts for AI with various configuration options.

## Features

- Compact, floating UI that takes up minimal screen space
- Generate prompts with customizable options
- Choose language preference (English/Chinese/Spanish/French)
- Set file operation permissions (edit/generate)
- Control external request permissions
- Specify code quality and style preferences
- Configure performance and security options
- Specify testing requirements
- Set execution requirements
- Specify directories to check
- Available as a standalone .exe file (Windows)

## Installation

### Option 1: Install as a Python package

1. Ensure you have Python installed (3.7 or higher recommended)
2. Install the required packages:
   ```
   pip install streamlit
   ```

### Option 2: Build a standalone executable (Windows)

1. Ensure you have Python installed (3.7 or higher recommended)
2. Run the build script:
   ```
   python build_exe.py
   ```
3. The executable will be created in the `dist` folder as `AI_Prompt_Generator.exe`

## Usage

There are three ways to run the application:

### Option 1: Using the run script (Compact floating window)

Simply run the `run.py` script:

```
python run.py
```

This will launch the application in a compact, floating window mode.

### Option 2: Using Streamlit directly (Full browser window)

If you have Streamlit in your PATH, you can run:

```
streamlit run main.py
```

This will launch the application in a full browser window.

### Option 3: Using the standalone executable (Windows only)

If you've built the executable using Option 2 in the Installation section, simply double-click the `AI_Prompt_Generator.exe` file to launch the application in a compact, floating window.

## GitHub Integration

You can push your project to GitHub using the included utility:

### Using the batch file (Windows)

Simply run the `push_to_github.bat` file:

```
push_to_github.bat
```

### Using the Python script (Cross-platform)

Run the Python script directly:

```
python push_to_github.py
```

The utility will:
1. Check if Git is installed
2. Initialize a Git repository if needed
3. Prompt for your GitHub repository URL
4. Add/update the remote repository
5. Add all files to Git (respecting the .gitignore file)
6. Prompt for a commit message
7. Commit the changes
8. Prompt for a branch name (defaults to main)
9. Push to GitHub

### .gitignore Configuration

The project includes a `.gitignore` file that excludes the following from version control:

- Python cache files and bytecode (`__pycache__/`, `*.pyc`, etc.)
- Virtual environment directories (`venv/`, `ENV/`, etc.)
- IDE-specific files and directories (`.idea/`, `.vscode/`, etc.)
- System files (`.DS_Store`, etc.)
- Log files and databases (`*.log`, `*.sqlite3`, etc.)

This ensures that only the necessary source code and documentation are included in your Git repository.

## How to Use

1. Launch the application using one of the methods above
2. Enter your task for the AI in the text area on the left
3. Configure your prompt options using the tabs on the right:
   - **Language & Communication**: Choose response language and explanation detail
   - **File Operations**: Set file operation permissions and framework preferences
   - **Code Quality**: Configure code style, documentation, and error handling
   - **Testing & Execution**: Specify testing requirements and directory to check
4. Click the "Generate Prompt" button
5. The generated prompt will appear on the left side with a built-in copy button
6. Use the prompt with your preferred AI tool

## Options Explained

### Language & Communication
- **Response Language**: Choose the language for the AI's response (English, Chinese, Spanish, French)
- **Explanation Detail**: Set the level of detail in explanations (minimal, low, medium, high, comprehensive)

### File Operations
- **Allow AI to edit files**: When enabled, explicitly permits the AI to modify existing files
- **Allow AI to generate files**: When enabled, explicitly permits the AI to create new files
- **Ban external requests**: When enabled, instructs the AI not to make external API calls
- **Preferred Framework**: Specify a preferred framework for the AI to use
- **Compatibility Requirements**: Specify compatibility requirements for the code

### Code Quality
- **Code Style**: Specify a preferred code style (PEP8, Google, NumPy, etc.)
- **Documentation Level**: Set the level of documentation required
- **Include error handling**: When enabled, requests proper error handling and validation
- **Optimize for performance**: When enabled, requests optimization for performance
- **Include security considerations**: When enabled, requests security best practices

### Testing & Execution
- **Create unit tests**: When enabled, requests the AI to include unit tests
- **Run tests without modifying existing ones**: When enabled, specifies that tests should be run without modifying existing tests
- **Directory to check**: Specifies a particular directory the AI should focus on

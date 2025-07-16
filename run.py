import os
import subprocess
import sys
import tempfile
import webbrowser
import time
import atexit
import shutil

def create_config():
    """
    Create a temporary Streamlit config file to customize the app appearance.
    """
    config_dir = os.path.join(os.path.expanduser("~"), ".streamlit")
    os.makedirs(config_dir, exist_ok=True)

    config_path = os.path.join(config_dir, "config.toml")

    # Save original config if it exists
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            original_config = f.read()

        # Create a backup
        with open(f"{config_path}.backup", 'w') as f:
            f.write(original_config)
    else:
        original_config = None

    # Write compact window configuration
    with open(config_path, 'w') as f:
        f.write("""
[browser]
serverAddress = "localhost"
gatherUsageStats = false
serverPort = 8501
autoOpenBrowser = false

[theme]
base = "light"
primaryColor = "#1E88E5"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
baseUrlPath = ""
enableCORS = false
enableXsrfProtection = true
maxUploadSize = 200
maxMessageSize = 200
enableWebsocketCompression = true
headless = true

[runner]
magicEnabled = true
installTracer = true
fixMatplotlib = true
""")

    # Return the original config to restore later
    return original_config

def restore_config(original_config):
    """
    Restore the original Streamlit config file.
    """
    config_path = os.path.join(os.path.expanduser("~"), ".streamlit", "config.toml")

    if original_config is not None:
        with open(config_path, 'w') as f:
            f.write(original_config)
    else:
        # If there was no original config, remove the created one
        if os.path.exists(config_path):
            os.remove(config_path)

def main():
    """
    Run the Streamlit application using Python's subprocess module.
    This script helps users run the application without directly calling the Streamlit executable.
    Configures Streamlit to run in a compact, floating window.
    """
    print("Starting AI Prompt Generator...")

    # Create custom config for compact window
    original_config = create_config()

    # Register function to restore original config on exit
    atexit.register(lambda: restore_config(original_config))

    # Create a flag file to track if browser has been opened
    # This helps prevent multiple browser windows from opening
    flag_dir = tempfile.gettempdir()
    browser_flag_file = os.path.join(flag_dir, "ai_prompt_generator_browser_opened.flag")

    # Check if the flag file exists and is recent (less than 30 seconds old)
    browser_already_opened = False
    if os.path.exists(browser_flag_file):
        file_age = time.time() - os.path.getmtime(browser_flag_file)
        if file_age < 30:  # If file is less than 30 seconds old
            browser_already_opened = True
        else:
            # Flag file is old, remove it
            try:
                os.remove(browser_flag_file)
            except:
                pass

    # Get the path to the Python executable
    python_exe = sys.executable

    # Construct the command to run Streamlit
    streamlit_module = "-m streamlit run"
    main_script = "main.py"

    # Additional parameters for a compact window
    # Prevent auto-opening browser windows
    params = "--server.port=8501 --server.headless=true --browser.serverAddress=localhost --browser.gatherUsageStats=false --server.enableXsrfProtection=false --server.enableCORS=false --browser.serverPort=8501 --server.enableWebsocketCompression=true"

    # Full command
    command = f"{python_exe} {streamlit_module} {main_script} {params}"

    # Start the Streamlit server in the background
    try:
        process = subprocess.Popen(command, shell=True)

        # Wait a moment for the server to start
        time.sleep(2)

        # Open the browser only if it hasn't been opened recently
        if not browser_already_opened:
            print("Opening browser window...")
            # Create the flag file to indicate browser has been opened
            with open(browser_flag_file, 'w') as f:
                f.write(f"Browser opened at {time.ctime()}")

            # Open browser with reuse flag (new=0)
            webbrowser.open("http://localhost:8501/?embed=true", new=0, autoraise=True)
        else:
            print("Browser window already open, reusing existing window.")

        print("AI Prompt Generator is running. Close this window to exit.")

        # Wait for the process to complete
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()

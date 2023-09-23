import subprocess

# Define the name of the requirements file
requirements_file = "requirements.txt"

def install_dependencies():
    try:
        # Use pip to install the requirements from requirements.txt
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Dependencies have been successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install dependencies. {e}")
    except FileNotFoundError:
        print("Error: pip not found. Please ensure pip is installed and try again.")

if __name__ == "__main__":
    install_dependencies()

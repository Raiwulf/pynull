
# pynull
A python application that nullifies any files who match the regex filter and path provided by the user. The pyNull application is designed to process files in a specified directory by nulling (emptying) their content while creating backups of the original files. It also allows the user to configure the directory path and a regular expression filter for selecting files to be processed.

# pyNull GUI Application

This document describes the structure and functionality of the pyNuller GUI application written in Python using the Tkinter library.

## Code Structure

The code is organized into several sections, including:

### Imports

```python
import os
import re
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, Tk
import webbrowser
``````

### Constants

```python
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
FRAME0_PATH = ASSETS_PATH / "frame0"
FONT_FOLDER = ASSETS_PATH / "fonts"
ICON_FOLDER = ASSETS_PATH / "icons"
CONFIG_FILE = OUTPUT_PATH / "config.txt"
icon = ICON_FOLDER / "icon.ico"
```

### Utility Function

```python
def relative_to_assets(path: str) -> Path:
    return FRAME0_PATH / Path(path)
```

### GUI Setup

The GUI setup section includes creating the main Tkinter window, configuring its appearance, and defining various widgets such as canvas, buttons, and entry fields.

### Event Handlers

- `open_file_dialog()`: Opens a file dialog to select a directory.
- `process_files()`: Processes files in the selected directory, nulling their content and creating backups.
- `save_data()`: Saves user data to the configuration file.
- `load_data()`: Loads user data from the configuration file.
- `on_closing()`: Handles the application closing event.

### Main Application

The main application section creates the Tkinter window, sets its properties, and starts the main event loop. It also binds events to specific actions.

### "About" Button

A "About" button has been added to the top right corner of the window. It opens the GitHub page of the application's author when clicked.

```python
def open_github_url():
    webbrowser.open_new("https://github.com/Raiwulf/pynull")
```

## Usage

To use the pyNuller application:

1. Run the script.
2. Configure the directory path and regular expression filter.
3. Click the "Process" button to null files and create backups.
4. View the status and error messages in the log area.
5. The "About" button redirects you to the GitHub page for the author.

## Conclusion

The pyNuller application provides a simple GUI for nulling files in a directory with backup functionality. It is designed for ease of use and customization.

For more details or to contribute to the project, please visit the [GitHub repository](https://github.com/Raiwulf/pynull).

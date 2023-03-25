# Dual Cursor Autoclick

This Python script allows users to set two cursor positions and then automatically clicks on both positions simultaneously with a single hotkey.

## Usage

To use the script, simply run it with four command-line arguments specifying the hotkeys for setting the first cursor position, setting the second cursor position, triggering the autoclick loop, and pausing the loop, respectively. For example:

```bash
python dual_cursor_autoclick.py F5 F6 F7 F8
```

Once the script is running, press `F5` to set the first cursor position, `F6` to set the second cursor position, and `F7` to start the autoclick loop. The loop will automatically click on both cursor positions simultaneously every 5 milliseconds. To pause the loop, press `F8`.

## Requirements

- Python 3.x
- PyAutoGUI
- keyboard

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Open a command prompt or terminal and install PyAutoGUI and keyboard using pip:

```bash
pip install pyautogui keyboard
```

3. Download or clone the "dual_cursor_autoclick.py" file from this repository.
4. Run the script from the command line as described in the Usage section above.

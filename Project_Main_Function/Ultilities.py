import sys
import os 
import time
import textwrap

def slow_print(text, delay=0.05):
    """Prints text one character at a time with a delay for a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to a new line after printing the text


def clear_screen():
    """Clears the terminal screen for better visibility."""
    os.system("cls" if os.name == "nt" else "clear")

def wrap_text(text, width=80):
    """Wraps text to a specified width for better display."""
    return "\n".join(textwrap.wrap(text, width))
import sys
import time

def slow_print(text, delay=0.05):
    """Prints text one character at a time with a delay for a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to a new line after printing the text
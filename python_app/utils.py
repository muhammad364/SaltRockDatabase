def prompt_int(prompt, default=None):
    """
    Prompts the user for an integer, optionally with a default.
    """
    while True:
        val = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ")
        if not val and default is not None:
            return default
        try:
            return int(val)
        except ValueError:
            print("Invalid integer. Please try again.")

def prompt_float(prompt, default=None):
    """
    Prompts the user for a float, optionally with a default.
    """
    while True:
        val = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ")
        if not val and default is not None:
            return default
        try:
            return float(val)
        except ValueError:
            print("Invalid number. Please try again.")

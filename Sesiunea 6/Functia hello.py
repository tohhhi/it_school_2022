from unicodedata import name


def hello(name="Guest"):
    """Print welcome message. Default name is Guest."""
    print("Hello and welcome", name)

hello()
hello("Marian")
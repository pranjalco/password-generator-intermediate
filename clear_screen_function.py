import os


def clear_screen():
    """This function clear screen when called in terminal or command prompt"""
    os.system('cls' if os.name == 'nt' else 'clear')

#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""Entry point of Airbnb console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines HBNB Command Interpreter.
    
    Attributes:
        prompt: prompt string
    """
    
    prompt = "(hbnb) "
    
    def emptyline(self):
        """Does nothing when an empty line is entered."""
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True
    
if __name__ == '__main__':
    """
    Repeatedly issue a prompt, accept input, parse an initial prefix
    off the received input, and dispatch to action methods, passing them
    the remainder of the line as argument.
    (see: https://github.com/python/cpython/blob/3.8/Lib/cmd.py#L98)
    """
    HBNBCommand().cmdloop()
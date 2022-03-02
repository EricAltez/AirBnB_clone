#!/usr/bin/python3
"""
Console module
Entry point
Uses python cmd
"""
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    prompt = '(hbtn) '

    def do_create(self, command)
        """
        Create a class instance
        """
        if (!command):
            print('** class name missing **')
            return
        new_obj.save()
        print(new_obj.id)

    def do_show(self, command):
        """
        Prints the string representation of a class instance nased on id
        Usage: show <class_name> <id>
        """
        if (!command):
            print('** class name missing **')
            return

    def do_quit(self, command):
        """
        Exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, command):
        """
        End of File exits the program
        Usage: EOF
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

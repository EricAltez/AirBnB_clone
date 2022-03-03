#!/usr/bin/python3
"""
Console module
Entry point
Uses python cmd
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    prompt = '(hbtn) '

    def do_create(self, command):
        """
        Create a class instance
        """
        if (len(command) < 1):
            print('** class name missing **')
            return
        if command != "BaseModel":
            print ("** class doesn't exist **")
            return
        new_obj = BaseModel()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, command):
        """
        Prints the string representation of a class instance nased on id
        Usage: show <class_name> <id>
        """
        if (len(command) < 1):
            print('** class name missing **')
        com = command.split()
        if com[0] != "BaseModel":
            print ("** class doesn't exist **")
            return
        if len(com) < 2:
            print ("** instance id missing **")
            return
        try:
            print (storage.all()(f"{com[0]}"+ "." +"{com[1]}"))
        except:
            print ("** no instance found **")

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

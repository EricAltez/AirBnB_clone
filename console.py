#!/usr/bin/python3
"""
Console module
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbtn) '

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

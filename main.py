import cmd
import os

import file_reader


class cmdGreeter(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "

    print("BCDE321 Assignment by Jos and Lachlan")
    print("Converting ES6 to UML Python Application")
    print("You can type 'help' for a list of commands")


    def do_convert(self, path):
        """Usage: convert /path/to/javascript.js\nSelect the javascript file or folder to begin converting to UML"""

        if path:
            filenames = file_reader.get_filenames(path)
            print(filenames)
        else:

            print("Please include a valid path to the ES6")

    def do_exit(self, line):
        """exit the console application"""
        return True


if __name__ == '__main__':
    cmdGreeter().cmdloop()

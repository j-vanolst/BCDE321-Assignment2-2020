from cmd import Cmd

class Menu(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_quit(self, line):
        print("Quitting...")
        return True

if __name__ == "__main__":
    menu = Menu()
    menu.cmdloop()
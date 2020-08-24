from cmd import Cmd

# Local Imports
from model.analyser import JSAnalyser
from graph.grapher import Grapher

class Menu(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_analyse(self, path: str):
        """
        Syntax: analyse [path]
        Run an analysis on a file / folder
        :param path: a string representing the path to the file / folder for analysis
        :return: None
        """
        analyser = JSAnalyser(path)
        print(analyser)

    def do_draw_class_diagram(self, path: str):
        """
        Syntax: draw_class_diagram [path]
        Render a PDF class diagram of an es6 file / folder
        :param path: a string representing the path to the file / folder for analysis
        :return: None
        """
        analyser = JSAnalyser(path)
        classes = analyser.get_classes()
        grapher = Grapher(classes)
        grapher.render()

    def do_quit(self, line):
        print("Quitting...")
        return True


if __name__ == "__main__":
    menu = Menu()
    menu.cmdloop()
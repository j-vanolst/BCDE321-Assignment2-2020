from cmd import Cmd

# Local Imports
from database.sqlitedb import SqliteDB
from model.analyser import JSAnalyser
from graph.grapher import Grapher

class Menu(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.db = SqliteDB('analysis.db')

    def do_add_record(self, path: str):
        """
        Syntax: add_record [path]
        Run an analysis on a file / folder and create a record in the database
        storing file, class, attribute and method counts.
        :param path: a string representing the path to the file / folder for analysis
        :return: None
        """
        analyser = JSAnalyser(path)

        file_count = analyser.file_count()
        class_count = analyser.class_count()
        attribute_count = analyser.attribute_count()
        method_count = analyser.method_count()

        sql = f'insert into analysis (path, fileCount, classCount, attributeCount, methodCount) values ("{path}", {file_count}, {class_count}, {attribute_count}, {method_count})'
        self.db.query(sql)

    def do_get_record(self, path: str):
        """
        Syntax: get_record [path]
        Get an analysis record from the database
        :param path: a string representing the path to the file / folder record in the DB
        :return: None
        """
        sql = f'select path, fileCount, classCount, attributeCount, methodCount from analysis where path="{path}"'
        results = self.db.fetch(sql)
        if (len(results) == 0):
            print(f'No records found for path: {path}...')
        else:
            for aResult in results:
                print(f'Path: {aResult[0]}\n'
                      f'File Count: {aResult[1]}\n'
                      f'Class Count: {aResult[2]}\n'
                      f'Attribute Count: {aResult[3]}\n'
                      f'Method Count: {aResult[4]}')

    def do_delete_record(self, path: str):
        """
        Syntax: delete_record [path]
        Remove an analysis record from the database
        :param path: a string representing the path of the file / folder record in the DB
        :return: None
        """
        sql = f'delete from analysis where path="{path}"'
        self.db.query(sql)

    def do_list_records(self, line):
        """
        Syntax: list_records
        Lists all stored analysis records in the database
        :return: None
        """
        sql = f'select path from analysis'
        results = self.db.fetch(sql)
        if (len(results) == 0):
            print('No records in the database...')
        else:
            for aResult in results:
                print(aResult)

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
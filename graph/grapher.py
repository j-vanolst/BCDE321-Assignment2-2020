from graphviz import Digraph, render
from model.analyser import JSAnalyser

analyser = JSAnalyser('../test/test_files/single_file_single_class.js')

print(analyser)

class Grapher:
    def __init__(self):
        self.graph = Digraph()

        self.graph_config()
        self.add_node()
        self.render()

    def graph_config(self):
        self.graph.attr('node', shape='record', fontname='Bitstream Vera Sans', fontsize='8')
        self.graph.attr('edge', dir='back', arrowtail='empty')

    def add_node(self):
        self.graph.node('A', '{Animal|name\\lage\\l|constructor(self, name)\\lgreet()\\l}')
        self.graph.node('B', '{Animal|name\\lage\\l|constructor(self, name)\\lgreet()\\l}')

    def render(self):
        self.graph.render('test.gv', view=True)
        render('dot', 'pdf', 'test.gv')

grapher = Grapher()
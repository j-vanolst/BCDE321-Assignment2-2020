import filecmp

from model.analyser import JSAnalyser
from graph.grapher import Grapher

analyser = JSAnalyser('test_files/single_file_single_class.js')
graph = Grapher(analyser.get_classes())
graph.render()

print(filecmp.cmp('output/output.pdf', 'output/output.pdf'))
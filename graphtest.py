from graphviz import Digraph, render
dot = Digraph()

dot  #doctest: +ELLIPSIS
dot.attr('node', shape='record', fontname='Bitstream Vera Sans', fontsize='8')
dot.attr('graph', splines='false')

dot.attr('edge', arrowtail="empty")
dot.node('A', 'King Arthur')


dot.node('B', '{MonotypeDelivery|\l|+ ship(): boolean\l}')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])




dot.edge('B', 'L', dir="back")
print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
'test-output/round-table.gv.pdf'
render('dot', 'pdf','view/output/round-table.gv')
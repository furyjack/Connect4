from graphviz import Digraph

def _create_graph(dot, node):
    #node.isimp = True
    if len(node.children) == 0 and node.isimp:
        dot.node(str(node), str(node.val))
        return

    if node.isimp:
        dot.node(str(node), str(node.val))
    for i,child in enumerate(node.children):
        #child.isimp = True
        if child.isimp:
            _create_graph(dot, child)
            dot.edge(str(node), str(child), str(child.lastmove[0]) + '-' + str(child.lastmove[1]))





def create_graph(root):
    dot =  Digraph(comment='Tree')
    _create_graph(dot, root)
    print(dot.source)
    dot.render('tree.gv', view=True)

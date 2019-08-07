import graphadjacencylist


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Graph Theory  |")
    print("-----------------\n")

    g = create_graph()

    # print(g)

    g = edit_graph(g)

    print(g)


def create_graph():

    g = graphadjacencylist.GraphAdjacencyList()

    g.add_vertex("Inverness")
    g.add_vertex("Aberdeen")
    g.add_vertex("Glasgow")
    g.add_vertex("Edinburgh")

    g.add_edge("Inverness", "Aberdeen", directed=False, weight=103)
    g.add_edge("Inverness", "Glasgow", directed=False, weight=168)
    g.add_edge("Inverness", "Edinburgh", directed=False, weight=154)

    g.add_edge("Aberdeen", "Glasgow", directed=False, weight=139)
    g.add_edge("Aberdeen", "Edinburgh", directed=False, weight=119)

    g.add_edge("Glasgow", "Edinburgh", directed=False, weight=44)

    return g


def edit_graph(g):

    g.edit_vertex("Inverness", "Inerness")
    g.edit_vertex("Aberdeen", "Aiberdeen")
    g.edit_vertex("Glasgow", "Glesga")

    return g


main()

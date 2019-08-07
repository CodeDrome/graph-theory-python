import vertex
import edge


class GraphAdjacencyList(object):

    def __init__(self):

        self.vertices = []

    def __str__(self):

        hline = ("-" * 44) + "\n"
        leftspace = ("|" + (" " * 16) + "|")
        string = []

        string.append(hline)
        string.append("|    Vertices    |    Edge To     | Weight |\n")
        string.append(hline)

        for vertex in self.vertices:

            string.append("|{0: <16}|".format(vertex.label))

            if len(vertex.edges) > 0:

                for index, edge in enumerate(vertex.edges):

                    if index > 0:
                        string.append(leftspace)

                    string.append("{0: <16}|".format(edge.to))

                    if edge.weight is not None:
                        string.append("{0: 8}|".format(edge.weight))
                    else:
                        string.append((" " * 8) + "|")

                    string.append("\n")

                string.append(hline)

            else:

                string.append((" " * 16) + "|" + (" " * 8) + "|\n")
                string.append(hline)

        return "".join(string)

    def add_vertex(self, label):

        """
        Adds a vertex with the given label to the list.
        Raises ValueError if already exists.
        """

        if self.__find_vertex_index(label) == -1:
            v = vertex.Vertex(label)
            self.vertices.append(v)
        else:
            raise ValueError("Vertex with this label already exists")

    def add_edge(self, label1, label2, directed, weight):

        """
        Adds edge between given two vertices with given weight.
        Recursively adds "reverse" edge if directed is False.
        Raises ValueError if edge already exists, or if
        either or both vertices do not exist.
        """

        if self.__edge_exists(label1, label2) is True:
            raise ValueError("Edge already exists")
        else:
            index1 = self.__find_vertex_index(label1)
            index2 = self.__find_vertex_index(label2)

            if index1 == -1 or index2 == -1:
                raise ValueError("One or both vertices not found")

            else:
                e1 = edge.Edge(label2, weight)
                self.vertices[index1].edges.append(e1)

                if directed is False:
                    self.add_edge(label2, label1, True, weight)

    def edit_vertex(self, label, new_label):

        """
        Changes vertex name to new value.
        Raises ValueError if label does not exist.
        """

        found = False

        for vertex in self.vertices:

            if vertex.label == label:
                vertex.label = new_label
                found = True

            for edge in vertex.edges:
                if edge.to == label:
                    edge.to = new_label

        if not found:
            raise ValueError("Vertex with this label does not exist")

    def edit_edge(self, from_label, to_label, weight):

        """
        Changes the weight of the edge to/from the
        given labels to new value.
        Raises ValueError if edge does not exist.
        """

        found = False

        for vertex in self.vertices:
            if vertex.label == from_label:
                for edge in vertex.edges:
                    if edge.to == to_label:
                        edge.weight = weight
                        found = True

        if not found:
            raise ValueError("Edge between labels does not exist")

    def delete_vertex(self, label):

        """
        Deletes the vertex with the given label.
        Raises ValueError if label does not exist.
        """

        found = False

        for vertex in self.vertices:

            for edge in vertex.edges:
                if edge.to == label:
                    vertex.edges.remove(edge)

            if vertex.label == label:
                self.vertices.remove(vertex)
                found = True

        if not found:
            raise ValueError("Vertex with this label does not exist")

    def delete_edge(self, from_label, to_label):

        """
        Deletes edge from/to given labels.
        Raises ValueError if edge does not exist.
        """

        found = False

        for vertex in self.vertices:
            if vertex.label == from_label:
                for edge in vertex.edges:
                    if edge.to == to_label:
                        vertex.edges.remove(edge)
                        found = True

        if not found:
            raise ValueError("Edge between labels does not exist")

    def __find_vertex_index(self, label):

        for index, vertex in enumerate(self.vertices):
            if vertex.label == label:
                return index

        return -1

    def __edge_exists(self, label1, label2):

        vertex_index = self.__find_vertex_index(label1)

        for edge in self.vertices[vertex_index].edges:
            if edge.to == label2:
                return True

        return False

from graph_interpretations import Adjacency
from graph_interpretations import Incidence


def main():
    adjacency = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1]
    ]

    incidence = [
        [1, 1, 0, 0, 0, -1, 0, -1, 0, 0],
        [-1, 0, 2, 1, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, -1, 0, 0, 0],
        [0, 0, 0, -1, 0, 1, 1, 0, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 2]
    ]

    source_adjacency: Adjacency = Adjacency(matrix=adjacency)
    returned_incidence: Incidence = Incidence(graph=source_adjacency.get_graph())

    source_incidence: Incidence = Incidence(matrix=incidence)
    returned_adjacency: Adjacency = Adjacency(graph=source_incidence.get_graph())

    print(returned_incidence)
    print(returned_adjacency)
    return


if __name__ == "__main__":
    main()

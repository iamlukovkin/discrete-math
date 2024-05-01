class GraphMethods:
    @staticmethod
    def depth_first_search(node, visited, stack, graph):
        visited[node] = True

        for neighbor in range(len(graph)):
            if graph[node][neighbor] and not visited[neighbor]:
                GraphMethods.depth_first_search(neighbor, visited, stack, graph)
        stack.append(node)

        return node, visited, stack, graph

    @staticmethod
    def find_min_paths(graph: list[list[int]]) -> list[int]:
        order = GraphMethods.sort_topologically(graph)
        dp_array = [0] * len(graph)

        for node in order:
            for idx in range(len(graph)):
                if graph[idx][node] != 0:
                    dp_array[node] = max(dp_array[node], dp_array[idx] + graph[idx][node])

        return dp_array

    @staticmethod
    def sort_topologically(graph):
        visited, stack = [False] * len(graph), []

        for node in range(len(graph)):
            if not visited[node]:
                GraphMethods.depth_first_search(node, visited, stack, graph)

        return stack[::-1]

    @staticmethod
    def find_shortest_path(graph, source, destination) -> list[float]:
        num_nodes = len(graph)
        distances = [float('inf')] * num_nodes
        distances[source] = 0

        for current_node in range(source, destination + 1):
            for next_node in range(num_nodes):
                if graph[current_node][next_node] != 0:
                    new_distance = distances[current_node] + graph[current_node][next_node]
                    if new_distance < distances[next_node]:
                        distances[next_node] = new_distance

        return distances[destination]

    @staticmethod
    def find_start_node(adjacency_matrix):
        num_nodes = len(adjacency_matrix)
        in_degrees = [sum(1 for edge in row if edge < num_nodes) for row in adjacency_matrix]

        for index, degree in enumerate(in_degrees):
            if degree == 0:
                return index

        return -1

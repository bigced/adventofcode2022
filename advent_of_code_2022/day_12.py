import string

import networkx as nx
import numpy as np


def char_to_index(char):
    if char == "S":
        return 1
    if char == "E":
        return 26
    return string.ascii_lowercase.index(char) + 1


def get_neighbour_edges(x, y, area):
    edges = []
    current_node = index_to_node(len(area[0]), y, x)
    current_value = char_to_index(area[y][x])

    if x > 0 and char_to_index(area[y][x - 1]) <= current_value + 1:
        edges.append([current_node, index_to_node(len(area[0]), y, x - 1)])
    if x < len(area[0]) - 1 and char_to_index(area[y][x + 1]) <= current_value + 1:
        edges.append([current_node, index_to_node(len(area[0]), y, x + 1)])
    if y > 0 and char_to_index(area[y - 1][x]) <= current_value + 1:
        edges.append([current_node, index_to_node(len(area[0]), y - 1, x)])
    if y < len(area) - 1 and char_to_index(area[y + 1][x]) <= current_value + 1:
        edges.append([current_node, index_to_node(len(area[0]), y + 1, x)])
    return edges


def build_graph_from_area(area):
    graph = nx.DiGraph()
    for index_y, line in enumerate(area):
        for index_x, cell in enumerate(line):
            edges = get_neighbour_edges(index_x, index_y, area)
            for edge in edges:
                graph.add_edge(edge[0], edge[1])
    return graph


def calculate_steps(graph, start, dest):
    return len(nx.shortest_path(graph, source=start, target=dest)) - 1


def calculate_steps_from_file(filename):
    area = get_area_data_from_file(filename)
    start = get_node(area, "S")
    dest = get_node(area, "E")
    graph = build_graph_from_area(area)
    return calculate_steps(graph, start, dest), part_2(graph, area, dest)


def index_to_node(row_length, y, x):
    return (y * row_length) + x + 1


def get_node(area, char):
    dest = np.where(area == char)
    return index_to_node(len(area[0]), int(dest[0]), int(dest[1]))


def get_area_data_from_file(filename):
    return np.genfromtxt(filename, delimiter=1, dtype=str)


def get_starting_nodes(area):
    nodes = []
    options = np.where(area == "a")
    for i in range(len(options[0])):
        nodes.append(index_to_node(len(area[0]), int(options[0][i]), int(options[1][i])))
    nodes.append(get_node(area, "S"))
    return nodes


def part_2(graph, area, dest):
    options = get_starting_nodes(area)
    shortest_path = None
    for option in options:
        try:
            attempted_path = calculate_steps(graph, option, dest)
            if not shortest_path:
                shortest_path = attempted_path
            elif attempted_path < shortest_path:
                shortest_path = attempted_path
        except nx.NetworkXNoPath:
            pass
    return shortest_path


if __name__ in "__main__":
    steps, steps_2 = calculate_steps_from_file("day_12.txt")
    print(f"There's {steps} steps and {steps_2}")

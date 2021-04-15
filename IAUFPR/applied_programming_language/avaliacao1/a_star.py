"""
Módulo que contém o algoritmo de busca A*.
"""
from dists import dists
from utils import get_solution_path
from dists import straight_line_dists_from_bucharest as h_table
from utils import cost_function as f

# Desculpa profe, mas vou "re-formatar" alguns dados originais aqui
# Transformarei as tuplas de par-valor listadas no dicionário de distâncias
# em um hashmap puro: um dicionário de dicionários.
# Os dicionários python ja apresentam uma estrutura de nó naturalmente.
data = {key: {k: v for k, v in value} for key, value in dists.items()}


def a_star(start, data, h_data, target='Bucharest'):
    """
    Esta função implementa um algoritmo de A* para encontrar o caminho de
    um ponto inicial até um objetivo dado um dicionário de 'nós' contendo
    os 'filhos' e suas respectivas distâncias (custos) para cada possível
    nó vizinho. O dicinário DEVE conter a estrutura abaixo:

    {
        <str> : {
            <str>: <int>,
            <str>: <int>,
            ...
        },
        ...
    }

    param : target : <str> -> Nó objetivo;
    param : data : <dict> -> Estrutura de nós (listada acima);
    param : h_data : <dict> -> Heurística para cada nó;
    param : start : <str> -> Nó inicial;
    return : <list>
    """
    steps = 0
    edge = []
    explored = []

    node = data[start]
    f_node = f(steps, 0, h_data[start])  # custo do nó
    edge.append([start, f_node])  # inicializa a borda (fila)
    previous = start

    while edge:
        if not edge:
            # Se não mais existir a borda, retornamos alguma solução
            return get_solution_path(start, target, explored, data)

        # Atualiza informações sobre o nó removendo o primeiro item da borda
        node_tuple = edge.pop(0)
        node_name, f_node, = node_tuple[0], node_tuple[1]
        steps += data[previous].get(node_name, 0)
        explored.append(node_name)
        possibilities = data[node_name]

        if node_name == target:
            # Se estivermos sobre o nó objetivo, retornamos alguma solução
            return get_solution_path(start, target, explored, data)

        for child in possibilities:
            # Calcula o custo do filho
            f_child = f(steps, data[node_name][child], h_data[child])
            child_node = [child, f_child]
            edge_labels = [node[0] for node in edge]

            if child not in edge_labels and child not in set(explored):
                edge.append(child_node)

            else:
                for node in edge:
                    if child == node[0] and f_child > node[1]:
                        edge[edge.index(node)][1] = f_child

        # Memoriza este nó como "anterior" para a próxima iteração
        previous = node_name

        # Ordena a fila de prioridades
        edge = sorted(edge, key=lambda node: node[1])

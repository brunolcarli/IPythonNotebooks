"""
Ferramentas e utilitários.
Este módulo disponibiliza ferramentas (algoritmos) para auxiliar o
processamento principal.
"""


class StdOutTexts:
    """
    Saída de texto padrão para o módulo principal.
    """
    GET_START_POINT = 'Insira o nome do ponto de partida:\n'
    INVALID_LOCATION = '\nLocalização não suportada.\n'
    CONTINUE = '\n\nDeseja continuar? sim/não\n'
    FINISH = '\nEncerrando!\n'
    SLOGAN = '\n\nEncontramos a melhor rota\nde qualquer ' \
             'lugar na Romênia para Bucareste.\n\n'
    SOLUTION = '\nMelhor Solução encontrada:\n'
    DASH = '----------------------------------\n'
    BANNER = '''
    ╔╗ ┬ ┬┌─┐┬ ┬┌─┐┬─┐┌─┐┌─┐┌┬┐ 
    ╠╩╗│ ││  ├─┤├─┤├┬┘├┤ └─┐ │  
    ╚═╝└─┘└─┘┴ ┴┴ ┴┴└─└─┘└─┘ ┴  
            ╔═╗┬┬─┐┬  ┬┌┐┌┌─┐┌─┐
            ╠═╣│├┬┘│  ││││├┤ └─┐
            ╩ ╩┴┴└─┴─┘┴┘└┘└─┘└─┘
    '''
    AUTHOR = '\nDeveloped by: Bruno L. Carli\n'


def cost_function(steps, cost, h):
    """
    Calcula f(n) sendo a função de custo de um nó.

    param : steps : <int> -> Total de passos dados;
    param : cost : <int> ->Custo para se deslocar ao nó;
    param : h : <int> -> Heurística do custo entre posição atual até o objetivo;
    return : <int>
    """
    return (steps + cost) + h


def get_solution_path(start, target, explored, data):
    """
    Anda de 'trás-pra-frente' pelos nós explorados verificando se
    seus vizinhos para definir o caminho até o objetivo, retornando uma
    lista de nós.

    param : start : <str> -> Nome da cidade (ponto atual]);
    param : target : <str> -> Nome da cidade alvo;
    param : explored : <list> -> Lista de nomes ja exploradas;
    param : data : <dict> -> Dicionários de nós (cidades);

    return : <list> of <str>
    """
    solution = []

    # move backwards to find the path
    explored = list(reversed(explored))
    for node in explored:
        if node == start:
            solution.insert(0, node)
            return solution

        connections = list(data[node])
        try:
            next_node = explored[explored.index(node)+1]
        except IndexError:
            if node == start:
                solution.insert(0, node)
        else:
            if not next_node in connections:
                del explored[explored.index(next_node)]
                solution.insert(0, node)
            else:
                solution.insert(0, node)

    return solution

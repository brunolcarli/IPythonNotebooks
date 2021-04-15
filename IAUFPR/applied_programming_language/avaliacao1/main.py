"""
Módulo principal de execução do programa.
Este é um programa lúdico utilizado como proposta avaliativa da
disciplina de Programação Aplicada do cursod e Especialização em
Inteligência Artificial da Universidade Federal do Paraná - UFPR.

Autor/Aluno: Bruno Luvizotto Carli
Curitiba/PR - 2012
"""
from sys import stdout
from a_star import a_star, h_table, data
from utils import StdOutTexts


if __name__ == '__main__':
    stdout.write(StdOutTexts.DASH)
    stdout.write(StdOutTexts.BANNER)
    stdout.write(StdOutTexts.SLOGAN)
    stdout.write(StdOutTexts.AUTHOR)
    stdout.write(StdOutTexts.DASH)

    while True:
        # Solicita um local de partida
        start_point = input(StdOutTexts.GET_START_POINT).title()
        
        if start_point not in data:
            stdout.write(StdOutTexts.INVALID_LOCATION)
        else:
            solution = a_star(start_point, data, h_table)

            stdout.write(StdOutTexts.SOLUTION)
            stdout.write(' -> '.join(item for item in solution))

        # Solicita ao usuário se deseja continuar
        loop_again = input(StdOutTexts.CONTINUE).lower()
        if loop_again in ('n', 'não', 'nao'):
            stdout.write(StdOutTexts.FINISH)
            break

    stdout.write(StdOutTexts.DASH)

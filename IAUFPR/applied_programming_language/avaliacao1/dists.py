#{
#    city1: [(neighbor_city, dist), ...],
#    city2: ...
#}
dists = {
    'Bucharest': [
        ('Urzineci',85),
        ('Giurgiu',90),
        ('Pitesti',101),
        ('Fagaras',211)
    ],
    'Giurgiu': [
        ('Bucharest',90)
    ],
    'Urzineci': [
        ('Bucharest',85),
        ('Hirsova',98),
        ('Vaslui',142)
    ],
    'Hirsova': [
        ('Urzineci',98),
        ('Eforie',86)
    ],
    'Eforie': [
        ('Hirsova',86)
    ],
    'Vaslui': [
        ('Urzineci',142),
        ('Iasi',92)
    ],
    'Iasi': [
        ('Vaslui', 92),
        ('Neamt',87)
    ],
    'Neamt': [
        ('Iasi', 87)
    ],
    'Fagaras': [
        ('Bucharest',211),
        ('Sibiu',99)
    ],
    'Pitesti': [
        ('Bucharest',101),
        ('Rimnicu Vilcea',97),
        ('Craiova',138)
    ],
    'Craiova':[
        ('Pitesti',138),
        ('Rimnicu Vilcea',146),
        ('Dobreta',120)
    ],
    'Rimnicu Vilcea':[
        ('Craiova',146),
        ('Pitesti',97),
        ('Sibiu',80)
    ],
    'Sibiu':[
        ('Rimnicu Vilcea',80),
        ('Fagaras',99),
        ('Oradea',151),
        ('Arad',140)
    ],
    'Oradea':[
        ('Sibiu',151),
        ('Zerind',71)
    ],
    'Zerind':[
        ('Oradea',71),
        ('Arad',75)
    ],
    'Arad':[
        ('Zerind',75),
        ('Timisoara',118),
        ('Sibiu',140)
    ],
    'Timisoara':[
        ('Arad',118),
        ('Lugoj',111)
    ],
    'Lugoj':[
        ('Timisoara',111),
        ('Mehadia',70)
    ],
    'Mehadia':[
        ('Lugoj',70),
        ('Dobreta',75)
    ],
    'Dobreta':[
        ('Mehadia',75),
        ('Craiova',120)
    ],
}

#{
#    city1: dist,
#    city2: dist,
#    ...
#}
straight_line_dists_from_bucharest = {
    'Arad': 366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urzineci':80,
    'Vaslui':199,
    'Zerind':374
}

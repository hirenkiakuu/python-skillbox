players = {
("Ivan", "Volkin"): (10, 5, 13),
("Bob", "Robbin"): (7, 5, 14),
("Rob", "Bobbin"): (12, 8, 2)
}

result = [(player + score) for player, score in players.items()]

print(result)

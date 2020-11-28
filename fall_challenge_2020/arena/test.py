from game import Game

g = Game(["/bin/sh"], ["/bin/sh"])
a = g.generate_msg(g.player1, g.player2)
print(len(a))
print(a)
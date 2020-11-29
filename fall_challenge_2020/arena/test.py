import os
import subprocess

from game import Game

bot = os.path.dirname(os.path.abspath(__file__)) + "/test_player.py"
g = Game([bot], [bot], debug=True)
g.match()

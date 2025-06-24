# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
#from RPS import player
from unittest import main
from RPS import MarkovBot

bot = MarkovBot(order=4)

#play(bot.playy, quincy, 1000)
#play(bot.playy, abbey, 1000)
#play(bot.playy, kris, 1000)
#play(bot.playy, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)

# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)
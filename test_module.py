import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
#from RPS import player
from RPS import MarkovBot

player = MarkovBot(order=4)
class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player.playy, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.')

    def test_player_vs_abbey(self):
        print("Testing game against abbey...")
        actual = play(player.playy, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat abbey at least 60% of the time.')

    def test_player_vs_kris(self):
        print("Testing game against kris...")
        actual = play(player.playy, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat kris at least 60% of the time.')

    def test_player_vs_mrugesh(self):
        print("Testing game against mrugesh...")
        actual = play(player.playy, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat mrugesh at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()

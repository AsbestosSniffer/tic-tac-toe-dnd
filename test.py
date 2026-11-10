import unittest
from tictactoe import *
import json

class TestValidInputs(unittest.TestCase):

    def test_tooshort(self):
        self.assertIsNone(validate_input('3'))
    def test_notint(self):
        self.assertIsNone(validate_input('___'))
    def test_outofbounds(self):
        self.assertIsNone(validate_input('1,4'))
    def test_valid(self):
        self.assertIsNotNone(validate_input('3,1'))

# class TestGameRuns(unittest.TestCase):
# 
#     def test_XWins(self):

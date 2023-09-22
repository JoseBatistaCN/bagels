from bagels import BagelsGame
import unittest


class BagelsTest(unittest.TestCase):
    def setUp(self):
        self.game = BagelsGame()

    def testGenerateMinAndMaxNumbersDefault(self):
        default_gen = self.game.generateMinAndMaxValue()

        self.assertEqual((100, 999), default_gen)

    def testGenerateMinAndMaxNumbersNotNumber(self):
        with self.assertRaises(ValueError):
            self.game.generateMinAndMaxValue("")

    def testGenerateMinAndMaxNumbersOtherNumber(self):
        fourDigitsGen = self.game.generateMinAndMaxValue(4)

        self.assertEqual((1000, 9999), fourDigitsGen)

    def testGenerateMinAndMaxNumbersNotPositiveNumber(self):
        with self.assertRaises(ValueError):
            self.game.generateMinAndMaxValue(-1)


    def testGenerateThoughtNumber(self):
        (min_range, max_range) = (100, 999)
        thought_number = self.game.generateThoughtNumber()
        
        self.assertTrue(min_range <= thought_number <=max_range)
        
    
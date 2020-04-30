import unittest
import romanos


class RomanNumberTest(unittest.TestCase):
    def test_symbols_roman(self):
        self.assertEqual(romanos.romano_a_entero('I'), 1)
        self.assertEqual(romanos.romano_a_entero('V'), 5)
        self.assertEqual(romanos.romano_a_entero('X'), 10)
        self.assertEqual(romanos.romano_a_entero('L'), 50)
        self.assertEqual(romanos.romano_a_entero('C'), 100)
        self.assertEqual(romanos.romano_a_entero('D'), 500)
        self.assertEqual(romanos.romano_a_entero('M'), 1000)
        self.assertEqual(romanos.romano_a_entero('KK'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero(''), 'Error en formato')

    def test_repetition(self):
        self.assertEqual(romanos.romano_a_entero('II'), 2)
        self.assertEqual(romanos.romano_a_entero('MMM'), 3000)
        self.assertEqual(romanos.romano_a_entero('KKK'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('MK'), 'Error en formato')

    def only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error en formato')

    def test_decreasing_numbers(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error en formato')


if __name__ == "__main__":
    unittest.main()

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

    def test_only_five(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error en formato')

    def test_decreasing_numbers(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('III'), 3)
        self.assertEqual(romanos.romano_a_entero('XI'), 11)
        self.assertEqual(romanos.romano_a_entero('XV'), 15)
        self.assertEqual(romanos.romano_a_entero('XX'), 20)

    def test_digitos_restan(self):
        self.assertEqual(romanos.romano_a_entero('XIX'), 19)

    def test_resta_separacion_un_grado(self):
        self.assertEqual(romanos.romano_a_entero('XC'), 90)
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XD'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XM'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error en formato')

    def test_resta_de_multiplos_5_no(self):
        self.assertEqual(romanos.romano_a_entero('VC'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XCV'), 95)

    def test_resta_un_solo_simbolo(self):
        self.assertEqual(romanos.romano_a_entero('XXL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IXL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XXX'), 30)


class RomantoIntegerTest(unittest.TestCase):
    def test_traduccion_digitos_simples(self):
        self.assertEqual(romanos.entero_a_romano(1), 'I')
        self.assertEqual(romanos.entero_a_romano(10), 'X')
        self.assertEqual(romanos.entero_a_romano(5), 'V')
        self.assertEqual(romanos.entero_a_romano(50), 'L')
        self.assertEqual(romanos.entero_a_romano(100), 'C')
        self.assertEqual(romanos.entero_a_romano(500), 'D')
        self.assertEqual(romanos.entero_a_romano(1000), 'M')

    def test_traduccion_digitos_complejos_unidades(self):
        self.assertEqual(romanos.entero_a_romano(2), 'II')
        self.assertEqual(romanos.entero_a_romano(3), 'III')
        self.assertEqual(romanos.entero_a_romano(4), 'IV')
        self.assertEqual(romanos.entero_a_romano(6), 'VI')
        self.assertEqual(romanos.entero_a_romano(7), 'VII')
        self.assertEqual(romanos.entero_a_romano(8), 'VIII')
        self.assertEqual(romanos.entero_a_romano(9), 'IX')
        self.assertEqual(romanos.entero_a_romano(30), 'XXX')
        self.assertEqual(romanos.entero_a_romano(200), 'CC')
        self.assertEqual(romanos.entero_a_romano(400), 'CD')
        self.assertEqual(romanos.entero_a_romano(3000), 'MMM')

    def test_busca_valor(self):
        self.assertEqual(romanos.busca_valor_menor_o_igual(2), ('I', 1))
        self.assertEqual(romanos.busca_valor_menor_o_igual(5), ('V', 5))
        self.assertEqual(romanos.busca_valor_menor_o_igual(7), ('V', 5))

    def test_descomponer(self):
        self.assertEqual(romanos.descomponer(1942), [1000, 900, 40, 2])

    def test_entero_a_romano(self):
        self.assertEqual(romanos.entero_a_romano(1942), 'MCMXLII')
        self.assertEqual(romanos.entero_a_romano(3999), 'MMMCMXCIX')
        self.assertEqual(romanos.entero_a_romano(4000), 'Overflow')


if __name__ == "__main__":
    unittest.main()

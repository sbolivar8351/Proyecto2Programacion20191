from unittest import TestCase
import Cliente as c

class  test_obtener_complemento(TestCase):

    def test_obtener_complemento(self):
        self.assertEqual(c.obtener_complemento('G'), 'C')
        self.assertEqual(c.obtener_complemento(0), 0)
        self.assertEqual(c.obtener_complemento('T'), 'A')
        self.assertEqual(c.obtener_complemento(0), 0)



    def Test_generar_cadena_complementaria(self):
            self.assertEqual(c.generar_cadena_complementaria('GGT'), 'CCA')
            self.assertEqual(c.generar_cadena_complementaria(0), 0)
            self.assertEqual(c.generar_cadena_complementaria('TTT'), 'AAA')
            self.assertEqual(c.generar_cadena_complementaria(0), 0)
            self.assertEqual(c.generar_cadena_complementaria('TGT'), 'ACA')
            self.assertEqual(c.generar_cadena_complementaria(0), 0)
            self.assertEqual(c.generar_cadena_complementaria('GTG'), 'CAC')
            self.assertEqual(c.generar_cadena_complementaria(0), 0)


class TestCalcular_correspondencia(TestCase):
        def Test_calcular_correspondencia(self):
            self.assertEqual(c.calcular_correspondencia('CAT', 'GTA'), 100.0)
            self.assertEqual(c.calcular_correspondencia(0), 0)

class TestCorresponden(TestCase):
        def test_corresponden(self):
            self.assertEqual(c.corresponden('TAT'), 'ATA')
            self.assertEqual(c.corresponden(0), 0)
            self.assertEqual(c.corresponden('CGC'), 'GCG')
            self.assertEqual(c.corresponden(0), 0)

class TestEs_cadena_valida(TestCase):
        def test_es_cadena_valida(self):
            def assertIsTrue(self, value):
                self.assertIs('CTT', True)

            def assertIsFalse(self, value):
                self.assertIs('CAH', False)

class TestEs_base(TestCase):
        def testEs_base(self):
            self.assertEqual(c.es_base('T'), 'CGT')
            self.assertEqual(c.es_base(0), 0)

class TestEs_subcadena(TestCase):
        def testEs_subcadena(self):
            def assertIsTrue(self, value):
                self.assertIs('GGA', True)

            def assertIsFalse(self, value):
                self.assertIs('CAH', False)

class TestReparar_dano(TestCase):
        def testreparar_dano(self):
            self.assertEqual(c.reparar_dano('TSA'), 'C')
            self.assertEqual(c.reparar_dano(0), 0)

class TestObtener_secciones(TestCase):
    def test_obtener_secciones(self):
        self.fail()
class TestObtener_complementos(TestCase):
    def test_obtener_complementos(self):
        self.fail()

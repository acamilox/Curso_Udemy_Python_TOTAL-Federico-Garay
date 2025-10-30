import unittest
import cambia_texto

# Heredando todos los métodos de TestCase
class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'buen día'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DÍA')


if __name__ == '__main__':
    unittest.main()

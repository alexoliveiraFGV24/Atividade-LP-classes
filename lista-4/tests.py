import unittest
from classes_lojas import *
from classes_funcionarios import *
from classes_instrumentos import *

class TestesLojas(unittest.TestCase):
    def setUp(self):
        self.loja = Loja("Loja de Instrumentos", "Rua Principal", 100)

    def test_adicionar_funcionarios(self):
        funcionario = Funcionario("João", "12345678900", 2500.0, "Vendedor")
        self.loja.adicionar_funcionarios([funcionario])
        self.assertIn(funcionario, self.loja.funcionarios)

    def test_remover_funcionarios(self):
        funcionario = Funcionario("João", "12345678900", 2500.0, "Vendedor")
        self.loja.adicionar_funcionarios([funcionario])
        self.loja.remover_funcionarios([funcionario])
        self.assertNotIn(funcionario, self.loja.funcionarios)

    def test_adicionar_instrumentos(self):
        instrumento = Instrumento("Yamaha", "F310", 500.0, 6)
        self.loja.adicionar_instrumentos([instrumento])
        self.assertIn(instrumento, self.loja.instrumentos)

    def test_remover_instrumentos(self):
        instrumento = Instrumento("Yamaha", "F310", 500.0, 6)
        self.loja.adicionar_instrumentos([instrumento])
        self.loja.remover_instrumentos([instrumento])
        self.assertNotIn(instrumento, self.loja.instrumentos)


class TestesFuncionarios(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario("Ana", "98765432100", 3000.0, "Gerente")

    def test_trocar_de_cargo(self):
        self.funcionario.trocar_de_cargo("Diretor")
        self.assertEqual(self.funcionario.cargo, "Diretor")

    def test_trocar_de_salario(self):
        self.funcionario.trocar_de_salario(3500.0)
        self.assertEqual(self.funcionario.salario, 3500.0)


class TestesInstrumentos(unittest.TestCase):
    def setUp(self):
        self.violao = Violao("Yamaha", "C40", 450.0, 6)
        self.guitarra = Guitarra("Fender", "Stratocaster", 5000.0, 6)
        self.baixo = Baixo("Ibanez", "GSR200", 1000.0, 4)

    def test_violao_tocar_louvor(self):
        resultado = self.violao.tocar_louvor("Grandes Coisas", "Fernandinho")
        self.assertEqual(resultado, "Tocando o louvor 'Grandes Coisas' do artista 'Fernandinho' no violão.")

    def test_guitarra_tocar_solo(self):
        resultado = self.guitarra.tocar_solo("Purple Haze", "Jimi Hendrix")
        self.assertEqual(resultado, "Tocando um solo da música 'Purple Haze' do artista 'Jimi Hendrix' na guitarra.")

    def test_baixo_tocar_future_funk(self):
        resultado = self.baixo.tocar_future_funk("Plastic Love", "Mariya Takeuchi")
        self.assertEqual(resultado, "Tocando a música 'Plastic Love' do artista 'Mariya Takeuchi' no baixo, no estilo Future Funk.")

if __name__ == '__main__':
    unittest.main(verbosity=2)

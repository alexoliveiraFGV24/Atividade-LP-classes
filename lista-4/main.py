from classes_lojas import *
from classes_funcionarios import *
from classes_instrumentos import *

def main():
    loja_1 = Loja("Musica do Tokão", "Cruz Lima", 30, [], [])
    loja_2 = Loja("Música da Renner", "Senador Vergeuiro", 43, [], [])

    violao_1 = Violao("Yamaha", "Clássico", 499.90, 6)
    violao_2 = Violao("Eagle", "Silent", 849.90, 8)

    guitarra_1 = Guitarra("Gibraltar", "Les Paul", 1399.0, 8)
    guitarra_2 = Guitarra("Jupiter", "SG", 799.90, 6)

    baixo_1 = Baixo("Ibanez", "Baixolão", 599.90, 4)
    baixo_2 = Baixo("Gibson", "Elétrico", 799.90, 6)

    funcionario_1 = Funcionario("Alex", "12345678900", 3000.0, "Diretor")
    funcionario_2 = Funcionario("João", "12345678900", 5000.0, "Gerente")
    funcionario_3 = Funcionario("Thalis", "12345678900", 3600.0, "Consultor Sênior")
    funcionario_4 = Funcionario("Matheus", "12345678900", 2000.0, "Assistente de Caixa")

    loja_1.adicionar_instrumentos([violao_1, guitarra_1, baixo_1])
    loja_1.adicionar_funcionarios([funcionario_1, funcionario_2])
    print(loja_1.consultar_funcionarios())
    print(loja_1.consultar_instrumentos())

    loja_2.adicionar_instrumentos([violao_2, guitarra_2, baixo_2])
    loja_2.adicionar_funcionarios([funcionario_3, funcionario_4])
    print(loja_2.consultar_funcionarios())
    print(loja_2.consultar_instrumentos())

if __name__ == '__main__':
    main()
    
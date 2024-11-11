from classes_instrumentos import *
from classes_funcionarios import *

class Loja:
    def __init__(self, nome: str, rua: str, numero: int, funcionarios: list = None, instrumentos: list = None):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome da loja deve ser uma string não vazia.")
        
        if not isinstance(rua, str) or not rua.strip():
            raise ValueError("Nome da rua deve ser uma string não vazia.")
        
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Número do endereço deve ser um inteiro positivo.")

        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.funcionarios = funcionarios if funcionarios else []
        self.instrumentos = instrumentos if instrumentos else []

    def __str__(self):
        funcionarios_str = ", ".join(str(func) for func in self.funcionarios)
        instrumentos_str = ", ".join(str(instr) for instr in self.instrumentos)
        return (f"A {self.nome}, localizada na rua {self.rua}, {self.numero}, "
                f"possui os funcionários: [{funcionarios_str}] e os instrumentos: [{instrumentos_str}]")

    def __del__(self):
        print(f"{self.nome} deletada com sucesso")

    def adicionar_funcionarios(self, funcionarios: list[Funcionario]):
        for funcionario in funcionarios:
            if isinstance(funcionario, Funcionario):
                self.funcionarios.append(funcionario)
            else:
                print(f"{funcionario} não é um funcionário válido e não foi adicionado.")

    def remover_funcionarios(self, funcionarios: list[Funcionario]):
        for funcionario in funcionarios:
            try:
                self.funcionarios.remove(funcionario)
            except ValueError:
                print(f"Funcionário {funcionario} não encontrado na loja.")

    def adicionar_instrumentos(self, instrumentos: list[Instrumento]):
        for instrumento in instrumentos:
            if isinstance(instrumento, Instrumento):
                self.instrumentos.append(instrumento)
            else:
                print(f"{instrumento} não é um instrumento válido e não foi adicionado.")

    def remover_instrumentos(self, instrumentos: list[Instrumento]):
        for instrumento in instrumentos:
            try:
                self.instrumentos.remove(instrumento)
            except ValueError:
                print(f"Instrumento {instrumento} não encontrado na loja.")
    
    def consultar_funcionarios(self):
        quantidade = len(self.funcionarios)
        return quantidade, self.funcionarios

    def consultar_instrumentos(self):
        quantidade = len(self.instrumentos)
        return quantidade, self.instrumentos

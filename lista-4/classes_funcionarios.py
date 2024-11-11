class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float, cargo: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome deve ser uma string não vazia.")
        
        if not isinstance(cpf, str) or len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve ser uma string de 11 dígitos numéricos.")
        
        if not isinstance(salario, float) or salario < 0:
            raise ValueError("Salário deve ser um float positivo.")
        
        if not isinstance(cargo, str) or not cargo.strip():
            raise ValueError("Cargo deve ser uma string não vazia.")

        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    
    def __str__(self):
        return f"{self.nome}, de CPF {self.cpf}, que está no cargo de {self.cargo}, recebe um salário de R${self.salario}"
    
    def trocar_de_cargo(self, cargo):
        if not isinstance(cargo, str) or not cargo.strip():
            raise ValueError("Cargo deve ser uma string não vazia.")
        self.cargo = cargo
    
    def trocar_de_salario(self, salario):
        if not isinstance(salario, (int, float)) or salario < 0:
            raise ValueError("Salário deve ser um número positivo.")
        self.salario = salario

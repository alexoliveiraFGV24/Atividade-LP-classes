class Instrumento:
    def __init__(self, marca: str, modelo: str, preco: float, num_cordas: int):
        if not isinstance(marca, str) or not marca.strip():
            raise ValueError("Marca deve ser uma string não vazia.")
        
        if not isinstance(modelo, str) or not modelo.strip():
            raise ValueError("Modelo deve ser uma string não vazia.")
        
        if not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError("Preço deve ser um número positivo.")
        
        if not isinstance(num_cordas, int) or num_cordas <= 0:
            raise ValueError("Número de cordas deve ser um inteiro positivo.")

        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.num_cordas = num_cordas

    def __str__(self):
        return f"{self.marca} {self.modelo}, com {self.num_cordas} cordas, preço: R${self.preco}"


class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas):
        super().__init__(marca, modelo, preco, num_cordas)
    
    def tocar_louvor(self, musica, artista):
        if not musica or not artista:
            raise ValueError("Música e artista devem ser fornecidos e não podem estar vazios.")
        return f"Tocando o louvor '{musica}' do artista '{artista}' no violão."
    
    def rasqueado(self, tipo):
        if not tipo:
            raise ValueError("Tipo de rasqueado deve ser fornecido e não pode estar vazio.")
        return f"Executando um rasqueado do tipo '{tipo}'."


class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas):
        super().__init__(marca, modelo, preco, num_cordas)
    
    def tocar_solo(self, musica, artista):
        if not musica or not artista:
            raise ValueError("Música e artista devem ser fornecidos e não podem estar vazios.")
        return f"Tocando um solo da música '{musica}' do artista '{artista}' na guitarra."
    
    def vibrato(self, oscilacoes):
        if not isinstance(oscilacoes, int) or oscilacoes <= 0:
            raise ValueError("Número de oscilações para o vibrato deve ser um inteiro positivo.")
        return f"Executando vibrato com {oscilacoes} oscilações."


class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas):
        super().__init__(marca, modelo, preco, num_cordas)
    
    def tocar_future_funk(self, musica, artista):
        if not musica or not artista:
            raise ValueError("Música e artista devem ser fornecidos e não podem estar vazios.")
        return f"Tocando a música '{musica}' do artista '{artista}' no baixo, no estilo Future Funk."
    
    def pizzicato(self, andamento):
        if not andamento:
            raise ValueError("Andamento para o pizzicato deve ser fornecido e não pode estar vazio.")
        return f"Executando pizzicato com andamento '{andamento}'."

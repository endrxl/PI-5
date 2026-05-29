class Pessoa:
    pessoas = []
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    @classmethod
    def listarPessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa)

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('Roberto', 30, 'Construtor')

print(pessoa1)

pessoa1.aniversario()

print(pessoa1)

qtd_pessoas = len(Pessoa.pessoas)

print(f'A quantidade de pessoas é {qtd_pessoas}')
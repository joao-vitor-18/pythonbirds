class Pessoa:
    def __init__(self, nome=None, idade=28):
        self.idade=idade
        self.nome=nome

    def cumprimentar(self):
        return f'Olá {id(p)}'

if __name__=='__main__':
    p = Pessoa('Pedro')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'João'
    print(p.nome)
    print(p.idade)

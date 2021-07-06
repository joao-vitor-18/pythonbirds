class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade=idade
        self.nome=nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
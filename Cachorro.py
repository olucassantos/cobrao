class Cachorro:

    nome = ''
    raca = ''

    def _init_(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print('Au ' + self.raca)
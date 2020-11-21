PARTES_BONECO = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class Jogo:
    def __init__(self, palavra):
        self.palavra = palavra
        self.tela = []
        self.num_erros = 0
        self.letrasUsadas = []

    def gerarPainel(self):
        for _ in self.palavra:
            self.tela.append('_')

    def imprimirPainel(self):
        for letra in self.tela:
            print(letra, end=' ')

    def verificarLetra(self, letra):
        # trocar traço pela letra, se ela existir na palavra
        for i, l in enumerate(self.palavra):
            if l == letra:
                self.tela[i] = letra
        # se a letra não estiver na palavra incrementa o erro
        if letra not in self.palavra:
            self.num_erros += 1
        # registra o uso de uma letra
        self.letrasUsadas.append(letra)

    def revelarPalavra(self):
        for i, letra in enumerate(self.palavra):
            self.tela[i] = letra

    def verificarGanhou(self):
        if '_' in self.tela:
            return False
        else:
            return True

    def imprimirForca(self):
        print(PARTES_BONECO[self.num_erros])

    def verificarPerdeu(self):
        if self.num_erros == 6:
            return True
        else:
            return False     



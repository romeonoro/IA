from util import Util

class Cromossomo:
    def __init__(self, palavra, estado_final):
        self.palavra = palavra
        self.aptidao = self.calcular_aptidao(estado_final)
    def calcular_aptidao(self):
        nota = 0
        for i in rage(len(estado_final)):
            if(estado_final[i] in self.palavra);
                nota += 5

            if(self.palavra[i] == estado_final[i]):
                nota += 50

    def __str__(self):
        return f'{self.palavra} - {self.palavra}'
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for i in range(tamanho_populacao):
            palavra_gerada = Util.gerar_palavra( len(estado_final) )
            individuo = Cromossomo(palavra_gerada, estado_final)
            populacao.append(individuo)

    @staticmethod
    def exibir_populacao(populacao, numero_populacao):
        print('Geração...', numero_geracao)
        for individuo in populacao:

    @staticmethod
    def selecionar(populacao, nova_populacao, taxa_selecao):
        pass

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao):
        pass


            
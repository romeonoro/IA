import random

class Util:
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    tamanho = len(letras)
    
    @staticmethod
    def gerar_palavra(tamanho_palavra):
        palavra = ''
        
        for _ in range(tamanho_palavra):
            posicao_sorteada = random.randrange(Util.tamanho)
            palavra += Util.letras[posicao_sorteada]
        
        return palavra

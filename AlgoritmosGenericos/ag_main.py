"""
estado final = amor - inteligencia (problema acadêmico, problema real nõ se sabe o estado final(se aplica lista de restrições))

população - lista de cromossomos | individuos | estados | objetos
nova população - próximas gerações
tamanho da população - inteiro
taxa de seleção - roleta, torneio, estocástico
taxa de reprodução
taxa de mutação 

classe cromossomo
    #função aptidao - definição da heuristica: tem alguma letra do estado final? Sim, 5 pts. Se a letra está o lugar, 50 pts.

[gfds(0), asdf(55), ghjk(0), lmnb(55), vcxz(0), poiu(5), awer(60), wdcv(5), tyui(5), bvjk(5)]

main
    - estado_final
    - tamanho_populacao
    - quantidade_geracoes
    - taxa_selecao - 20 a 40% (nao cria novos individuos)
    - taxa_reproducao = 100 - taxa_selecao
    - taxa_mutacao

    - gerar_populacao(populacao, tamanho_populacao, estado_final) -> aplicar a aptidao
    - ordenar (populacao)    

        - repetição 1 até quantidade de gerações:
        selecionar(populacao, nova_populacao, taxa_selecao)
        reproduzir(populacao, nova_populacao, taxa_reproducao) -> aplicar a aptidao
        verificar se é hora da mutação
            mutar -> aplicar a aptidao
        mover nova_populacao para populacao
        apagar nova_populacao
        order(populacao)
""" 
from cromossomo import Cromossomo

estado_final = input('Entre com a palavra do estado final: ')
tamanho_populacao = int(input('Tamanho da população: '))
quantidade_geracoes = int(input('Gerações: '))
taxa_selecao = int(input('Taxa de seleção [25 a 25]: '))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input('Taxa de mutação: '))

populacao = list()
nova_populacao = list()

Cromossomo.gerar_populacao(populacao, tamanho_populacao, estado_final)
populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
Cromossomo.exibir_populacao(populacao, 0)

for i in range(1, quantidade_geracoes):
    Cromossomo.selecionar(populacao, nova_populacao, taxa_selecao)
    Cromossomo.reproduzir(populacao, nova_populacao, taxa_reproducao)

    if i % taxa_mutacao == 0:
        Cromossomo.mutar(nova_populacao)
    
    populacao.clear
    populacao.append(nova_populacao)
    nova_populacao.clear
    populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
    Cromossomo.exibir_populacao(populacao, i)
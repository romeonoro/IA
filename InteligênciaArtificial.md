# Importante Saber

### Força Bruta

- Necessita de RAM e processador
- **Profundidade:** Estoura a memória rapidamente, necessita de bastante hardware.
- **Amplitude:** Não estoura a memória rapidamente, usa mais largura.
- **Características da força bruta:**
  - Hardware poderoso/sobrando (memória RAM e processador)
  - Uso de dicas ou informações privilegiadas (heurísticas)
  - Pouca restrição
  - **Custo:**
    - Custo Fixo 1 (Puzzle)
    - Custo Variável (Xadrez)

## Identar

### Técnicas para construção de Sistemas de Comportamento Inteligente

  - **Base de conhecimento:** Fatos ou experiências
  - **Raciocínio automatizado:** Dedução e indução
  - **Aprendizagem de máquina:** Treinamento ou repetição de amostras - reconhecimento

- **Resolução de problemas:**
  - (A) Problemas em que se quer os passos até um estado final (conhecido ou não)
  - (B) Diagnóstico - Reconhecimento de padrões

### Exemplos:

1) Qual o melhor caminho de um pacote de uma rede de dados cabeada com fibra óptica? - **(A)**
2) Saindo da pizzaria e entregando N pizzas em um tempo mínimo? - **(A)**
3) Um programa de computador que jogue damas contra um ser humano? - **(A)**
4) Uma função que carregue foto, obrigatoriamente, de somente um rosto de uma pessoa? - **(B)**
   - **Desafios:**
     1) Fazer a máquina reconhecer pessoas
        - Treinamento:
          - Imagens positivas: imagens de pessoas
          - Imagens negativas: imagens sem pessoas
          - Imagens sobrepostas
     2) Fazer a máquina reconhecer somente um rosto
        - Treinamento:
          - Imagens positivas: imagens de somente um rosto
          - Imagens negativas: imagens sem pessoas
          - Imagens sobrepostas

5) A partir da foto de uma folha de planta, informar se a planta está ou não doente? - **(B)**
   - **Desafios:**
     - Juntar imagens de N tipos de plantas
     - Para cada tipo de planta, trazer imagens de doentes e não doentes

## Resolução de Problemas por Métodos de Busca

- **Técnica de IA para encontrar um conjunto de passos até um estado final (conhecido ou não)**
  - **Modelagem:** Estados, regras de transição, restrições, lista de visitados, função meta
  - **Estratégias para escolher as regras de transição:**
    - **Métodos de busca:**
      - **Cegos ou de força bruta:**
        - Aplicado quando:
          - Não se tem informação privilegiada (heurística)
          - Hardware poderoso está disponível
          - Pouca restrição
        - **Largura ou amplitude:** Uso de fila
        - **Profundidade:** Uso de pilha (recursiva)
      - **Informados ou heurísticos:**
        - **O que é heurística?** Informação privilegiada para aplicar uma regra de transição
        - **Quando aplicar?**
          - Quando se tem dica ou heurística
          - Quando se tem pouco hardware
          - Quando se tem muitas restrições
        - **Principais métodos heurísticos:**
          - **Subida de Encosta (Climb Hill):**
            - Profundidade
            - Custo real - g(n)
          - **Guloso:**
            - Amplitude
            - Custo estimado - h(n)
          - **A***:
            - Amplitude
            - Mistura custo real com custo estimado (correção)

## Problemas Clássicos em IA

- O Problema das *N-Rainhas*
- O Problema das *Jarras*
- O Problema da *Torre de Hanói*
- O Problema do *Puzzle*

## Observação Importante

**Toda vez que um estado/objeto é gerado, é preciso fazer 3 testes:**
1) É válido?
2) Já foi visitado?
3) É a meta?

---
1) Que tipo de problema a IA resolve?
    - Problemas que é necessário a presença de um especialista, muitas vezes por causa da quantidade de restrições
    - Problemas em que não se sabe o estado final e problemas em que se precisa saber o passo-a-passo (como fazer) da solução

2) O que é Inteligência Artificial?
    - Área da Computação com metodologias, técnicas e algoritmos para resolver aqueles tipos de problemas    

3) Principais subáreas da Inteligência Artificial?
    - Métodos de busca: 
        - cegos ou força bruta: amplitude e profundidade
        - heurísticos: Guloso, Subida de Encosta, A*, Algoritmos Genéticos

    - Redes Neurais
    - Sistemas Multiagentes
    - Representação de Conhecimento
    - Processamento da Língua Natural (PLN)

4) O que é um sistema de comportamento inteligente?
    - Um sistema composto por base de conhecimento (fatos e regas, ou crenças e plano), Raciocínio Automatizado (dedução e indução) e Aprendizado de Máquina (treinamento por repetição ou amostras)

5) Que tipo de problema RNA resolve?
    - Problemas de reconhecimento de padrões ou em que a presença do especialista é fundamental

6) Quais as características que um problema apresenta quando ele tem alta complexidade?
    - restrições
    - desconhecimento do estado final

7) No processo de modelagem da solução de problemas na área de IA, o que se deve modelar?
    - Estados: inicial(ais) e final(ais) -> é uma possível solução, é um instante do processo de solução
        - atributos
    - Regras de transição
        - métodos
    - Restrições
    - Lista de visitados
    - Função meta ou objetivo
---

# Inteligência Artificial
## Técnicas de resolução de problema:
### Que tipo de problemas?
- (A) Diagnóstico ou reconhecimento de padrões
  - tomada de decisões
    - área médica
  - processamento de imagens
- (B) Definição de passos até o estado final (empacotamento)
  - área de jogos
  - linha de montagem

### Sistemas de Comportamento Inteligente
- **Base de conhecimento** (gigantesca)
  - fatos
- **Raciocínio automatizado** (dedução e indução)
- **Aprendizagem** -> reconhecimento de padrões por treino

## Áreas
### (B) Métodos de busca (solução de problemas)
- profundidade, amplitude, subida de encosta, gulosa, A*
- algoritmos genéticos
### (A) (B) Representação de conhecimento
- prolog
- ontologia
- (B) sistemas multiagentes
- (A) redes neurais
- (A) processamento da língua natural - PLN

# Problemas:
  1) resolver o jogo da velha - B
  2) resolver um problema de mal funcionamento de um computador - A
  3) resolver o problema do puzzle - B
  4) fazer a entrega de n pizzas por um motoboy em um tempo mínimo - B
  5) montar a grade de horários em um curso de graduação - B
  6) identificar os instrumentos musicais em uma música - A

## Modelar a solução com alguma técnica de IA
  1) mapear os estados possíveis do problema
     - definir classe e seus atributos
     - definir o estado inicial e o estado(s) final(is)
  2) mapear os métodos das classes - Regras de Transição
  3) mapear as restrições - método ehValido()
  4) forma de mapear os visitados - hashSet ou uma árvore
       - gerar uma string dos atributos daquele estado/objeto
  5) definir o método meta ou objetivo
     
### Observação:
  - toda vez que um estado/objeto é gerado é preciso fazer 3 testes:
      1) é válido?
      2) já visitei?
      3) é a meta?

# O Problema das N-Rainhas
# O Problema das Jarras
# O Prbolema da Torre de Hanói
# Problema do Puzzle

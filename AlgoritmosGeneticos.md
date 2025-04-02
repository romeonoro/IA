Os **algoritmos genéticos (AGs)** são uma técnica de otimização e busca inspirada no processo de seleção natural da evolução biológica. Eles são usados para encontrar soluções aproximadas para problemas complexos onde métodos exatos seriam inviáveis devido ao alto custo computacional.

## 🔬 **Como funcionam?**
Os algoritmos genéticos trabalham com uma população de possíveis soluções (indivíduos), que evoluem ao longo de várias gerações por meio dos seguintes operadores:

1. **Codificação**: Representação das soluções como cromossomos (normalmente strings binárias, mas podem ser outras estruturas).
2. **Avaliação (Fitness)**: Mede o quão boa é cada solução segundo uma função de aptidão.
3. **Seleção**: Escolhe os indivíduos mais aptos para reprodução (ex.: roleta, torneio, seleção elitista).
4. **Cruzamento (Crossover)**: Combina partes de dois indivíduos para gerar novos filhos.
5. **Mutação**: Faz pequenas alterações aleatórias nos filhos para manter diversidade e evitar mínimos locais.
6. **Substituição**: Os novos indivíduos substituem os antigos e o processo se repete até um critério de parada ser atingido.

## 🏆 **Aplicações**
- Otimização de funções matemáticas
- Machine Learning (treinamento de redes neurais)
- Jogos (IA adversarial)
- Roteamento e logística (ex.: problema do caixeiro-viajante)
- Engenharia (design de circuitos, planejamento estrutural)

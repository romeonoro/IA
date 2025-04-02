# Algoritmo Genético

## Definições

- **Estado final** = amor - inteligência (problema acadêmico). 
  - Para um problema real, não se sabe o estado final (aplica-se uma lista de restrições).

- **População** = lista de cromossomos | indivíduos | estados | objetos.
- **Nova população** = próximas gerações.
- **Tamanho da população** = inteiro.
- **Taxa de seleção** = roleta, torneio, estocástico.
- **Taxa de reprodução**.
- **Taxa de mutação**.

## Classe Cromossomo

### Função de Aptidão
- Definição da heurística:
  - Se tem alguma letra do estado final: **+5 pontos**.
  - Se a letra está no lugar correto: **+50 pontos**.

### Exemplo de População Inicial:
```text
[gfds(0), asdf(55), ghjk(0), lmnb(55), vcxz(0), poiu(5), awer(60), wdcv(5), tyui(5), bvjk(5)]
```

## Fluxo Principal (Main)

### Parâmetros
- `estado_final`
- `tamanho_populacao`
- `quantidade_geracoes`
- `taxa_selecao` = 20 a 40% (não cria novos indivíduos)
- `taxa_reproducao` = 100 - `taxa_selecao`
- `taxa_mutacao`

### Passos do Algoritmo
1. **Gerar população inicial**: `gerar_populacao(populacao, tamanho_populacao, estado_final)`
   - Aplicar a função de aptidão.
2. **Ordenar população**: `ordenar(populacao)`
3. **Evolução**: Para `1` até `quantidade_geracoes`:
   - `selecionar(populacao, nova_populacao, taxa_selecao)`
   - `reproduzir(populacao, nova_populacao, taxa_reproducao)`
     - Aplicar a função de aptidão.
   - **Verificar se é hora da mutação**:
     - `mutar(nova_populacao) `
     - Aplicar a função de aptidão.
   - **Atualizar população**:
     - Mover `nova_populacao` para `populacao`.
     - Apagar `nova_populacao`.
     - Ordenar `populacao`.

---

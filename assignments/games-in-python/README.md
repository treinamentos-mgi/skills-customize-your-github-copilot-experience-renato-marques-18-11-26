
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo da Forca em Python no qual o jogador adivinha uma palavra oculta antes de esgotar as tentativas. Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória.

## 📝 Tarefas

### 🛠️ Implementar os palpites e o progresso da palavra

#### Descrição
Crie a lógica principal do jogo: selecione uma palavra de uma lista predefinida e permita que o jogador tente descobri-la digitando letras.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista com pelo menos cinco palavras.
- Exibir cada letra ainda não descoberta como `_` e revelar as letras acertadas nas posições correspondentes.
- Solicitar e processar um palpite de letra por vez.
- Atualizar e exibir o progresso da palavra após cada palpite.

### 🛠️ Controlar tentativas e encerrar a partida

#### Descrição
Complete o fluxo da partida contabilizando palpites incorretos e informando ao jogador o resultado.

#### Requisitos
O programa concluído deve:

- Começar com seis tentativas incorretas disponíveis e diminuir esse total somente quando o palpite não estiver na palavra.
- Exibir quantas tentativas incorretas ainda restam após um erro.
- Encerrar a partida quando todas as letras forem descobertas ou quando não restarem tentativas.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra escolhida.
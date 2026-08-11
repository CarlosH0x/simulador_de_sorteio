# ⚽ Simulador de Sorteio das Quartas de Final da Copa do Brasil 2026

Criei um programa simples desenvolvido em **Python** para simular o sorteio dos confrontos das quartas de final da Copa do Brasil.

O projeto utiliza uma lista com 8 equipes, embaralha os times aleatoriamente e forma 4 confrontos, exibindo os jogos de ida e volta.

> 📚 Projeto desenvolvido como parte dos meus estudos dos fundamentos da linguagem Python.

---

## 🎯 Objetivo

O objetivo deste projeto foi praticar conceitos fundamentais de Python através da criação de um programa simples e funcional.

Onde aproveitei a ideia do sorteio da Copa do Brasil.

Entre os principais conceitos utilizados estão:

- Variáveis
- Listas
- Índices
- Estruturas de repetição
- Funções
- Módulos
- Geração de valores aleatórios
- Manipulação de strings
- F-strings
- Controle de tempo de execução

---

## ⚙️ Como funciona

O programa utiliza uma lista contendo 8 equipes classificadas:

```python
times = [
    "Atlético Mineiro",
    "Cruzeiro",
    "Grêmio",
    "Internacional",
    "Palmeiras",
    "Santos",
    "Vasco",
    "Vitória",
]
```

Em seguida, a função random.shuffle() embaralha os elementos da lista.
```python
random.shuffle(times)
```
Depois disso, o programa percorre a lista de dois em dois elementos, formando os quatro confrontos. E como a lista é embaralhada aleatoriamente, os confrontos podem ser diferentes a cada execução.

---

## 🧠 Principais recursos utilizados

**import random**

O módulo random fornece funções para trabalhar com valores e operações aleatórias. Neste projeto, ele é utilizado para embaralhar a lista das equipes.

**import time**

O módulo time permite trabalhar com funções relacionadas ao tempo. Neste projeto ele é utilizado para criar uma pequena pausa entre os sorteios:
```python
  time.sleep(1)
```

**Loop `for` com `range(0, len(lista), 2)`**

Percorre a lista de times de **2 em 2**, formando os pares de confronto. 

Por fim, os confrontos são exibidos na tela utilizando o `print` com `f-strings`, mostrando os jogos de ida e volta.

---
## 💻 Código

O código completo do simulador está disponível aqui:

👉 [sorteio_copa.py](sorteio_copa.py)

---
## 📌 Sobre o projeto

Aproveitei a ideia do sorteio da Copa do Brasil e busquei unir o que eu já sei em Python e criar um programa funcional relacionado a isso.

Ele ainda é um programa simples, mas ele cumpre o seu papel de simular o sorteio das equipes.

Aos poucos vou ir melhorando esse código para que fique mais organizado e profissional, a medida que eu for evoluindo em Python

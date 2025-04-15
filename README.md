# Load Balancer Simulator

Este projeto simula a alocação de usuários em servidores com base em uma lista de carga por "ticks" (unidades de tempo). A ideia é ilustrar como um balanceador de carga pode distribuir usuários entre servidores considerando limitações de tempo de atendimento (`ttask`) e capacidade máxima por servidor (`umax`).

## 📁 Estrutura do Projeto

```
load_balancer/
├── input.txt         # Arquivo de entrada com os parâmetros e dados de simulação
├── load_balancer.py  # Script principal que executa a lógica da simulação
├── LICENSE           # Licença do projeto
├── README.md         # Este arquivo
└── .gitignore        # Arquivos e pastas ignorados pelo Git
```

## ⚙️ Como Funciona

1. **Entrada** (`input.txt`):
   - Primeira linha: `ttask` → tempo (em ticks) que um usuário permanece em um servidor.
   - Segunda linha: `umax` → número máximo de usuários que um servidor pode atender simultaneamente.
   - A partir da terceira linha: número de novos usuários chegando a cada tick.

2. **Processamento**:
   - Usuários são alocados nos servidores existentes se houver capacidade.
   - Se todos os servidores estiverem cheios, um novo servidor é criado.
   - A cada tick, o tempo restante de cada usuário nos servidores é decrementado.
   - Servidores sem usuários são removidos.

3. **Saída** (`output.txt`):
   - Cada linha mostra o número de usuários ativos em cada servidor no respectivo tick.
   - A última linha mostra o custo total (quantidade total de servidores ativos ao longo da simulação).

## ▶️ Como Executar

Certifique-se de ter o Python 3 instalado.

```bash
python load_balancer/load_balancer.py
```

## 📥 Exemplo de input.txt
```
4
2
1
3
0
1
0
1
```

## 🧠 Interpretação:
- ttask = 4: cada usuário permanece por 4 ticks.
- umax = 2: cada servidor pode atender até 2 usuários.

- Chegada de usuários por tick:
   - Tick 0: 1 usuário
   - Tick 1: 3 usuários
   - Tick 2: 0 usuários
   - Tick 3: 1 usuário
   - Tick 4: 0 usuários
   - Tick 5: 1 usuário

## 📤 Exemplo de output.txt

```
1
2,1
1
1
0
1
7
```

- As primeiras linhas representam os estados dos servidores em cada tick.

- A última linha (7) representa o custo total (número total de servidores ativos somados por tick).

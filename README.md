
# 🐍 Snake Game

Este é um simples jogo da cobra desenvolvido em Python 3.12.2 utilizando `Tkinter` para a interface gráfica e `Pillow` para manipulação de imagens. O objetivo é controlar a cobra com as setas do teclado, comer a maçã e evitar colidir com as bordas ou consigo mesma.

## 📋 Requisitos

- Python 3.12.2 ou superior
- `Pillow`: Biblioteca para manipulação de imagens.
- `ruff`: Ferramenta de lint para verificar e padronizar o estilo de código.

## 🚀 Como executar

### 1. Instale as dependências

Execute o comando abaixo para instalar todas as dependências:
```bash
make install
```

### 2. Execute o jogo
Use o comando abaixo para iniciar o jogo:
```bash
make run
```

## 🛠️ Comandos disponíveis
Este projeto utiliza um `Makefile` para simplificar as tarefas comuns. Os seguintes comandos estão disponíveis:

- **Checar e corrigir estilo de código com `ruff`:**
  ```bash
  make style
  ```

- **Instalar dependências:**
  ```bash
  make install
  ```
  E configurar o `PYTHON_CONFIGURE_OPTS` para instalar o Python 3.12.2 com o `tcl-tk`:
  ```bash
  PYTHON_CONFIGURE_OPTS="--with-tcl-tk=<local de instalação do tcl-tk>" pyenv install 3.12.2
  
  Ex.: PYTHON_CONFIGURE_OPTS="--with-tcl-tk=/opt/homebrew/Cellar/tcl-tk" pyenv install 3.12.2
  ```


- **Executar o jogo:**
  ```bash
  make run
  ```

## 🎮 Como jogar
- **Setas do teclado:** Controlam a direção da cobra.
- **Objetivo:** Comer a maçã para crescer e aumentar sua pontuação.
- **Game Over:** O jogo termina se a cobra colidir com as bordas ou consigo mesma.

## 📂 Estrutura do Projeto
```
.
├── Makefile
├── README.md
├── requirements.txt
├── snake.py
├── dot.png
└── head.png
```

## 📝 Licença
Este projeto é apenas um exemplo educativo e não possui uma licença específica.

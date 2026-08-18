# Fundamentos de Inteligência Artificial — 2026.2 · Turma A

Laboratórios da disciplina. **ILES/ULBRA Itumbiara** · Sistemas de Informação e Engenharia
de Software · Prof. Leonardo Garcia Marques.

---

## Como começar

Você precisa de **duas** ferramentas instaladas na máquina: o `git` e o `uv`. Se ainda não
as tem, siga o roteiro entregue em aula antes de continuar.

```bash
git clone <endereço-deste-repositório>
cd fundamentos-ia-2026-2-a
uv sync
```

O `uv sync` lê o `pyproject.toml` e o `uv.lock`, baixa a versão certa do Python, cria o
ambiente virtual em `.venv/` e instala as bibliotecas. **Na primeira vez demora** — são
algumas centenas de megabytes.

Depois, confira se deu tudo certo:

```bash
uv run verifica_ambiente.py
```

Se ele imprimir as versões e salvar o `teste-ambiente.png`, você está pronto.

---

## Rodando os laboratórios

```bash
uv run jupyter lab
```

O navegador abre; entre em `notebooks/` e escolha o laboratório.

> 💡 Se preferir o **VS Code**, abra a pasta com `code .`, instale as extensões *Python* e
> *Jupyter* e, ao abrir um `.ipynb`, clique em **Select Kernel** e escolha o interpretador
> que está dentro de `.venv`. Escolher outro é a causa nº 1 de `ModuleNotFoundError` com a
> biblioteca instalada.

---

## O que tem aqui

```
fundamentos-ia-2026-2-a/
├── README.md                  este arquivo
├── pyproject.toml             o que o projeto precisa
├── uv.lock                    as versões exatas que todos vamos usar
├── .python-version            a versão do Python do projeto
├── verifica_ambiente.py       teste rápido de que está tudo funcionando
└── notebooks/
    ├── lab01/                 Python para quem já programa
    ├── lab02/                 Busca não informada — BFS e DFS
    └── lab03/                 Busca informada — heurísticas e A*
```

### Índice dos laboratórios

| Lab | Aula | Tema | Bibliotecas |
|-----|------|------|-------------|
| **01** | — | Python para quem já programa: do C/Java ao Python | só a biblioteca padrão |
| **02** | 11/08 | Busca não informada: BFS e DFS em um labirinto | só a biblioteca padrão |
| **03** | 18/08 | Busca informada: custo uniforme, gulosa e A\* | só a biblioteca padrão |

> O **lab01** é a base para os demais. Se você programa em C, Java ou pseudocódigo mas
> nunca escreveu Python, comece por ele — ele termina com você implementando, sem saber,
> o algoritmo do lab02.

Os notebooks vêm com lacunas marcadas `TODO`. Os **gabaritos são publicados no AVA** depois
da aula — não ficam neste repositório.

> Os laboratórios 02 e 03 usam apenas `collections` e `heapq`, que já vêm com o Python.
> Rodam em qualquer lugar, inclusive no Google Colab. As bibliotecas de ciência de dados
> entram a partir da aula de **15/09**.

---

## Os três arquivos que sustentam o ambiente

Vale entender a diferença, porque ela é conteúdo da disciplina:

| Arquivo | O que diz | Vai para o repositório? |
|---|---|---|
| `pyproject.toml` | **o que** o projeto precisa — "preciso do pandas" | ✅ sim |
| `uv.lock` | **qual versão exata** foi instalada, com hash | ✅ sim |
| `.venv/` | o ambiente **já montado**, específico da sua máquina | ❌ não |

É por isso que o `.venv/` está no `.gitignore`: ele é grande, é descartável e o `uv sync`
o reconstrói idêntico a partir dos outros dois. **O que se versiona é a receita, não o
bolo.**

---

## Comandos do dia a dia

| Comando | O que faz |
|---|---|
| `uv sync` | reconstrói o ambiente a partir do `pyproject.toml` + `uv.lock` |
| `uv add <pacote>` | acrescenta uma dependência |
| `uv run <arquivo.py>` | executa dentro do ambiente do projeto |
| `uv run jupyter lab` | abre o Jupyter no ambiente do projeto |
| `git pull` | traz as atualizações que eu publicar |

> 📌 **Antes de cada aula, rode `git pull`.** Os laboratórios novos chegam por aqui.
> Se eu tiver acrescentado alguma biblioteca, rode `uv sync` em seguida.

---

## Se algo travar

| Sintoma | O que fazer |
|---|---|
| `'uv'` não é reconhecido | Feche e reabra o terminal. Se persistir, reinstale — não entrou no `PATH`. |
| `uv sync` muito lento ou interrompido | Normal na primeira vez. Se cair, rode de novo: o download é retomado. |
| `ModuleNotFoundError` com a biblioteca instalada | Kernel errado no notebook. Selecione o que está em `.venv`. |
| O notebook dá erro estranho depois de várias edições | *Kernel → Restart e Run All*. Se o erro sumir, era estado velho. |
| Conflito no `git pull` porque você editou o notebook | Renomeie a sua cópia (ex.: `lab03-meu.ipynb`) antes de puxar. |

**Não fique travado em silêncio.** Use o canal da turma — provavelmente mais alguém está no
mesmo ponto.

---

## Bibliografia

1. RUSSELL, Stuart; NORVIG, Peter. *Inteligência artificial: uma abordagem moderna*.
   4. ed. Rio de Janeiro: LTC, 2022.
2. GÉRON, Aurélien. *Mãos à obra: aprendizado de máquina com Scikit-Learn, Keras &
   TensorFlow*. 3. ed. Rio de Janeiro: Alta Books, 2023.
3. SILVA, Ivan Nunes da; SPATTI, Danilo Hernane; FLAUZINO, Rogério Andrade. *Redes neurais
   artificiais para engenharia e ciências aplicadas*. 2. ed. São Paulo: Artliber, 2016.

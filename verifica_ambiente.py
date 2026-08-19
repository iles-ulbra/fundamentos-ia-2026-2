"""
Verificação do ambiente da disciplina.

    uv run verifica_ambiente.py

Imprime as versões instaladas e desenha um gráfico simples. Se este script
rodar até o fim sem erro, o ambiente está pronto para os laboratórios.
"""

import sys


def main() -> None:
    print("=" * 52)
    print("  Fundamentos de IA — 2026.2")
    print("  Verificação do ambiente")
    print("=" * 52)
    print(f"  Python      {sys.version.split()[0]}")

    faltando = []
    for rotulo, modulo in [
        ("NumPy      ", "numpy"),
        ("pandas     ", "pandas"),
        ("matplotlib ", "matplotlib"),
        ("scikit-learn", "sklearn"),
    ]:
        try:
            mod = __import__(modulo)
            print(f"  {rotulo} {mod.__version__}")
        except ImportError:
            print(f"  {rotulo} AUSENTE")
            faltando.append(modulo)

    # A biblioteca padrão basta para os laboratórios 02 e 03.
    from collections import deque
    import heapq

    fila = deque([3, 1, 2])
    fila.appendleft(0)
    monte = [3, 1, 2]
    heapq.heapify(monte)
    print(f"  collections.deque  ok  -> {list(fila)}")
    print(f"  heapq              ok  -> menor = {heapq.heappop(monte)}")

    print("-" * 52)
    if faltando:
        print("  ATENÇÃO: faltam pacotes.  Rode:  uv sync")
        print("  Ausentes:", ", ".join(faltando))
        sys.exit(1)

    print("  Tudo certo. Gerando o gráfico de teste...")
    import matplotlib

    matplotlib.use("Agg")  # não exige janela; salva em arquivo
    import matplotlib.pyplot as plt

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], marker="o")
    plt.title("Ambiente funcionando")
    plt.xlabel("x")
    plt.ylabel("x²")
    plt.savefig("teste-ambiente.png", dpi=100, bbox_inches="tight")
    print("  Gráfico salvo em  teste-ambiente.png")
    print("=" * 52)


if __name__ == "__main__":
    main()

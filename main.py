"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = float(input("Digite o primeiro lado:"))
    b = float(input("Digite o segundo lado:"))
    c = float(input("Digite o terceiro lado:"))
    tipo = str("null")

    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
      validade = 0
    else:
      validade = 1

    if validade == 0:
      print("Os valores informados não formam um triângulo.")
    else:
      if a==b and b==c:
        tipo = str("equilátero")
      elif a==b or b==c or a==c:
        tipo = str("isósceles")
      else:
        tipo = str("escaleno")
      print(f"O triângulo é {tipo}.")             

if __name__ == '__main__':
    main()

def vogal(letra):
    # Verifica se é vogal
    print(
        letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or
        letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'
    )

def consoante(letra):
    # Verifica se é consoante (todas as letras do alfabeto menos as vogais)
    print(
        letra == 'b' or letra == 'c' or letra == 'd' or letra == 'f' or letra == 'g' or
        letra == 'h' or letra == 'j' or letra == 'k' or letra == 'l' or letra == 'm' or
        letra == 'n' or letra == 'p' or letra == 'q' or letra == 'r' or letra == 's' or
        letra == 't' or letra == 'v' or letra == 'w' or letra == 'x' or letra == 'y' or letra == 'z' or
        letra == 'B' or letra == 'C' or letra == 'D' or letra == 'F' or letra == 'G' or
        letra == 'H' or letra == 'J' or letra == 'K' or letra == 'L' or letra == 'M' or
        letra == 'N' or letra == 'P' or letra == 'Q' or letra == 'R' or letra == 'S' or
        letra == 'T' or letra == 'V' or letra == 'W' or letra == 'X' or letra == 'Y' or letra == 'Z'
    )


def main():
    # Entrada de dado e verifica o primeiro caractere
    letra = input("Digite uma letra: ")[0]
    vogal(letra)
    consoante(letra)


if __name__ == "__main__":
    main().

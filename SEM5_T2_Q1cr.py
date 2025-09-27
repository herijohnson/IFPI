def vogal(letra):
    # Verifica se é uma vogal ou consoante maíuscula ou mínuscula
    print(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U')


def main():
# Entrada de dado e verifica o primeiro caractere
    letra = input("Digite uma letra: ")[0]
    vogal(letra)
if __name__ == "__main__":
   main()
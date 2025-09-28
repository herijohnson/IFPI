def consoante_e_vogal(letra):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    # O operador "in" verifica se a letra está dentro da string (vogais ou consoantes).
    # O operador "or" retorna True se pelo menos uma das condições for verdadeira.
    # Assim, o print mostra True se a letra for vogal OU consoante, e False caso contrário.
    print(letra in vogais or letra in consoantes)

def main():
    letra = input().strip()[0]  # pega o primeiro caractere da entrada
    consoante_e_vogal(letra)

if __name__ == "__main__":
    main()
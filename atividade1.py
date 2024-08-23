import math


def coletar_dados():
    """Coleta os dados de altura e gênero de 15 pessoas."""
    alturas = []
    generos = []
    for i in range(15):

        while True:
            try:
                altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
                alturas.append(altura)
                break
            except ValueError:
                print("Altura inválido. Digite uma altura válida.")
        genero = input(f"Digite o gênero da pessoa {i+1} (M/F): ").upper()
        while genero not in ['M', 'F']:
            genero = input("Gênero inválido. Digi  te M para Masculino ou F para Feminino: ").upper()

        generos.append(genero)
    return alturas, generos


def analisar_dados(alturas, generos):
    """Analisa os dados e apresenta os resultados."""
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    altura_homens = 0
    num_homens = generos.count('M')
    num_mulheres = generos.count('F')
    for i in alturas:
        if generos[i] == 'M':
            altura_homens += alturas[i]

    media_homens = altura_homens / num_homens





    print("A maior altura é:", maior_altura, "metros.")
    print("A menor altura é:", menor_altura, "metros.")
    print("A média de altura dos homens é:", media_homens, "metros.")
    print("O número de mulheres é:", num_mulheres)


# Coletando os dados
alturas, generos = coletar_dados()

# Analisando os dados
analisar_dados(alturas, generos)




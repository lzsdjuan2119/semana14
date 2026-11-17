import pandas as pd
import matplotlib.pyplot as plt

archivo = "PBI_Paises.csv"
data = pd.read_csv(archivo, thousands=',')
data.set_index('Country', inplace=True)

anios = list(map(str, range(2000, 2025)))

def grafico1():
    data.loc["Peru", anios].plot(kind='line')
    plt.title("PBI de Peru (2000-2024)")
    plt.show()

def grafico2():
    data.loc[["Peru", "Chile"], anios].T.plot(kind='line')
    plt.title("PBI de Peru y Chile (2000-2024)")
    plt.show()

def grafico3():
    top5 = data.sort_values(by='2024', ascending=False).head(5)
    top5[anios].T.plot(kind='line')
    plt.title("Top 5 PBI (2000-2024)")
    plt.show()

def main():
    while True:
        print("\n--- EJERCICIO 1: GRAFICOS LINEALES ---")
        print("1. Grafico PBI Peru (2000-2024)")
        print("2. Grafico PBI Peru y Chile (2000-2024)")
        print("3. Grafico Top 5 PBI (2000-2024)")
        print("4. Salir")
        opcion = input("Elige una opcion (1-4): ")

        if opcion == "1":
            grafico1()
        elif opcion == "2":
            grafico2()
        elif opcion == "3":
            grafico3()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()

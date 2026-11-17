import pandas as pd
import matplotlib.pyplot as plt

archivo = "PBI_Paises.csv"
data = pd.read_csv(archivo, thousands=',')
data.set_index('Country', inplace=True)

def grafico_top10():
    top10 = data.sort_values(by='2018', ascending=True,inplace=True)
    top10=data['2018'].tail(10)
    top10.plot(kind='barh')
    plt.title("Top 10 Paises por PBI (2018)")
    plt.xlabel("Años")
    plt.show()

def main():
    while True:
        print("\n--- EJERCICIO 2: GRAFICO DE BARRAS ---")
        print("1. Mostrar grafico de barras Top 10 (2018)")
        print("2. Salir")
        opcion = input("Elige una opcion (1-2): ")

        if opcion == "1":
            grafico_top10()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()

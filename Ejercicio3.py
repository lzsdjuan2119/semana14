import pandas as pd
import matplotlib.pyplot as plt

archivo = "PBI_Paises.csv"
data = pd.read_csv(archivo, thousands=',')
data.set_index('Country', inplace=True)

def grafico_area():
    top5 = data.sort_values(by='2018', ascending=False).head(5)
    top5['2018'].plot(kind='area')
    plt.title("Top 5 Paises por PBI (2018) - Area")
    plt.show()

def main():
    while True:
        print("\n--- EJERCICIO 3: GRAFICO DE AREAS ---")
        print("1. Mostrar grafico de area Top 5 (2018)")
        print("2. Salir")
        opcion = input("Elige una opcion (1-2): ")

        if opcion == "1":
            grafico_area()
        elif opcion == "2":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()

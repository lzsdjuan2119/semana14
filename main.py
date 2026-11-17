import Ejercicio1
import Ejercicio2
import Ejercicio3

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ============")
        print("1. Ejercicio 1 ")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3 ")
        print("4. Salir")
        print("================================================")
        
        opcion = input("Elige un ejercicio (1-4): ")

        if opcion == "1":
            Ejercicio1.main()
        elif opcion == "2":
            Ejercicio2.main()
        elif opcion == "3":
            Ejercicio3.main()
        elif opcion == "4":
            print("chau p ")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()

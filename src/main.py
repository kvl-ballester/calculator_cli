from calculator.calculator import Calculator
ACCION_TEXT = """
    Seleccionar accion. \n
    1) Sumar\n
    2) Restar\n
    3) Multiplicar\n
    4) Dividir\n
    5) Salir
"""

def ask_number(number_label: str):
    while True:
        try:
            numero_str = input(f"Escribir número {number_label}: ")
            numero_float = float(numero_str)
            return numero_float
        except ValueError:
            print("#"* 25 +  "\n## Opcion no válida.\n" + "#" * 25)
            continue


def main(calculator: Calculator):
    print("Calculator CLI.")
    while True:
        accion_str = input(ACCION_TEXT)
        try:
            accion_int = int(accion_str)
            if accion_int < 1 or accion_int > 5:
                raise ValueError
            
        except ValueError:
            print("#"* 25 +  "\n## Opcion no válida.\n" + "#" * 25)
            continue

        if accion_int == 5:
            print("Adios!")
            return
        
        a = ask_number("a")
        b = ask_number("b")

        if accion_int == 1:
            result = calculator.sumar(a, b)
        if accion_int == 2:
            result = calculator.restar(a, b)
        if accion_int == 3:
            result = calculator.multiplicar(a, b)
        if accion_int == 4:
            result = calculator.dividir(a, b)

        print(f"\nResultado: {result} \n")
if __name__ == "__main__":
    calculator = Calculator()
    main(calculator)







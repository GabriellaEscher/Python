import math

def calculadora_log(base, number):
    return math.log(number) / math.log(base)

def main():
    print("calculadora de Logaritmo")

    try:
        number = float(input("Digite o número: "))
        base = float(input("Digite a base: "))

        if number <= 0 or base <= 0:
            print("O número e a base devem ser maiores que zero.")
            return
        
        result = calculadora_log(number, base)
        result_int = round(result)
        print(f"Log base {base} de {number} é {result_int}")
        
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()


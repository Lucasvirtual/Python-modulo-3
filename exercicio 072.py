numeros = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente, digite outro número")
print(f"Você digitou o número {numeros[num]}")
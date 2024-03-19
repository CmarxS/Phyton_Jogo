import random
número = random.randint(1, 100)
chute = int(input("Digite o número a ser adivinhado: "))
tentativas = 10

while tentativas > 0:
        if chute == número:
         print(f"Você acertou! o número misterioso era {número} ")
         break
        elif chute > número:
         tentativas -= 1
         print(f"O número misterioso é menor que {chute}")
         print(f"Tentativas restantes: {tentativas}")
         chute = int(input("Digite o número a ser adivinhado: "))
        else: 
         tentativas -= 1
         print(f"O número misterioso é maior que {chute}")
         print(f"Tentativas restantes: {tentativas}")
         chute = int(input("Digite o número a ser adivinhado: "))
        if tentativas == 0:
            print(f"Fim das tentativas, o número misterioso era {número}")
            break


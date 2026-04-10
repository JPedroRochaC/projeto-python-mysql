import random
print ('======= ADVINHE O NÚMERO =======')
print(' Nivel de dificuldade \n 1. FÁCIL (1 a 10) \n 2. MÉDIO (1 a 15) \n 3. DIFÍCIL (1 a 20)')
dificuldade=int(input(' Digite seu nivel de dificuldade: '))
if dificuldade == 1 :
 numero = random.randint(1, 10)
elif dificuldade == 2 :
 numero = random.randint(1, 15)
else :
 numero = random.randint(1, 20)
print ('======= VALENDO =======')
chute = int(input('Seu chute: '))
contador = 1

while chute != numero :
      contador += 1
      if chute > numero:
        print('Muito alto')
        chute = int(input('Seu chute: '))
      elif chute < numero :
        print('Muito baixo')
        chute = int(input('Seu chute: '))

print(f'Parabéns você acertou o número era {numero}!')
print(f'Tentativas: {contador}')
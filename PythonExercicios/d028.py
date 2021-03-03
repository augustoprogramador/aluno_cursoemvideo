from random import randint

p1 = int(input('Tente advinhar o húmero que estou "pensando" entre 0 e 5...\n'))
p2 = randint(0, 5)
if p1 == p2:
    print(f'PARABÉNS! Você acertou! o número que escolhi foi {p2}')
else:
    print(f'Que pena, você errou! O número que escolhi foi {p2}. Quer jogar de novo?')

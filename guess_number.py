import random 

#usuario 
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um numero entre 1 a {x}: '))
        if guess < random_number:
            print('Desculpe, adivinhe de novo. Muito baixo')
        elif guess > random_number:
            print('Desculpe, adivinhe de novo. Muito alto')
    print(f'Sim, parabéns. Você adivinhou o número {random_number} corretamente')
guess(10)

#computador
def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Se {guess} é muito alto (A), muito baixo (B) ou correto (C)??').lower()
        if feedback == 'a':
            high = guess - 1
        if feedback == 'b':
            low = guess + 1
    print(f'Yey! O computador adivinhou seu numero, {guess} corretamente!')
computer_guess(10)
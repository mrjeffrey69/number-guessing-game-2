import random
numbers = [num for num in range(1,101)]

answer = random.choice(numbers)




def main():
    is_running = True

    print("welcome to the number guessing game!")
    print("guess the number between 1 and 100")
    print('1.Easy')
    print('2.Medium')
    print('3.Hard')
    while True:
        diff = input('select your difficulty(1,2,3): ')

        # check if difficulty is valid
        match diff:
            case '1':
                lives = 20
                break
            case '2':
                lives = 10
                break
            case '3':
                lives = 5
                break
            case _:
                print(f'{diff} is not a valid difficulty , please pick a number between 1 and 3')
                continue



    while is_running:
        guess = input('enter your guess: ')
        
        # check if guess is a valid number
        if not guess.isdigit():
            print(f'{guess} is not a valid number , please pick a number between 1 and 100')
            continue
        guess = int(guess)
        if guess > 100 or guess < 1:
            print(f'guess is out of range , please pick a number between 1 and 100')
            continue
        # see if answer is right
        if guess == answer:
            print(f'You Win!\nThe number was {answer}\n lives left: {lives}')
            break

        elif guess < answer:
            print('higher')
            lives -= 1
            print(lives)
        elif guess > answer:
            print('lower')
            lives -= 1
            print (lives)
        # check if dead
        if lives  == 0:
            print(f'You Lose!\nThe number was {answer}')
            break

    play_again = input('would you like to play again?(y,n): ').lower()

    if play_again == "y":
        main()
    else:
        print('thanks for playing')
        print('goodbye')




if __name__ == "__main__":
    main()
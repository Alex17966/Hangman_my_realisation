from game import Game
from game_status import GameStatus

game = Game()
word = game.word_generator()


def chars_to_list(lst):
    return ''.join(lst)


print(f'Hi! Please guess the word of {len(word)} letters')
print(chars_to_list(['-' for item in word]))


while game.game_satus == GameStatus.IN_PROGRESS:
    print(f'Used letters: {chars_to_list(game.tried_letters)}')
    letter = input(f'Input a letter. {game.allowed_mistakes - game.mistakes_made} tries remained')

    print(chars_to_list(game.word_output(letter)))

    if game.game_satus == GameStatus.LOST:
        print('You are hanged! You lose')
        print(f'The word was {word}')
    elif game.game_satus == GameStatus.WON:
        print('Congrats! You are Winner')

import random

from game_status import GameStatus
from invalid_exception import InvalidExceptionError


class Game:
    def __init__(self, allowed_mistakes: int = 6):
        if not 4 <= allowed_mistakes <= 10:
            raise ValueError(f'Allowed mistakes should be between 4 and 10. You chose {allowed_mistakes}')

        self.allowed_mistakes = allowed_mistakes
        self.mistakes_made = 0
        self.tried_letters = []
        self.opened_indexes = []
        self.game_satus = GameStatus.NOT_STARTED
        self.word = ''

    def word_generator(self) -> str:
        words = []
        with open('data/WordsStockRUS.txt', encoding='utf8') as file:
            for item in file:
                words.append(item.rstrip('\n'))
            self.word = random.choice(words)

        self.opened_indexes = [False for _ in self.word]
        self.game_satus = GameStatus.IN_PROGRESS

        return self.word

    def word_output(self, letter: str) -> list[str]:
        if self.mistakes_made == self.allowed_mistakes:
            raise InvalidExceptionError('Incorporated error')
        if self.game_satus != GameStatus.IN_PROGRESS:
            raise InvalidExceptionError('Incorporated error')

        open_any = False
        result = []
        for index, cur_letter in enumerate(self.word):
            if cur_letter == letter:
                open_any = True
                self.opened_indexes[index] = True

            if self.opened_indexes[index]:
                result.append(cur_letter)
            else:
                result.append('-')

        if not open_any:
            self.mistakes_made += 1

        self.tried_letters.append(letter)

        if self.mistakes_made == self.allowed_mistakes:
            self.game_satus = GameStatus.LOST

        if all(self.opened_indexes):
            self.game_satus = GameStatus.WON

        return result

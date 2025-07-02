import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class RockPlayer(Player):
    def move(self):
        return 'rock'


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = random.choice(moves)

    def move(self):
        return self.their_last_move

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = random.choice(moves)

    def move(self):
        index = moves.index(self.my_last_move)
        next_move = moves[(index + 1) % len(moves)]
        return next_move

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, Paper, or Scissors?\n").lower()
            if choice in moves:
                return choice
            else:
                print("Please type in Rock, Paper, or Scissors")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 Wins the round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 Wins the round!")
            self.p2_score += 1
        else:
            print("Round Tied!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"Player 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"Final score for Player 1: {self.p1_score}")
        print(f"Final score for Player 2: {self.p2_score}")

        if self.p1_score > self.p2_score:
            print("Player 1 Wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 Wins the game!")
        else:
            print("No winner! It's a draw!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RockPlayer())
    game.play_game()

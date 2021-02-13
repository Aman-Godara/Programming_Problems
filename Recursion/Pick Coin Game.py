"""Coin game: Alice and Bob are playing a game using a bunch of coins.
The players pick several coins out of the bunch in turn.
Each time a player is allowed to pick 1, 2 or 4 coins, and the player that gets the last coin is the winner.
Assume that both players are very smart and he/she will try his/her best to
work out a strategy to win the game. For example, if there are 2
coins and Alice is the first player to pick, she will definitely pick 2 coins and win.
If there are 3 coins and Alice is still the first player
to pick, no matter she picks 1 or 2 coins, Bob will get the last coin and win the game.
Given the number of coins and the order of
players (which means the first and the second players to pick the
coins), you are required to write a program to calculate the winner
of the game, and calculate how many different strategies there are
for he/she to win the game.
You should use recursion to solve the problem, and the parameters are read from the command line.
You can assume that there are no more than 30 coins.

Here are some sample runs of the program:
./pickcoin 1 alice bob
alice 1
./pickcoin 2 bob alice
bob 1
./pickcoin 3 alice bob
bob 2
./pickcoin 10 alice bob
alice 22
./pickcoin 25 alice bob
alice 3344
./pickcoin 30 alice bob
bob 18272
"""


def pickCoins(choices_array, coins_available):
    # function returns a negative value or a positive value or zero
    # positive value: indicates number of ways in which current player can win, it is guaranteed that current player will win.
    # negative value: indicates number of ways in which opponent player can win, it is guaranteed that opponent player will win.

    # if no coins are available; current player has lost and the path followed to reach here is one way in which the current player can lose
    if coins_available == 0:
        return -1
    # if coins available are negative; previous player has voilated the rules
    if coins_available < 0:
        return 0
    losses, wins = 0, 0
    for choice in choices_array:
        opponents_turn = pickCoins(choices_array,
                                   coins_available - choice)  # opponent's response, if current player takes this choice
        # if opponents_turn is negative: this is a good choice
        if opponents_turn <= 0:
            wins = wins + (-1 * opponents_turn)
        # if opponents_turn is positive: this is a bad choice
        else:
            losses = losses + (-1 * opponents_turn)

    # first priority of a player is to win
    if wins > 0:  # if it possible to win
        return wins  # then return number of ways current player can win
    # if there is no way to win, then player doesn't have any option other than to lose
    # in other words, a player will make a bad choice only if there are no good choices to make
    return losses


print(pickCoins([1, 2, 4], 3))

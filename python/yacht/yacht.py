# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    elif category == FULL_HOUSE:
        what_dice = list(set(dice))
        if (len(what_dice) == 2 and (dice.count(what_dice[0]) == 2 or
                                     dice.count(what_dice[0]) == 3)):
            return sum(dice)
        return 0
    elif category == FOUR_OF_A_KIND:
        what_dice = list(set(dice))
        for die in what_dice:
            if dice.count(die) >= 4:
                return 4 * die
        return 0
    elif category == LITTLE_STRAIGHT:
        what_dice = list(set(dice))
        if len(what_dice) == 5 and 6 not in dice:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        what_dice = list(set(dice))
        if len(what_dice) == 5 and 1 not in dice:
            return 30
        return 0
    elif category == YACHT:
        what_dice = list(set(dice))
        if len(what_dice) == 1:
            return 50
        return 0
    else:
        return sum(dice)

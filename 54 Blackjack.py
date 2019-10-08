"""Blackjack"""
def main(num):
    """Blackjack"""
    score = 0
    count = 0
    for _ in range(num):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            count += 1
        else:
            score += int(card)

    if count == 1:
        if score <= 10:
            score += 11
        else:
            score += 1
    if count == 2:
        if score <= 9:
            score += 12
        elif score >= 10:
            score += 2
    if count == 3:
        score += 13
    print(score)

main(int(input()))

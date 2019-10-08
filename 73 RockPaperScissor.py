"""<3 Jeffy"""
def main(text):
    """RockPaperScissor"""
    count = 0
    score1 = 0
    score2 = 0
    for _ in range(len(text)//2):
        player1 = text[count]
        count += 1
        player2 = text[count]
        count += 1
        score1, score2 = check(player1, player2, score1, score2)
    if score1 > score2:
        print("A win %d-%d"%(score1, score2))
    elif score2 > score1:
        print("B win %d-%d"%(score2, score1))
    else:
        print("DRAW %d"%score1)

def check(player1, player2, score1, score2):
    """gOd"""
    if player1 == "R":
        if player2 == "S":
            score1 += 1
        elif player2 == "P":
            score2 += 1
    elif player1 == "S":
        if player2 == "P":
            score1 += 1
        elif player2 == "R":
            score2 += 1
    elif player1 == "P":
        if player2 == "R":
            score1 += 1
        elif player2 == "S":
            score2 += 1
    return score1, score2
main(input())

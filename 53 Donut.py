"""Donut"""
def main(price, kob, term, want):
    """Donut"""
    canall = (kob + term) * (want //(kob + term))
    result = (kob * (want //(kob + term))) * price
    canterm = want - canall
    if canterm >= kob:
        canall += kob + term
        result += price * kob
    else:
        canall += canterm
        result += price * canterm
    print("%d %d"%(result, canall))
main(int(input()), int(input()), int(input()), int(input()))

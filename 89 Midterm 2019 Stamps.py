"""ig : chw_jeffy"""
def main(times, kob_baht, stamp, kob_stamp, lod):
    """[Midterm 2019] Stamps"""
    result_price = 0
    mystamp = 0
    for _ in range(times):
        price = int(input())
        if mystamp >= kob_stamp:
            while 1:
                if price <= 0 or mystamp < kob_stamp:
                    break
                price -= lod
                mystamp -= kob_stamp
        if price < 0:
            price = 0
        result_price += price
        if price >= kob_baht:
            mystamp += stamp * (price // kob_baht)
    print(result_price, mystamp, sep="\n")

main(int(input()), int(input()), int(input()), int(input()), int(input()))

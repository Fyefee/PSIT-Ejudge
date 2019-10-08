"""Timing II"""
def main(num):
    """Timing II"""
    result_seconds = num % 60
    minute = num // 60
    result_minute = minute % 60
    hour = minute // 60
    result_hour = hour % 24
    day = hour // 24
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(day, result_hour, result_minute, result_seconds))

main(int(input()))

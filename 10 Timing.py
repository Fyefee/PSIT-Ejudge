"""Timing"""
def main(num):
    """Timing"""
    result_seconds = num % 60
    minute = num // 60
    result_minute = minute % 60
    hour = minute // 60
    result_hour = hour % 24
    day = hour // 24
    print("%d %d %d %d"%(day, result_hour, result_minute, result_seconds))

main(int(input()))

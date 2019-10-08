"""Turnstile"""
def main():
    """Turnstile"""
    state = "P"
    count = 0
    while 1:
        text = input()
        if text == "END":
            break
        if text == "P" and state == "C":
            state = "P"
            count += 1
        elif text == "C" and state == "P":
            state = "C"
    print(count)

main()

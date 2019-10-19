"""ig : chw_jeffy"""
def main(text):
    """RemoveTag"""
    tag = []
    delete = ""
    for i in text:
        if "<" in delete and i == ">":
            delete += i
            tag.append(delete)
            delete = ""
        elif i == "<":
            delete += i
        elif "<" in delete:
            delete += i
    for i in tag:
        text = text.replace(i, " ")
    print(text.split())

main(input())

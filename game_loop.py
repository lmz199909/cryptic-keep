from help import helps
def Loop(s):
    while True:
        s=input("<").strip().lower()
        if s==help:
            helps()
        elif s.startswith("go"):
            s=s.split(" ")[1]
            
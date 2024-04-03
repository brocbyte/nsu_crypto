import hashlib

hs = {}
def hash(txt):
    hashGen = hashlib.sha512()
    hashGen.update(txt)
    return hashGen.hexdigest()

def help():
    print("""
    command 'register' -> r _login _pass
    command 'login' -> l _login _pass
    command 'info' -> i
    command 'help' -> h
    command 'exit' -> e
          """)

def report():
    print("invalid command :((")

def main():
    help()
    while True:
        txt = input()
        toks = txt.split(' ')
        if len(toks) == 0:
            report()
            continue
        command = toks[0]
        print("command: " + command)
        if command == 'r':
            if len(toks) != 3:
                report()
                continue
            login = toks[1]
            h = hash(toks[2].encode('utf-8'))
            print(f"login: {login}, pass: {toks[2]}")
            hs[login] = h
        elif command == 'l':
            if len(toks) != 3:
                report()
                continue
            login = toks[1]
            h = hash(toks[2].encode('utf-8'))
            print(f"login: {login}, pass: {toks[2]}")
            if login in hs and hs[login] == h: print("Logged in!")
            else: print("Failed to login :(")
        elif command == 'i':
            print(hs)
        elif command == 'h':
            help()
        elif command == 'e':
            exit(0)


if __name__ == "__main__":
    main()


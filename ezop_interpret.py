import sys
import random

def interpret_ezop(code):
    queue = list(code)
    at_var = 0

    while queue:
        cmd = queue.pop(0)
        if cmd == 'I' and queue and queue[0] == '@':
            queue.pop(0)
            try:
                at_var = int(input())
            except ValueError:
                print("Chyba: Neplatný vstup")
                return
        elif cmd == 'G' and queue and queue[0] == '@':
            queue.pop(0)
            at_var = random.randint(-1024, 1024)
        elif cmd == 'O' and queue and queue[0] == '@':
            queue.pop(0)
            print(at_var)
        elif cmd == '+':
            at_var += 1
        elif cmd == '-':
            at_var -= 1
        elif cmd == '0':
            at_var = 0
        elif cmd == '#':
            print("Skript ukončen.")
            return
        else:
            print("Chyba: Neplatná instrukce")
            return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použití: python script.py "I@++O@-O@#"")
    else:
        interpret_ezop(sys.argv[1])

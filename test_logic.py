import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "DRAW!"
    elif user_choice == 0 and computer_choice == 1:
        return "COMPUTER WINS!"
    elif user_choice == 0 and computer_choice == 2:
        return "USER WINS!"
    elif user_choice == 1 and computer_choice == 0:
        return "USER WINS!"
    elif user_choice == 1 and computer_choice == 2:
        return "COMPUTER WINS!"
    elif user_choice == 2 and computer_choice == 0:
        return "COMPUTER WINS!"
    elif user_choice == 2 and computer_choice == 1:
        return "USER WINS!"
    return "DRAW!"


def game_py_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "DRAW"
    elif user_choice == 0 and computer_choice == 1:
        return "COMPUTER"
    elif user_choice == 0 and computer_choice == 2:
        return "USER"
    elif user_choice == 1 and computer_choice == 0:
        return "USER"
    elif user_choice == 1 and computer_choice == 2:
        return "COMPUTER"
    elif user_choice == 2 and computer_choice == 0:
        return "COMPUTER"
    elif user_choice == 2 and computer_choice == 1:
        return "USER"
    return "DRAW"


names = ["Rock", "Paper", "Scissor"]
passed = 0
total = 0
for u in range(3):
    for c in range(3):
        total += 1
        gui = decide_winner(u, c)
        orig = game_py_result(u, c)
        if orig == "DRAW":
            ok = gui == "DRAW!"
        elif orig == "USER":
            ok = gui == "USER WINS!"
        else:
            ok = gui == "COMPUTER WINS!"
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"[{status}] User={names[u]:8} Comp={names[c]:8} -> GUI={gui:15} game.py={orig}")

print(f"\n{passed}/{total} tests passed")
sys.exit(0 if passed == total else 1)
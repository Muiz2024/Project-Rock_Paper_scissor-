import tkinter as tk
import game_gui
import traceback

try:
    root = tk.Tk()
    app = game_gui.RockPaperScissorsGUI(root)

    app.on_user_select(0)
    print("user_choice:", app.user_choice)
    print("states:", [b["state"] for b in app.choice_buttons])

    app._computer_turn()
    print("computer_choice:", app.computer_choice)
    print("result:", app.result_label.cget("text"))
    print("states after turn:", [b["state"] for b in app.choice_buttons])

    app.restart_game()
    print("after restart user:", app.user_choice)
    print("after restart result:", repr(app.result_label.cget("text")))
    print("after restart user_text:", repr(app.user_text.cget("text")))
    print("after restart comp_text:", repr(app.comp_text.cget("text")))

    root.destroy()
    print("Full flow simulation PASSED")
except Exception:
    traceback.print_exc()
    raise
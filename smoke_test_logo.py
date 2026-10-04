import tkinter as tk
import game_gui
import traceback

try:
    root = tk.Tk()
    app = game_gui.RockPaperScissorsGUI(root)
    print("Title:", root.title())
    print("Logo loaded:", app.logo_image is not None)
    print("Canvas items:", len(app.canvas.find_all()))

    app.on_user_select(0)
    print("After select -> states:", [b["state"] for b in app.choice_buttons])
    print("status text:", app.canvas.itemcget(app.status_id, "text"))

    app._computer_turn()
    print("result:", app.canvas.itemcget(app.result_id, "text"))
    print("result fill:", app.canvas.itemcget(app.result_id, "fill"))
    print("states after turn:", [b["state"] for b in app.choice_buttons])

    app.restart_game()
    print("after restart user:", app.user_choice)
    print("after restart result:", repr(app.canvas.itemcget(app.result_id, "text")))

    root.after(800, root.destroy)
    root.mainloop()
    print("Dark theme smoke test PASSED")
except Exception:
    traceback.print_exc()
    raise

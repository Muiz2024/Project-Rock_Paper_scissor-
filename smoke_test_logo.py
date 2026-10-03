import tkinter as tk
import game_gui
import traceback

try:
    root = tk.Tk()
    app = game_gui.RockPaperScissorsGUI(root)
    print("Title:", root.title())
    print("Logo loaded:", app.logo_image is not None)
    print("Logo full loaded:", app.logo_image_full is not None)
    root.after(1200, root.destroy)
    root.mainloop()
    print("GUI smoke test with logo PASSED")
except Exception:
    traceback.print_exc()
    raise
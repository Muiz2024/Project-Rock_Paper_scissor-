import os
import sys
import random
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk


def resource_path(relative_path):
    """Return absolute path to a resource, works for dev and PyInstaller .exe."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


CHOICES = ["Rock", "Paper", "Scissor"]
EMOJI = ["\U0001FAA8", "\U0001F4DD", "\u2702\uFE0F"]
IMG_FILES = ["rock.png", "paper.png", "scissor.png"]

BG_COLOR = "#f4f6fb"
TITLE_COLOR = "#2c3e50"
ACCENT = "#2980b9"
USER_COLOR = "#27ae60"
COMP_COLOR = "#e74c3c"
RESULT_COLORS = {
    "USER WINS!": "#27ae60",
    "COMPUTER WINS!": "#e74c3c",
    "DRAW!": "#f39c12",
}


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.user_choice = None
        self.computer_choice = None
        self.choice_buttons = []
        self.photo_images = {}

        self._load_images()
        self._set_window_icon()
        self._build_ui()

    def _load_images(self):
        for idx, fname in enumerate(IMG_FILES):
            path = resource_path(os.path.join("images", fname))
            img = Image.open(path).resize((110, 110), Image.LANCZOS)
            self.photo_images[idx] = ImageTk.PhotoImage(img)

        qpath = resource_path(os.path.join("images", "question.png"))
        qimg = Image.open(qpath).resize((110, 110), Image.LANCZOS)
        self.question_image = ImageTk.PhotoImage(qimg)

        logo_path = resource_path(os.path.join("images", "logo.png"))
        logo_img = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(logo_img.resize((56, 56), Image.LANCZOS))
        self.logo_image_full = ImageTk.PhotoImage(logo_img)

    def _set_window_icon(self):
        ico_path = resource_path(os.path.join("images", "logo.ico"))
        try:
            self.root.iconbitmap(default=ico_path)
        except tk.TclError:
            pass
        try:
            self.root.iconphoto(False, self.logo_image_full)
        except tk.TclError:
            pass

    def _build_ui(self):
        title_frame = tk.Frame(self.root, bg=BG_COLOR)
        title_frame.grid(row=0, column=0, columnspan=3, pady=(15, 5))

        tk.Label(
            title_frame, image=self.logo_image, bg=BG_COLOR,
        ).pack(side=tk.LEFT, padx=(10, 10))

        tk.Label(
            title_frame,
            text="ROCK PAPER SCISSORS",
            font=("Helvetica", 26, "bold"),
            fg=TITLE_COLOR,
            bg=BG_COLOR,
        ).pack(side=tk.LEFT)

        sep_top = tk.Frame(self.root, height=3, bg=ACCENT, width=520)
        sep_top.grid(row=1, column=0, columnspan=3, pady=(0, 15))

        tk.Label(
            self.root, text="Your Choice", font=("Helvetica", 14, "bold"),
            fg=USER_COLOR, bg=BG_COLOR,
        ).grid(row=2, column=0, pady=(0, 5))
        tk.Label(
            self.root, text="Computer Choice", font=("Helvetica", 14, "bold"),
            fg=COMP_COLOR, bg=BG_COLOR,
        ).grid(row=2, column=2, pady=(0, 5))

        self.user_img_label = tk.Label(self.root, image=self.question_image, bg=BG_COLOR)
        self.user_img_label.grid(row=3, column=0, padx=30)

        self.user_text = tk.Label(
            self.root, text="", font=("Helvetica", 12), fg=TITLE_COLOR, bg=BG_COLOR,
        )
        self.user_text.grid(row=4, column=0, pady=(5, 10))

        self.comp_img_label = tk.Label(self.root, image=self.question_image, bg=BG_COLOR)
        self.comp_img_label.grid(row=3, column=2, padx=30)

        self.comp_text = tk.Label(
            self.root, text="", font=("Helvetica", 12), fg=TITLE_COLOR, bg=BG_COLOR,
        )
        self.comp_text.grid(row=4, column=2, pady=(5, 10))

        sep_mid = tk.Frame(self.root, height=2, bg="#bdc3c7", width=520)
        sep_mid.grid(row=5, column=0, columnspan=3, pady=(10, 10), padx=10)

        self.result_label = tk.Label(
            self.root, text="", font=("Helvetica", 30, "bold"),
            fg=TITLE_COLOR, bg=BG_COLOR,
        )
        self.result_label.grid(row=6, column=0, columnspan=3, pady=(10, 10))

        self.status_label = tk.Label(
            self.root, text="Click a choice to play!", font=("Helvetica", 12),
            fg="#7f8c8d", bg=BG_COLOR,
        )
        self.status_label.grid(row=7, column=0, columnspan=3, pady=(0, 10))

        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.grid(row=8, column=0, columnspan=3, pady=(5, 5))

        for idx, name in enumerate(CHOICES):
            btn = tk.Button(
                btn_frame,
                image=self.photo_images[idx],
                text=f"{EMOJI[idx]} {name}",
                compound=tk.TOP,
                font=("Helvetica", 11, "bold"),
                fg=TITLE_COLOR,
                bg="#ffffff",
                activebackground="#d6eaf8",
                relief=tk.RAISED,
                bd=3,
                padx=10,
                pady=6,
                cursor="hand2",
                command=lambda i=idx: self.on_user_select(i),
            )
            btn.grid(row=0, column=idx, padx=15)
            self.choice_buttons.append(btn)

        restart_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=("Helvetica", 13, "bold"),
            fg="#ffffff",
            bg=ACCENT,
            activebackground="#1f6391",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.restart_game,
        )
        restart_btn.grid(row=9, column=0, columnspan=3, pady=(15, 5))

        tk.Label(
            self.root,
            text="developed by: Muhammad Muiz Hamza Ahmed",
            font=("Helvetica", 10, "italic"),
            fg="#95a5a6",
            bg=BG_COLOR,
        ).grid(row=10, column=0, columnspan=3, pady=(0, 15))

    def _set_buttons_state(self, state):
        for btn in self.choice_buttons:
            btn.configure(state=state)

    def on_user_select(self, choice):
        if self.user_choice is not None:
            return

        if choice < 0 or choice >= 3:
            messagebox.showerror("Invalid Choice", "Please select a valid option.")
            return

        self.user_choice = choice
        self._set_buttons_state(tk.DISABLED)

        self.user_img_label.configure(image=self.photo_images[choice])
        self.user_text.configure(text=f"You Chose: {EMOJI[choice]} {CHOICES[choice]}")

        self.comp_img_label.configure(image=self.question_image)
        self.comp_text.configure(text="")
        self.result_label.configure(text="")
        self.status_label.configure(text="Computer is thinking...", fg=ACCENT)

        self.root.after(3000, self._computer_turn)

    def _computer_turn(self):
        self.computer_choice = random.randint(0, 2)

        self.comp_img_label.configure(image=self.photo_images[self.computer_choice])
        self.comp_text.configure(
            text=f"Computer Chose: {EMOJI[self.computer_choice]} {CHOICES[self.computer_choice]}"
        )

        result = self._decide_winner(self.user_choice, self.computer_choice)
        self.result_label.configure(
            text=result, fg=RESULT_COLORS.get(result, TITLE_COLOR)
        )
        self.status_label.configure(text="Round complete! Click Restart to play again.", fg="#7f8c8d")

        self._set_buttons_state(tk.NORMAL)

    def _decide_winner(self, user_choice, computer_choice):
        """Reuse the exact winning conditions from game.py."""
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

    def restart_game(self):
        self.user_choice = None
        self.computer_choice = None

        self.user_img_label.configure(image=self.question_image)
        self.user_text.configure(text="")
        self.comp_img_label.configure(image=self.question_image)
        self.comp_text.configure(text="")
        self.result_label.configure(text="", fg=TITLE_COLOR)
        self.status_label.configure(text="Click a choice to play!", fg="#7f8c8d")

        self._set_buttons_state(tk.NORMAL)


def main():
    root = tk.Tk()
    RockPaperScissorsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
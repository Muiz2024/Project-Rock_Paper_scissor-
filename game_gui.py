import os
import sys
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

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

GRADIENT_TOP = (15, 23, 42)
GRADIENT_BOTTOM = (49, 46, 129)

HEADING = "#FFFFFF"
TEXT = "#CBD5E1"
DIM = "#94A3B8"
BTN_BG = "#1E293B"
BTN_ACTIVE = "#334155"
BTN_FG = "#E2E8F0"
BTN_BORDER = "#334155"
RESTART_BG = "#4F46E5"
RESTART_ACTIVE = "#4338CA"
ACCENT = "#818CF8"
SEPARATOR = "#475569"

RESULT_COLORS = {
    "USER WINS!": "#22C55E",
    "COMPUTER WINS!": "#EF4444",
    "DRAW!": "#F59E0B",
}

WIN_W = 560
WIN_H = 680


class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg="#0F172A")
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

    def _draw_gradient(self):
        top = GRADIENT_TOP
        bottom = GRADIENT_BOTTOM
        for y in range(WIN_H):
            t = y / (WIN_H - 1)
            r = int(top[0] + (bottom[0] - top[0]) * t)
            g = int(top[1] + (bottom[1] - top[1]) * t)
            b = int(top[2] + (bottom[2] - top[2]) * t)
            self.canvas.create_line(0, y, WIN_W, y, fill="#%02x%02x%02x" % (r, g, b))

    def _build_ui(self):
        self.canvas = tk.Canvas(
            self.root, width=WIN_W, height=WIN_H,
            highlightthickness=0, bd=0,
        )
        self.canvas.pack(fill="both", expand=True)
        self._draw_gradient()

        title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        title_text = "ROCK PAPER SCISSORS"
        text_w = title_font.measure(title_text)
        logo_w = 56
        gap = 12
        group_w = logo_w + gap + text_w
        start_x = (WIN_W - group_w) / 2
        self.canvas.create_image(start_x, 28, image=self.logo_image, anchor="nw")
        self.canvas.create_text(
            start_x + logo_w + gap, 56, text=title_text,
            font=("Helvetica", 24, "bold"), fill=HEADING, anchor="w",
        )

        self.canvas.create_line(40, 100, 520, 100, fill=SEPARATOR, width=2)

        self.canvas.create_text(
            140, 120, text="Your Choice",
            font=("Helvetica", 13, "bold"), fill=HEADING, anchor="center",
        )
        self.canvas.create_text(
            420, 120, text="Computer Choice",
            font=("Helvetica", 13, "bold"), fill=HEADING, anchor="center",
        )

        self.user_img_id = self.canvas.create_image(
            140, 135, image=self.question_image, anchor="n",
        )
        self.comp_img_id = self.canvas.create_image(
            420, 135, image=self.question_image, anchor="n",
        )

        self.user_text_id = self.canvas.create_text(
            140, 255, text="", font=("Helvetica", 12), fill=TEXT, anchor="center",
        )
        self.comp_text_id = self.canvas.create_text(
            420, 255, text="", font=("Helvetica", 12), fill=TEXT, anchor="center",
        )

        self.canvas.create_line(40, 290, 520, 290, fill=SEPARATOR, width=1)

        self.result_id = self.canvas.create_text(
            280, 330, text="", font=("Helvetica", 28, "bold"),
            fill=HEADING, anchor="center",
        )

        self.status_id = self.canvas.create_text(
            280, 378, text="Click a choice to play!",
            font=("Helvetica", 12), fill=DIM, anchor="center",
        )

        btn_y = 405
        btn_xs = [65, 215, 365]
        for idx, name in enumerate(CHOICES):
            btn = tk.Button(
                self.canvas,
                image=self.photo_images[idx],
                text=f"{EMOJI[idx]} {name}",
                compound=tk.TOP,
                font=("Helvetica", 11, "bold"),
                fg=BTN_FG,
                bg=BTN_BG,
                activebackground=BTN_ACTIVE,
                activeforeground="#FFFFFF",
                relief=tk.FLAT,
                bd=0,
                padx=10,
                pady=8,
                cursor="hand2",
                highlightthickness=2,
                highlightbackground=BTN_BORDER,
                highlightcolor=ACCENT,
                command=lambda i=idx: self.on_user_select(i),
            )
            self.canvas.create_window(btn_xs[idx], btn_y, window=btn, anchor="nw", width=130)
            self.choice_buttons.append(btn)

        restart_btn = tk.Button(
            self.canvas,
            text="Restart Game",
            font=("Helvetica", 13, "bold"),
            fg="#FFFFFF",
            bg=RESTART_BG,
            activebackground=RESTART_ACTIVE,
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            highlightthickness=0,
            command=self.restart_game,
        )
        self.canvas.create_window(195, 585, window=restart_btn, anchor="nw", width=170)

        self.canvas.create_text(
            280, 650, text="developed by: Muhammad Muiz Hamza Ahmed",
            font=("Helvetica", 10, "italic"), fill=DIM, anchor="center",
        )

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

        self.canvas.itemconfig(self.user_img_id, image=self.photo_images[choice])
        self.canvas.itemconfig(
            self.user_text_id,
            text=f"You Chose: {EMOJI[choice]} {CHOICES[choice]}",
        )

        self.canvas.itemconfig(self.comp_img_id, image=self.question_image)
        self.canvas.itemconfig(self.comp_text_id, text="")
        self.canvas.itemconfig(self.result_id, text="")
        self.canvas.itemconfig(self.status_id, text="Computer is thinking...", fill=ACCENT)

        self.root.after(3000, self._computer_turn)

    def _computer_turn(self):
        self.computer_choice = random.randint(0, 2)

        self.canvas.itemconfig(self.comp_img_id, image=self.photo_images[self.computer_choice])
        self.canvas.itemconfig(
            self.comp_text_id,
            text=f"Computer Chose: {EMOJI[self.computer_choice]} {CHOICES[self.computer_choice]}",
        )

        result = self._decide_winner(self.user_choice, self.computer_choice)
        self.canvas.itemconfig(
            self.result_id, text=result, fill=RESULT_COLORS.get(result, HEADING),
        )
        self.canvas.itemconfig(
            self.status_id,
            text="Round complete! Click Restart to play again.", fill=DIM,
        )

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

        self.canvas.itemconfig(self.user_img_id, image=self.question_image)
        self.canvas.itemconfig(self.user_text_id, text="")
        self.canvas.itemconfig(self.comp_img_id, image=self.question_image)
        self.canvas.itemconfig(self.comp_text_id, text="")
        self.canvas.itemconfig(self.result_id, text="", fill=HEADING)
        self.canvas.itemconfig(self.status_id, text="Click a choice to play!", fill=DIM)

        self._set_buttons_state(tk.NORMAL)


def main():
    root = tk.Tk()
    RockPaperScissorsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

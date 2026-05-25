# gui.py

import tkinter as tk
from tkinter import messagebox

from game_logic import board, check_winner, is_draw, reset_board
from ai import get_ai_move

# إنشاء النافذة
root = tk.Tk()

root.title("XO Minimax AI")
root.geometry("400x500")

# مستوى الصعوبة
difficulty = tk.StringVar()
difficulty.set("Hard")

# قائمة اختيار المستوى
difficulty_menu = tk.OptionMenu(
    root,
    difficulty,
    "Easy",
    "Medium",
    "Hard"
)

difficulty_menu.config(
    font=('Arial', 14),
    width=10
)

difficulty_menu.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=10
)

buttons = []

# تعطيل الأزرار
def disable_all_buttons():

    for btn in buttons:
        btn.config(state='disabled')

# عند الضغط على زر
def button_click(index):

    if board[index] == ' ':

        # حركة اللاعب
        board[index] = 'X'

        buttons[index].config(
            text='X',
            state='disabled'
        )

        # فوز اللاعب
        if check_winner('X'):

            messagebox.showinfo(
                "Result",
                "You Win!"
            )

            disable_all_buttons()
            return

        # تعادل
        if is_draw():

            messagebox.showinfo(
                "Result",
                "Draw!"
            )

            return

        # حركة الذكاء الاصطناعي
        ai_move = get_ai_move(
            difficulty.get()
        )

        board[ai_move] = 'O'

        buttons[ai_move].config(
            text='O',
            state='disabled'
        )

        # فوز الكمبيوتر
        if check_winner('O'):

            messagebox.showinfo(
                "Result",
                "Computer Wins!"
            )

            disable_all_buttons()
            return

        # تعادل
        if is_draw():

            messagebox.showinfo(
                "Result",
                "Draw!"
            )

# إعادة تشغيل اللعبة
def reset_game():

    reset_board()

    for btn in buttons:

        btn.config(
            text=' ',
            state='normal'
        )

# إنشاء أزرار اللعبة
for i in range(9):

    btn = tk.Button(
        root,
        text=' ',
        font=('Arial', 30),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(
        row=(i//3)+1,
        column=i%3
    )

    buttons.append(btn)

# زر إعادة التشغيل
reset_button = tk.Button(
    root,
    text="Restart Game",
    font=('Arial', 16),
    command=reset_game
)

reset_button.grid(
    row=4,
    column=0,
    columnspan=3,
    pady=20
)

# تشغيل اللعبة
def start_game():
    root.mainloop()
import customtkinter as ctk
import tkinter as tk
import random

# =========================
# Design
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================
# Das eigentliche Programm
# =========================

def prank_starten():
    MAX_WINDOWS = 100
    windows = []
    running = True

    ERROR_MESSAGES = [
        "Fatal Error",
        "System32 not found",
        "Unknown exception",
        "Memory access violation",
        "Kernel panic",
        "Unexpected error",
        "Something went terribly wrong"
    ]

    prank_root = tk.Tk()
    prank_root.withdraw()

    def stop_all(event=None):
        nonlocal running

        running = False

        for w in windows[:]:
            try:
                w.destroy()
            except:
                pass

        prank_root.destroy()

    def create_error_window(x=None, y=None):
        if not running:
            return

        if len(windows) >= MAX_WINDOWS:
            return

        win = tk.Toplevel(prank_root)

        width = 320
        height = 120

        if x is None:
            x = random.randint(
                0,
                win.winfo_screenwidth() - width
            )

        if y is None:
            y = random.randint(
                0,
                win.winfo_screenheight() - height
            )

        win.geometry(f"{width}x{height}+{x}+{y}")
        win.title("Error")

        windows.append(win)

        msg = random.choice(ERROR_MESSAGES)

        tk.Label(
            win,
            text="❌",
            font=("Arial", 24)
        ).pack()

        tk.Label(
            win,
            text=msg,
            font=("Arial", 12)
        ).pack()

        tk.Button(
            win,
            text="OK",
            command=lambda: None
        ).pack(pady=5)

        win.bind(
            "<Enter>",
            lambda e, w=win: clone_window(w)
        )

        win.bind("<Escape>", stop_all)

    def clone_window(window):
        if not running:
            return

        if len(windows) >= MAX_WINDOWS:
            return

        x = window.winfo_x()
        y = window.winfo_y()

        for _ in range(6):
            offset_x = random.randint(-150, 150)
            offset_y = random.randint(-150, 150)

            create_error_window(
                x + offset_x,
                y + offset_y
            )

    prank_root.bind("<Escape>", stop_all)

    create_error_window()

    prank_root.mainloop()

# =========================
# Warnungsfenster
# =========================

root = ctk.CTk()
root.title("Programmwarnung")
root.geometry("900x600")
root.resizable(False, False)

def stop_warning(event=None):
    root.destroy()

def show_agreement():
    warning_frame.pack_forget()
    agreement_frame.pack(fill="both", expand=True, padx=20, pady=20)

def update_start_button():
    if agreed.get():
        start_button.configure(state="normal")
    else:
        start_button.configure(state="disabled")

def start_program():
    root.destroy()
    prank_starten()

root.bind("<Escape>", stop_warning)

# =========================
# Seite 1
# =========================

warning_frame = ctk.CTkFrame(
    root,
    corner_radius=20
)

warning_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

ctk.CTkLabel(
    warning_frame,
    text="⚠ Programmwarnung",
    font=("Segoe UI", 32, "bold")
).pack(pady=(30, 15))

textbox = ctk.CTkTextbox(
    warning_frame,
    width=750,
    height=260,
    font=("Segoe UI", 14)
)

textbox.pack(pady=20)

textbox.insert(
    "0.0",
    """
⚠️ Inhaltswarnung

Das installierte Spiel enthält blinkende Lichteffekte, schnelle Bildwechsel, laute Geräusche, intensive Spannungselemente und Jumpscares.

Diese Inhalte können für manche Personen unangenehm oder belastend sein. Personen mit Epilepsie, Lichtempfindlichkeit oder einer erhöhten Empfindlichkeit gegenüber Schreckeffekten sollten vor dem Spielen Vorsicht walten lassen.

Bitte spiele verantwortungsvoll und achte auf dein eigenes Wohlbefinden.

Klicke auf „Weiter“, um fortzufahren, oder auf „Abbrechen“, um die Installation zu beenden.
"""
)

textbox.configure(state="disabled")

ctk.CTkButton(
    warning_frame,
    text="Weiter",
    width=220,
    height=50,
    font=("Segoe UI", 16, "bold"),
    command=show_agreement
).pack(pady=20)

# =========================

# Seite 2

# =========================

agreement_frame = ctk.CTkFrame(
root,
corner_radius=20
)

ctk.CTkLabel(
agreement_frame,
text="✓ Bestätigung",
font=("Segoe UI", 32, "bold")
).pack(pady=(30, 15))

agreement_textbox = ctk.CTkTextbox(
agreement_frame,
width=750,
height=260,
font=("Segoe UI", 14)
)

agreement_textbox.pack(pady=20)

agreement_textbox.insert(
"0.0",
"""
Bestätigung

Durch Klicken auf „Ich stimme zu“ bestätigst du, dass du die Inhaltswarnung gelesen hast und verstehst, dass das installierte Spiel folgende Inhalte enthalten kann:

• Blinkende Lichter und visuelle Effekte
• Laute Geräusche
• Schnelle Bildwechsel
• Spannungselemente und Jumpscares

Du möchtest die Installation dennoch fortsetzen.

Klicke auf „Ich stimme zu“, um fortzufahren, oder auf „Ablehnen“, um die Installation abzubrechen.
"""
)

agreement_textbox.configure(state="disabled")

agreed = ctk.BooleanVar()

ctk.CTkCheckBox(
agreement_frame,
text="Ich stimme zu und möchte fortfahren",
variable=agreed,
command=update_start_button,
font=("Segoe UI", 16)
).pack(pady=20)

start_button = ctk.CTkButton(
agreement_frame,
text="STARTEN",
state="disabled",
width=300,
height=60,
font=("Segoe UI", 18, "bold"),
command=start_program
)

start_button.pack(pady=30)
root.mainloop()
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CHARACTERS = [
    {
        "id": 1,
        "poem": (
            "Он в шляпе ходит каждый день,\n"
            "Играть в игры ему не лень.\n"
            "Усы пушистые, добрый взгляд —\n"
            "Кто это? Каждый будет рад!"
        ),
        "photo": resource_path("assets/person1.jpg"),
        "name": "Персонаж 1"
    },
    {
        "id": 2,
        "poem": (
            "Она поёт с самого утра,\n"
            "Смеётся звонко, как игра.\n"
            "Волосы рыжие, яркий стиль —\n"
            "Угадай, кто эта мисс?"
        ),
        "photo": resource_path("assets/person2.jpg"),
        "name": "Персонаж 2"
    },
]

class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Угадай кто")
        self.geometry("500x650")
        self.resizable(False, False)
        self.configure(fg_color="#0f0f1a")
        self.current_frame = None
        self.show_main_screen()

    def show_frame(self, frame_class, *args):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_screen(self):
        self.show_frame(MainScreen)

    def show_choice_screen(self):
        self.show_frame(ChoiceScreen)

    def show_poem_screen(self, char_index):
        self.show_frame(PoemScreen, char_index)

    def show_photo_screen(self, char_index):
        self.show_frame(PhotoScreen, char_index)


class MainScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        accent = ctk.CTkFrame(self, height=4, fg_color="#5865f2", corner_radius=0)
        accent.pack(fill="x")
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True)
        ctk.CTkLabel(center, text="🎮  ИГРА", font=ctk.CTkFont(family="Arial", size=18, weight="bold"), text_color="#5865f2").pack(pady=(0, 8))
        ctk.CTkLabel(center, text="Угадай кто?", font=ctk.CTkFont(family="Arial", size=44, weight="bold"), text_color="#ffffff").pack(pady=(0, 12))
        ctk.CTkLabel(center, text="Прочитай подсказку и угадай персонажа!", font=ctk.CTkFont(size=15), text_color="#9090aa").pack(pady=(0, 48))
        ctk.CTkButton(center, text="▶  Начать игру", font=ctk.CTkFont(size=18, weight="bold"), width=220, height=54, corner_radius=27, fg_color="#5865f2", hover_color="#4752c4", command=master.show_choice_screen).pack()
        ctk.CTkLabel(self, text="v1.0", font=ctk.CTkFont(size=11), text_color="#444466").pack(pady=16)


class ChoiceScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        accent = ctk.CTkFrame(self, height=4, fg_color="#5865f2", corner_radius=0)
        accent.pack(fill="x")
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True)
        ctk.CTkLabel(center, text="Выбери персонажа", font=ctk.CTkFont(size=30, weight="bold"), text_color="#ffffff").pack(pady=(0, 10))
        ctk.CTkLabel(center, text="Нажми на кнопку — получи подсказку", font=ctk.CTkFont(size=14), text_color="#9090aa").pack(pady=(0, 50))
        btn_frame = ctk.CTkFrame(center, fg_color="transparent")
        btn_frame.pack()
        for char in CHARACTERS:
            idx = char["id"] - 1
            ctk.CTkButton(btn_frame, text=f"  {char['id']}  ", font=ctk.CTkFont(size=36, weight="bold"), width=110, height=110, corner_radius=55, fg_color="#1e1e2e", hover_color="#5865f2", border_width=2, border_color="#5865f2", command=lambda i=idx: master.show_poem_screen(i)).pack(side="left", padx=20)
        ctk.CTkButton(self, text="← Назад", font=ctk.CTkFont(size=13), width=120, height=36, corner_radius=18, fg_color="transparent", hover_color="#1e1e2e", border_width=1, border_color="#444466", text_color="#9090aa", command=master.show_main_screen).pack(pady=24)


class PoemScreen(ctk.CTkFrame):
    def __init__(self, master, char_index):
        super().__init__(master, fg_color="transparent")
        char = CHARACTERS[char_index]
        accent = ctk.CTkFrame(self, height=4, fg_color="#5865f2", corner_radius=0)
        accent.pack(fill="x")
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True, padx=40)
        ctk.CTkLabel(center, text="🔍 Угадай кто это?", font=ctk.CTkFont(size=16, weight="bold"), text_color="#5865f2").pack(pady=(0, 24))
        card = ctk.CTkFrame(center, fg_color="#1e1e2e", corner_radius=16)
        card.pack(fill="x", pady=(0, 32))
        ctk.CTkLabel(card, text=char["poem"], font=ctk.CTkFont(size=17), text_color="#e0e0f0", justify="center", wraplength=380).pack(padx=30, pady=30)
        btn_frame = ctk.CTkFrame(center, fg_color="transparent")
        btn_frame.pack()
        ctk.CTkButton(btn_frame, text="← Назад", font=ctk.CTkFont(size=14), width=140, height=44, corner_radius=22, fg_color="transparent", hover_color="#1e1e2e", border_width=1, border_color="#444466", text_color="#9090aa", command=master.show_choice_screen).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Далее →", font=ctk.CTkFont(size=14, weight="bold"), width=140, height=44, corner_radius=22, fg_color="#5865f2", hover_color="#4752c4", command=lambda: master.show_photo_screen(char_index)).pack(side="left", padx=10)


class PhotoScreen(ctk.CTkFrame):
    def __init__(self, master, char_index):
        super().__init__(master, fg_color="transparent")
        char = CHARACTERS[char_index]
        accent = ctk.CTkFrame(self, height=4, fg_color="#5865f2", corner_radius=0)
        accent.pack(fill="x")
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True, padx=40)
        ctk.CTkLabel(center, text="🎉 Вот кто это!", font=ctk.CTkFont(size=22, weight="bold"), text_color="#ffffff").pack(pady=(0, 20))
        photo_path = char["photo"]
        if os.path.exists(photo_path):
            img = Image.open(photo_path)
            img = img.resize((300, 300), Image.LANCZOS)
            photo = ctk.CTkImage(light_image=img, dark_image=img, size=(300, 300))
            img_label = ctk.CTkLabel(center, image=photo, text="")
            img_label.image = photo
        else:
            img_label = ctk.CTkFrame(center, width=300, height=300, fg_color="#1e1e2e", corner_radius=16)
            ctk.CTkLabel(img_label, text="📷\nФото не найдено", text_color="#555577", font=ctk.CTkFont(size=14), justify="center").place(relx=0.5, rely=0.5, anchor="center")
        img_label.pack(pady=(0, 24))
        ctk.CTkLabel(center, text=char["name"], font=ctk.CTkFont(size=20, weight="bold"), text_color="#5865f2").pack(pady=(0, 24))
        ctk.CTkButton(center, text="← Назад к подсказке", font=ctk.CTkFont(size=14), width=200, height=44, corner_radius=22, fg_color="transparent", hover_color="#1e1e2e", border_width=1, border_color="#444466", text_color="#9090aa", command=lambda: master.show_poem_screen(char_index)).pack()


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()

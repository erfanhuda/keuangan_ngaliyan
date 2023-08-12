import tkinter as tk

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Aplikasi Keuangan Ngaliyan 2")
        self.geometry("800x600")


if __name__ == '__main__':
    app = Main()
    app.iconbitmap("icon.ico")
    app.mainloop()
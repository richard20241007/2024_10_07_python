from tkinter import ttk
from ttkthemes import ThemedTk


class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main():
    window = Window(theme='arc')
    window.mainloop()


if __name__ == '__main__':
    main()

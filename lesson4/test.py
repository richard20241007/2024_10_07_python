from ttkthemes import ThemedTk
from tkinter import ttk


class Window(ThemedTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title()
        self.title("homework!!!!")
        style = ttk.Style(self)
        # ===================TOP FRAME==================================================================#
        topFrame = ttk.Frame(self, borderwidth=1, relief='groove')
        btn1 = ttk.Button(topFrame, text='按鈕1', command=self.user_click1)
        btn1.pack(side='left', padx=10, expand=True)
        btn2 = ttk.Button(topFrame, text='按鈕2', command=self.user_click2)
        btn2.pack(side='left', padx=10, expand=True)
        btn3 = ttk.Button(topFrame, text='按鈕3')
        btn3.pack(side='left', padx=10, expand=True, command=self.user_click3)
        topFrame.pack(ipadx=10, expand=True, fill='x')
        # ==================End TOP FRAME====================================================#
        # ===================BOTTOM FRAME===============================================================#
        buttomFrame = ttk.Frame(self, borderwidth=1, relief='groove')

        # ===================BOTTOM FRAME LEFT===============================================================#
        buttomFrameL = ttk.Frame(self, borderwidth=1, relief='groove')
        btn4 = ttk.Button(buttomFrameL, text='按鈕4')
        btn4.pack(side='top', ipady=30, padx=5, pady=(10, 5))
        btn5 = ttk.Button(buttomFrameL, text='按鈕5')
        btn5.pack(side='top', ipady=10, padx=5, pady=5)
        btn6 = ttk.Button(buttomFrameL, text='按鈕6')
        btn6.pack(side='top', ipady=10, padx=5, pady=(5, 10))
        buttomFrameL.pack(side='left', expand=True, fill='y', padx=10)
        # ===================End BOTTOM FRAME LEFT===============================================================#
        # ===================BOTTOM FRAME CENTER===============================================================#
        buttomFrameC = ttk.Frame(self, borderwidth=1, relief='groove')
        btn7 = ttk.Button(buttomFrameC, text='按鈕7')
        btn7.pack(side='top', ipady=22, padx=(5, 8), pady=(5, 10))
        btn8 = ttk.Button(buttomFrameC, text='按鈕8')
        btn8.pack(side='top', ipady=5, padx=(5, 8), pady=5)
        btn9 = ttk.Button(buttomFrameC, text='b按鈕9')
        btn9.pack(side='top', ipady=25, padx=(5, 8), pady=5)
        buttomFrameC.pack(side='left', expand=True, fill='y', padx=10)
        # ===================End BOTTOM FRAME CENTER===============================================================#
        # ===================BOTTOM FRAME RIGHT===============================================================#
        buttomFrameR = ttk.Frame(self, borderwidth=1, relief='groove')
        btn10 = ttk.Button(buttomFrameR, text='按鈕9')
        btn10.pack(side='top', ipady=15, padx=5, pady=(0, 10))
        btn11 = ttk.Button(buttomFrameR, text='按鈕10')
        btn11.pack(side='top', ipady=15, padx=5, pady=10)
        btn12 = ttk.Button(buttomFrameR, text='按鈕11')
        btn12.pack(side='top', ipady=15, padx=5, pady=10)
        buttomFrameR.pack(side='left', expand=True, fill='y', padx=10)
        # ===================End BOTTOM FRAME Right===============================================================#
        buttomFrame.pack(expand=True, fill='x')
        # ===================End BOTTOM FRAME===============================================================#

    def user_click1(shelf):
        print('hello!button')

    def user_click2(shelf):
        print('hello!button')

    def user_click3(shelf):
        print('hello!button')


def main():
    root = Window(theme='breeze')
    root.mainloop()


if __name__ == '__main__':
    main()

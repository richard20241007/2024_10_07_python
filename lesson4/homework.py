from ttkthemes import ThemedTk
from tkinter import ttk



class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('homework')
        style = ttk.Style(self)
        # ===================TOP FRAME==================================================================#
        topFrame = ttk.Frame(self, borderwidth=1, relief='groove')
        self.btn1 = ttk.Button(topFrame, text="按鈕", command=self.user_click1)
        self.btn1.pack(side='left', expand=True, fill='x', padx=10)
        btn2 = ttk.Button(topFrame, text="按鈕", command=self.user_click2)
        btn2.pack(side='left', expand=True, fill='x')
        btn3 = ttk.Button(topFrame, text="按鈕", command=self.user_click3)
        btn3.pack(side='left', expand=True, fill='x', padx=10)
        topFrame.pack(padx=10, pady=(10, 0), ipadx=10,
                      ipady=10, expand=True, fill='x')
# ==================End TOP FRAME====================================================#
# ===================BOTTOM FRAME====================================================
        bottomFrame = ttk.Frame(self, borderwidth=1,
                                height=2000, relief='groove')
        bottomFrame.pack(padx=10, pady=10, expand=True, fill='x')

        f1 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove')
        f2 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove')
        f3 = ttk.Frame(bottomFrame, borderwidth=3, relief='groove')
        f1.pack(side='left', padx=10, expand=True, fill='both')
        f2.pack(side='left', padx=10, expand=True, fill='both')
        f3.pack(side='left', padx=10, expand=True, fill='both')

        btna4 = ttk.Button(f1, text="按鈕4")
        btna4.pack(fill='x', padx=10, pady=(5, 5), ipady=50)
        btna4.bind('<ButtonRelease>', self.left_button_click)
        btna5 = ttk.Button(f1, text="按鈕5")
        btna5.bind('<ButtonRelease>', self.left_button_click)
        btna5.pack(fill='x', padx=10, pady=(5, 5), ipady=25)
        btna6 = ttk.Button(f1, text="按鈕6")
        btna6.bind('<ButtonRelease>', self.left_button_click)
        btna6.pack(fill='x', padx=10, pady=(5, 5), ipady=25)

        btnb7 = ttk.Button(f2, text="按鈕7")
        btnb7.pack(fill='x', padx=10, pady=(5, 5), ipady=40)
        btnb8 = ttk.Button(f2, text="按鈕8")
        btnb8.pack(fill='x', padx=10, pady=(5, 5), ipady=20)
        btnb9 = ttk.Button(f2, text="按鈕9")
        btnb9.pack(fill='x', padx=10, pady=(5, 5), ipady=40)

        btnc10 = ttk.Button(f3, text="按鈕10")
        btnc10.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)
        btnc11 = ttk.Button(f3, text="按鈕11")
        btnc11.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)
        btnc12 = ttk.Button(f3, text="按鈕12")
        btnc12.pack(fill='x', padx=10, pady=(5, 5), ipady=100/3)
        # ===================End BOTTOM FRAME===============================================================#

    def user_click1(self):
        self.btn1.configure(text='被按了')
        print('hello!button')

    def user_click2(self):
        print('hello!button')

    def user_click3(self):
        print('hello!button')
    
    def left_button_click(self,event):
        print(event.widget.configure(text="被按了"))


def main():
    window = Window(theme="arc")
    window.mainloop()


if __name__ == '__main__':
    main()

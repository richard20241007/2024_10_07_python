import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Window(ThemedTk):
    root = ThemedTk()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TtkThemes_homework")
        self.geometry("600x400")
        

    # 創建頂部的按鈕框架
        style = ttk.Style(self)
        topFrame = ttk.Frame(self, borderwidth=1, relief='groove')
        btn1 = ttk.Button(topFrame, text="按鈕1")
        btn1.pack(side='left', expand=True, fill='x', padx=10)
        btn2 = ttk.Button(topFrame, text="按鈕2")
        btn2.pack(side='left', expand=True, fill='x')
        btn3 = ttk.Button(topFrame, text="按鈕3")
        btn3.pack(side='left', expand=True, fill='x', padx=10)
        topFrame.pack(padx=10, pady=(10, 0), ipadx=10,
                      ipady=10, expand=True, fill='x')
        bottomFrame = ttk.Frame(
            self, width=500, height=300, borderwidth=1, relief='groove')
        bottomFrame.pack(padx=10, pady=10)   
    

    # 創建主框架
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # 在主框架中創建3列
        for i in range(3):
            main_frame.columnconfigure(i, weight=1)
        main_frame.rowconfigure(0, weight=1)

    # 在每列中創建一個框架
        for col in range(3):
            column_frame = ttk.Frame(main_frame, relief="groove", borderwidth=2)
            column_frame.grid(row=0, column=col, sticky="nsew", padx=5)
            column_frame.columnconfigure(0, weight=1)

        # 根據列的不同，設置不同的按鈕大小
        if col == 0:  # 左邊列
            sizes = ["大的", "中等", "中等"]
        elif col == 1:  # 中間列
            sizes = ["大的", "最小的", "大的"]
        else:  # 右邊列
            sizes = ["中等", "中等", "中等"]

        # 在每個列框架中添加按鈕
        for row, size in enumerate(sizes):
            btn = ttk.Button(column_frame, text=size)
            if size == "大的":
                btn.grid(row=row, column=0, sticky="nsew",
                         padx=5, pady=10, ipady=20)
                column_frame.rowconfigure(row, weight=2)
            elif size == "中等":
                btn.grid(row=row, column=0, sticky="nsew",
                         padx=5, pady=5, ipady=10)
                column_frame.rowconfigure(row, weight=1)
            elif size == "最小的":
                btn.grid(row=row, column=0, sticky="nsew",
                         padx=5, pady=2, ipady=2)
                column_frame.rowconfigure(row, weight=1)



def main():
    window = Window(theme="arc")
    window.mainloop()


if __name__ == "__main__":
    main()
    

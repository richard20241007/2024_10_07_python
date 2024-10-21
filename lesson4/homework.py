import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


def Window():
    root = ThemedTk()
    root.title("TtkThemes_homework")
    root.geometry("600x400")

    # =========創建頂部的按鈕框架
    top_frame = ttk.Frame(root)
    top_frame.pack(fill=tk.X, padx=10, pady=10)

    # 設置頂部框架的列權重，使按鈕平均分配空間
    for i in range(3):
        top_frame.columnconfigure(i, weight=1)

    # 創建並放置頂部按鈕
    for i in range(3):
        btn = ttk.Button(top_frame, text=f"按鈕{i+1}")
        btn.grid(row=0, column=i, sticky="ew", padx=5)

    # 創建主框架
    main_frame = ttk.Frame(root)
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

    return root


def main():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()

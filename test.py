import tkinter as tk

# アプリケーションウィンドウを作成する
root = tk.Tk()
root.title("Hello World")

# ラベルを作成する
label = tk.Label(root, text="Hello World")
label.pack()

# アプリケーションウィンドウを表示する
root.mainloop()

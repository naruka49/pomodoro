import tkinter as tk
import time

# ポモドーロタイマーの時間（単位：秒）
POMODORO_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

# ポモドーロのカウント
pomodoro_count = 0

# タイマーを更新する関数
def update_timer(timer, end_time):
    remaining_time = end_time - time.time()
    if remaining_time <= 0:
        timer.config(text="時間です！")
    else:
        minutes, seconds = divmod(int(remaining_time), 60)
        timer.config(text=f"{minutes:02d}:{seconds:02d}")
        timer.after(1000, update_timer, timer, end_time)

# ポモドーロを開始する関数
def start_pomodoro():
    global pomodoro_count
    pomodoro_count += 1
    timer_label.config(text="25:00")
    start_time = time.time()
    end_time = start_time + POMODORO_TIME
    update_timer(timer_label, end_time)
    status_label.config(text=f"ぽもどーろ {pomodoro_count} を開始します。")
    start_button.config(state="disabled")
    short_break_button.config(state="disabled")
    long_break_button.config(state="disabled")
    reset_button.config(state="disabled")
    root.after(POMODORO_TIME * 1000, complete_pomodoro)

# 短い休憩を開始する関数
def start_short_break():
    timer_label.config(text="05:00")
    start_time = time.time()
    end_time = start_time + SHORT_BREAK_TIME
    update_timer(timer_label, end_time)
    status_label.config(text="短い休憩を開始します。")
    start_button.config(state="disabled")
    short_break_button.config(state="disabled")
    long_break_button.config(state="disabled")
    reset_button.config(state="disabled")
    root.after(SHORT_BREAK_TIME * 1000, complete_break)

# 長い休憩を開始する関数
def start_long_break():
    timer_label.config(text="15:00")
    start_time = time.time()
    end_time = start_time + LONG_BREAK_TIME
    update_timer(timer_label, end_time)
    status_label.config(text="長い休憩を開始します。")
    start_button.config(state="disabled")
    short_break_button.config(state="disabled")
    long_break_button.config(state="disabled")
    reset_button.config(state="disabled")
    root.after(LONG_BREAK_TIME * 1000, complete_break)

# ポモドーロを完了する関数
def complete_pomodoro():
    status_label.config(text="ポモドーロが終了しました！")
    start_button.config(state="normal")
    short_break_button.config(state="normal")
    long_break_button.config(state="normal")
    reset_button.config(state="normal")

# 休憩を完了する関数
def complete_break():
    status_label.config(text="休憩が終了しました！")
    short_break_button.config(state="normal")
    long_break_button.config(state="normal")
    reset_button.config(state="normal")
    
# タイマーをリセットする関数
def reset_timer():
    timer_label.config(text="25:00")
    status_label.config(text="")
    start_button.config(state="normal")
    short_break_button.config(state="normal")
    long_break_button.config(state="normal")
    reset_button.config(state="disabled")

#アプリケーションウィンドウを作成する
root = tk.Tk()
root.title("ぽもどーろたいまー")

#タイマーと状態のラベルを作成する
timer_label = tk.Label(root, text="25:00", font=("Arial", 48))
timer_label.pack()
status_label = tk.Label(root, text="", font=("Arial", 18))
status_label.pack()

#ボタンを作成する
start_button = tk.Button(root, text="ポモドーロを開始", command=start_pomodoro)
start_button.pack()
short_break_button = tk.Button(root, text="短い休憩を開始", command=start_short_break)
short_break_button.pack()
long_break_button = tk.Button(root, text="長い休憩を開始", command=start_long_break)
long_break_button.pack()
reset_button = tk.Button(root, text="リセット", command=reset_timer, state="disabled")
reset_button.pack()

#アプリケーションウィンドウを表示する
root.mainloop()
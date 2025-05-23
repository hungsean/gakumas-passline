import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_chart():
    # 讀取 3 個當前值和 3 個參數值
    try:
        values = [float(entry.get()) for entry in entries[:3]]
        params = [float(entry.get()) for entry in entries[3:]]
    except ValueError:
        # 若有非數字輸入，則不更新
        return

    # 找出參數最大值的索引及對應的基準柱高度
    idx_max = params.index(max(params))
    baseline = values[idx_max]

    # 計算每個欄位的及格線高度，確保參數最大者的紅線在柱頂
    thresholds = [baseline * p / params[idx_max] for p in params]

    # 清除舊圖，繪製新柱狀圖
    ax.clear()
    ax.bar(
        [0, 1, 2],
        values,
        color=["#f74992", "#2a90f2", "#feb63c"],
        width=0.6
    )
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["紅", "藍", "橘黃"])

    # 在每個柱上畫紅色虛線，對應計算後的及格線
    for i, h in enumerate(thresholds):
        ax.hlines(
            y=h,
            xmin=i - 0.3,
            xmax=i + 0.3,
            colors="red",
            linestyles="--"
        )

    # 調整 y 軸範圍，留點空白
    ax.set_ylim(0, max(values + thresholds) * 1.1)
    ax.set_ylabel("數值")

    canvas.draw()

# 建立主視窗和介面
root = tk.Tk()
root.title("三欄柱狀圖與及格線")

frame = ttk.Frame(root, padding=10)
frame.pack(side=tk.TOP, fill=tk.X)

labels = ["目前值1", "目前值2", "目前值3", "參數1", "參數2", "參數3"]
entries = []
for i, txt in enumerate(labels):
    ttk.Label(frame, text=txt).grid(row=i, column=0, sticky=tk.W, pady=2)
    e = ttk.Entry(frame, width=15)
    e.grid(row=i, column=1, pady=2)
    entries.append(e)

btn = ttk.Button(root, text="繪製圖表", command=plot_chart)
btn.pack(pady=5)

fig, ax = plt.subplots(figsize=(4, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()

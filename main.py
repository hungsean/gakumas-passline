import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_chart():
    # 讀取上方三個當前值
    try:
        values = [float(entry.get()) for entry in entries[:3]]
        ratios = [float(entry.get()) for entry in entries[3:]]
    except ValueError:
        # 若輸入非數字，直接跳過
        return

    # 計算比例
    total = sum(ratios)
    percents = [r/total for r in ratios]

    # 找出最大比例對應的基準
    idx_max = percents.index(max(percents))
    baseline_value = values[idx_max]

    # 計算每個欄位的及格線高度
    thresholds = [p * baseline_value for p in percents]

    # 清除舊圖，繪製新圖
    ax.clear()
    bars = ax.bar(
        [0, 1, 2],
        values,
        color=["#f74992", "#2a90f2", "#feb63c"],
        width=0.6
    )
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["紅", "藍", "橘黃"])

    # 在每個柱狀圖上畫對應的紅色及格線
    for i, thresh in enumerate(thresholds):
        ax.hlines(
            y=thresh,
            xmin=i - 0.3,
            xmax=i + 0.3,
            colors="red",
            linestyles="--"
        )

    ax.set_ylim(0, max(values + thresholds) * 1.1)
    ax.set_ylabel("數值")

    canvas.draw()

# 建立主視窗
root = tk.Tk()
root.title("三欄柱狀圖與及格線")

# 輸入區塊
frame = ttk.Frame(root, padding=10)
frame.pack(side=tk.TOP, fill=tk.X)

labels = ["目前值1", "目前值2", "目前值3", "參數1", "參數2", "參數3"]
entries = []
for i, text in enumerate(labels):
    ttk.Label(frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=2)
    e = ttk.Entry(frame, width=15)
    e.grid(row=i, column=1, pady=2)
    entries.append(e)

# 按鈕
btn = ttk.Button(root, text="繪製圖表", command=plot_chart)
btn.pack(pady=5)

# Matplotlib 圖表區
fig, ax = plt.subplots(figsize=(4, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Kristen's Course: How to get RICH 101")
window.minsize(width=1200,height=900)

label1 = tk.Label(text="Step 1: WATCH TIKTOK TILL 3AM\n",font=("Comic Sans",30,"bold"))
label2 = tk.Label(text="Step 2: PARTAYYYYYY 💅\n",font=("Comic Sans",30,"bold"))
label3 = tk.Label(text="Step 3: DRINK ON WEEKENDS\n",font=("Comic Sans",30,"bold"))
label3.pack(side='bottom',expand=True)
label1.pack(side='top',expand=True)
label2.pack(side='left',expand=True)

window.mainloop()

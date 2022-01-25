import tkinter as tk

window = tk.Tk() #object that is the root window
window.title('TKInter hello world')

text = tk.Label(text = 'Hello World')
text2 = tk.Label(text = 'Im')
text3 = tk.Label(text = 'Brendan')

text.pack()
text2.pack()
text3.pack()

window.mainloop() #start event loop, method on top of 'window'

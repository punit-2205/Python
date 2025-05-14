import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == '=':
        try:
            result = str(eval(current_text))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == 'C':
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify='right', bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                           command=lambda t=text: on_click(t))
        button.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()       
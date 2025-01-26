import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Position in the options array
    }
]

def generate_question():
    topic = topic_entry.get().strip()
    for q in questions:
        if q["topic"].lower() == topic.lower():
            question_label.config(text=q["question"])
            code_label.config(text=q["code"])
            options_var.set(None)
            for i in range(len(q["options"])):
                options_buttons[i].config(text=q["options"][i], value=i)
            return
    messagebox.showerror("Error", "Topic not found")

def check_answer():
    selected_option = options_var.get()
    correct_answer = questions[0]["answer"]
    if selected_option == correct_answer:
        feedback_label.config(text="Correct! Well done!", fg="green")
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red")

root = tk.Tk()
root.title("Python Quiz Generator")

tk.Label(root, text="Enter Python topic:").pack()
topic_entry = tk.Entry(root)
topic_entry.pack()
tk.Button(root, text="Generate Python Question", command=generate_question).pack()

question_label = tk.Label(root, text="")
question_label.pack()
code_label = tk.Label(root, text="", font=("Courier", 12))
code_label.pack()

options_var = tk.IntVar()
options_buttons = [tk.Radiobutton(root, variable=options_var, value=i) for i in range(4)]
for button in options_buttons:
    button.pack()

tk.Button(root, text="Submit", command=check_answer).pack()
feedback_label = tk.Label(root, text="")
feedback_label.pack()

root.mainloop()



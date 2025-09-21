import tkinter as tk
from tkinter import *

win = tk.Tk()

win.title("BMI, Dosage and Drops Calculator")
win.config(bg="#E0F7FA")
win.geometry("800x600")

def get_result():
    try:
        kg_weight = float(weight_entry.get())
        cm_height = float(height_entry.get())
        m_height = cm_height / 100
        bmi = kg_weight / (m_height * m_height)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        elif 30 <= bmi < 35:
            category = "Obesity I"
        elif 35 <= bmi < 40:
            category = "Obesity II"
        else:
            category = "Obesity III"

        result_label.config(text=f"BMI: {round(bmi,2)} → {category}")

    except ValueError as ve:
        result_label.config(text="⚠️ Please enter numbers only!")
        win.after(2000,lambda: result_label.config(text=""))


for i in range(6):
    win.rowconfigure(i, weight=1)
for j in range(3):
    win.columnconfigure(j, weight=1)


bmi_title = Label(text="BMI calculator",
                  fg="#333333", bg="#E0F7FA",
                  font= ("Montserrat Bold", 20, "bold"),
                  justify="center")

bmi_title.grid(row=0, column=1, pady=30)

weight_label = Label(text="Enter weight (kgs):",
                  fg="#333333", bg="#E0F7FA",
                  font= ("Roboto Regular", 12, "bold"),
                  justify="left")

weight_label.grid(row=1, column =0, columnspan=2)

weight_entry = Entry(font= ("Roboto Regular", 12, "bold"), justify="center", fg="#333333")
weight_entry.grid(row=1, column =1, columnspan=2, pady=5)
weight_entry.focus_set()

height_label = Label(text="Enter Height (cms):",
                  fg="#333333", bg="#E0F7FA",
                  font= ("Roboto Regular", 12, "bold"),
                  justify="left")
height_label.grid(row=2, column =0, columnspan=2, pady=5)

height_entry = Entry(font= ("Roboto Regular", 12, "bold"), justify="center", fg="#333333")
height_entry.grid(row=2, column =1, columnspan=2, pady=5)

convert_button = Button(text= "Calculate", font= ("Roboto Regular", 14, "bold"),
                        justify="center",
                        bg="#0288D1",fg="#333333",command=get_result)
convert_button.grid(row=3,column=1)

result_label = Label(text=" ", fg="#333333", bg="#E0F7FA",
                  font= ("Roboto Regular", 14, "bold"),
                  justify="center")

result_label.grid(row=4, column =1)

win.mainloop()
from tkinter import *
window=Tk()
#create a main parent window.

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    # To convert cm into meter.
    bmi = weight/(height*height)
    print(bmi)
    bmi = round(bmi, 1)
    print(bmi)
    name = username.get()
    
    result_label.destroy()

    msg=""
    
    if bmi < 18.5:
        msg="you areUnderweight"
    elif bmi > 18.5 and bmi <=24.9:
      msg="is in Normal Range"
    elif bmi > 25 and bmi <=29.9:
      msg="you are Overweight"
    elif bmi > 30:
      msg="you are Obese"
    else:
      msg="Something Went Wrong"
    
    output_message=Label(result_frame,text=name+", your BMI is "+str(bmi)+" and "+msg, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

window.title('BMI Calculator')
window.geometry("400x600")
window.configure(bg='lightcyan')

app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Enter Height(cm)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=10)
height_label.place(x=11, y=140)

height_entry=Entry(window, text="", bd=5, width=22)
height_entry.place(x=150,y=142)

weight_label=Label(window, text="Enter weight(kg)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=15)
weight_label.place(x=8,y=185)

weight_entry=Entry(window, text="", bd=5, width=22)
weight_entry.place(x=150,y=187)

calculate_button=Button(window, text="Calculate", fg="black", bg="white", bd=20,command=calculate_bmi)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "black", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=350)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time
from plyer import notification
#function to open bp_monitor window
def open_bp_monitor():
    #this defines new window , write/insert all the buttons aor labels or any aothe bunctionin this window
    # Labels and Buttons in the new window
    class BloodPressureMonitor:
     def __init__(self, root):
        self.root = root
        self.root.title("Blood Pressure Monitor")

        self.age_var = tk.IntVar(master=root)
        self.systolic_var = tk.DoubleVar(master=root)
        self.diastolic_var = tk.DoubleVar(master=root)
        self.fitness_var = tk.StringVar(master=root)

        tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Systolic BP:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Diastolic BP:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Fitness Level:").grid(row=3, column=0, padx=10, pady=5)

        tk.Entry(root, textvariable=self.age_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.systolic_var).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.diastolic_var).grid(row=2, column=1, padx=10, pady=5)

        fitness_levels = ["Low", "Moderate", "High"]
        ttk.Combobox(root, values=fitness_levels, textvariable=self.fitness_var).grid(row=3, column=1, padx=10, pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Classify", command=self.classify_bp).grid(row=5, column=0, columnspan=2, pady=10)

     def classify_bp(self):
        age = self.age_var.get()
        systolic_bp = self.systolic_var.get()
        diastolic_bp = self.diastolic_var.get()
        fitness_level = self.fitness_var.get()

        if age < 40:
            if fitness_level == "low":
                status = "Normal"
            else:
                status = "Elevated"
        else:
            if 120 <= systolic_bp <= 129 and diastolic_bp < 80:
                status = "Elevated"
            elif 130 <= systolic_bp <= 139 or 80 <= diastolic_bp <= 89:
                status = "Stage 1 Hypertension"
            elif systolic_bp >= 140 or diastolic_bp >= 90:
                status = "Stage 2 Hypertension"
            else:
                status = "Normal"

        result_text = f"Classification: {status}"
        self.result_label.config(text=result_text)

    if __name__ == "__main__":
     root = tk.Tk()
     app = BloodPressureMonitor(root)
     root.mainloop()




#function to open heart_monitor window
def open_sugar_analyse():

    class SugarLevelAnalyzer:
        def __init__(self, root):
            self.root = root
            self.root.title("Sugar Level Analyzer")

            self.fasting_var = DoubleVar(master=root)
            self.post_prandial_var = DoubleVar(master=root)
            self.result_var = StringVar(master=root)

            Label(root, text="Fasting Sugar Level (mg/dL):").grid(row=0, column=0, padx=10, pady=5)
            Label(root, text="Post-Prandial Sugar Level (mg/dL):").grid(row=1, column=0, padx=10, pady=5)

            Entry(root, textvariable=self.fasting_var).grid(row=0, column=1, padx=10, pady=5)
            Entry(root, textvariable=self.post_prandial_var).grid(row=1, column=1, padx=10, pady=5)

            self.result_label = Label(root, textvariable=self.result_var)
            self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

            Button(root, text="Analyze", command=self.analyze_sugar_levels).grid(row=3, column=0, columnspan=2, pady=10)

        def analyze_sugar_levels(self):
            fasting_level = self.fasting_var.get()
            post_prandial_level = self.post_prandial_var.get()

            if fasting_level < 100 and post_prandial_level < 140:
                result = "Normal"
            elif 100 <= fasting_level < 126 or 140 <= post_prandial_level < 200:
                result = "Pre-Diabetes"
            else:
                result = "Diabetes"

            result_text = f"Analysis Result: {result}"
            self.result_var.set(result_text)

    if __name__ == "__main__":
        root = Tk()
        app = SugarLevelAnalyzer(root)
        root.mainloop()



def open_bmi_calculation():
    
    def calculate_bmi():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get()) / 100  # Convert height to meters

            bmi = weight / (height ** 2)
            result_label.config(text=f"BMI: {bmi:.2f}")

            if bmi < 18.5:
                status_label.config(text="UNDERWEIGHT",fg="#ebcf34")
            elif bmi>18.5 and bmi<24.9:
                status_label.config(text="YOU ARE FIT",fg="green")
            elif bmi>=25 and bmi<=29.9:
                status_label.config(text="YOU ARE OVERWEIGHT",fg="blue")
            else:
                status_label.config(text="OBESE",fg="red")
        except ValueError:
            result_label.config(text="Invalid input. Please enter valid numbers.")
            status_label.config(text="")

    # Create main root
    root = Tk()
    root.title("BMI Calculator")
    root.config(bg="#393040")
    root.title("BODY MASS INDEX")
    root.geometry("1080x678")

    bg = PhotoImage(master=root,file = "bmi_image.png") 
    background_label = Label(root, image=bg)
    background_label.place(x = 0, y = 0) 


    # Create widgets
    main=Label(root,text="BODY MASS INDEX CALCULATOR",bg="#7bc25d",width=120,padx=3,font=("Arial",30),fg="red",)
    main.pack()
    height_label = Label(root, text="ENTER HEIGHT (in cm):",fg="blue",width=29,height=1,bg="#6c9c44",font="Bold",pady=10) 
    height_label.pack()
    height_entry = Entry(root,width=29,fg="#0733f5",bg="#a7c3c9",text="enter the ",font=("Bold,35"))
    height_entry.insert(0,"")
    height_entry.pack(pady=20)

    weight_label = Label(root, text="ENTER WEIGHT (in kg):",width=29,fg="Blue",bg="#6c9c44",font="Bold")
    weight_label.pack(pady=10)

    weight_entry = Entry(root,width=29,fg="#0733f5",bg="#a7c3c9",font=("Bold,35"))
    weight_entry.insert(0,"")
    weight_entry.pack(pady=10)

    calculate_button = Button(root, text="ENTER", command=calculate_bmi,width=20,bg="Crimson",)
    calculate_button.pack(pady=20)

    result_label = Label(root, text="",bg="white",fg="#c9165e",width=20,font=("Arial",26))
    result_label.pack()
            
    status_label = Label(root, text="", font=("Helvetica", 24, "bold"),bg="#FFFFFF")
    status_label.pack()
    main.pack()

    # Run the main loop
    root.mainloop()

def open_calorie_burn():
    
    def count_cals():
        try:
            gender=str(gender1.get())
            age=int(age1.get())
            weight=float(weight1.get())
            heart_rate=int(heart_rate1.get())
            time=float(time1.get())
        except:
            output = "PLEASE ENTER VALID INPUTS"
        else:
            if gender=="male" and age>0 and weight>0 and heart_rate>0:
                calories=round(abs(((age*0.2017)+(weight*0.09036)+(heart_rate*0.6309)-(55.0969*time))/4.184),2)
                output=("Calories burnt is " + str(calories))
            elif gender=="female" and age>0 and weight>0 and heart_rate>0:
                calories=round(abs(((age*0.074)+(weight*0.05741)+(heart_rate*0.4472)-(20.4022*time))/4.184),2)
                output=("Calories burnt is " + str(calories))
            else:
                output=("INVALID INPUTS ENETERED")

        label.config(text=output)
        return output


    window1=Tk()
    window1.title("__Calorie_Calculator__")
    window1.geometry("910x633")

    bg = PhotoImage(master=window1,file ="bg1.png")
    label1 = Label( window1, image = bg) 
    label1.place(x = 0, y = 0) 

    Label(window1, text='Select gender: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB",fg='black').grid(row=1, padx=10, pady=10)
    gender1 = StringVar(master=window1)
    gender1.set(False)
    Radiobutton(window1, text = "Male", variable = gender1, value = "male",bg="#E1E6EB",fg='black').grid(row=1,column=2,sticky=W)
    Radiobutton(window1, text = "Female", variable = gender1, value = "female",bg="#E1E6EB",fg='black').grid(row =2,column=2,sticky=W)
    # gender1 = Entry(window1, width=40)
    # gender1.grid(row=1,column=2)
    Label(window1, text='Enter age: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB",fg='black').grid(row=3, padx=10, pady=5)
    age1 = Entry(window1, width=40,bg="#E1E6EB",fg='black')
    age1.grid(row=3,column=2)
    Label(window1,text='Enter weight:',height=1,font=('Times',13),relief="flat",bg="#E1E6EB",fg='black').grid(row=4, padx=10, pady=5)
    weight1= Entry(window1, width=40,bg="#E1E6EB",fg='black')
    weight1.grid(row=4,column=2)
    Label(window1, text='Enter heart rate: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB",fg='black').grid(row=5, padx=10, pady=5)
    heart_rate1= Entry(window1, width=40,bg="#E1E6EB",fg='black')
    heart_rate1.grid(row=5,column=2)
    Label(window1, text='Enter time in minutes only: ',height=1,font=('Times',13),relief="flat",bg="#E1E6EB",fg='black').grid(row=6, padx=10, pady=5)
    time1= Entry(window1, width=40,bg="#E1E6EB",fg='black')
    time1.grid(row=6,column=2)

    label=Label(window1, text="", font=('Comic Sans MS',15),bg="#DCE1E6",fg='black')
    label.grid(row=9,column=0,columnspan=3,sticky=NSEW, padx=5, pady=10)

    Button(window1, text="Calculate calories", command=count_cals, height=1,font=('Comic Sans MS',13)).grid(row=7,column=2,sticky=NS, padx=2, pady=5)

    window1.mainloop()

def open_water_alarm():

    def water_alarm():
        duration = int(duration1.get())
        minute= float(minutes.get())
        while duration:   
            time.sleep(60*minute)
            notification.notify(title='Drink water', message="It's time to drink water")
            duration-=1
        return

    window2=Tk()
    window2.title("__Water_Alarm__")
    window2.geometry("750x300")

    bg = PhotoImage(master=window2,file ="bg2.png")
    label1 = Label( window2, image = bg) 
    label1.place(x = 0, y = 0) 

    Label(window2, text='Enter the number of times you want to be reminded in a day: ',height=1,font=('Comic Sans MS',11,'bold'),relief="flat",bg="#00A2E8",fg="#FFFFFF").grid(row=1, padx=10, pady=5)
    duration1 = Entry(window2, width=10,bg='white',fg='black')
    duration1.grid(row=1,column=2)
    Label(window2, text='Enter once in how many minutes you want to be reminded: ',height=1,font=('Comic Sans MS',11,'bold'),relief="flat",bg="#00A2E8",fg="#FFFFFF").grid(row=2, padx=10, pady=5)
    minutes = Entry(window2, width=10,bg='white',fg='black')
    minutes.grid(row=2,column=2)

    Button(window2, text="Set Reminder", command=water_alarm, height=1,font=('Comic Sans MS',13),relief="ridge",bg="#FFFFFF",fg="#00A2E8").grid(row=1,rowspan=2,column=3,sticky=NS, padx=50, pady=5)

    window2.mainloop()

def pulse_rate_monitor():
    win=Tk()
    win.config()
    win.title("heart rate assessment")
    #win.iconbitmap('c:/Users/communicate/Downloads/heart01.ico')
    win.geometry("300x300")
    win.resizable(False, False)
    win.attributes("-alpha",0.9)

    Label(win,text="HEART RATE ASSESMENT",fg="white").pack()

    frame=Frame(win,)
    frame.pack(side=TOP)


    L1=Label(frame,text="Enter resting heart rate(bpm)",fg="white")
    L1.pack()
    Heart=Entry(frame,width="20")
    Heart.pack()

    Label(frame,text="enter age",fg="white")
    options=[
        ("less than 4 weeks",1),
        ("less than a year",2),
        ("1-3 years",3),
        ("3-5 years",4),
        ("5-12 years",5),
        ("13-18 years",6),
        ("18+ years",7)
        ]

    assess=IntVar(master=win)
    assess.set(1)
    for text,mode in options:
        Radiobutton(frame,text=text,fg="white",variable=assess,value=mode).pack(anchor='w')



    def calculate(a,b):
        try:
            g=int(a)
        except Exception:
            messagebox.showerror("Error","Invalid Heart Rate")
        if b==1:
            if g<100:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>205:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==2:
            if g<100:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>180:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==3:
            if g<98:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>140:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==4:
            if g<80:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>120:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==5:
            if g<75:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>118:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==6:
            if g<60:
                messagebox.showinfo("Result","abnormally low heart rate")
            elif g>100:
                messagebox.showinfo("Result","abnormally high heart rate")
            else:
                messagebox.showinfo("Result","Normal heart rate")
        if b==7:
            if g<60:
                messagebox.showinfo("Result","Bradycardia-low")
            elif g>100:
                messagebox.showinfo("Result","Tachycardia-high")
            else:
                messagebox.showinfo("Result","Normal heart rate")
                Target=Toplevel(master=win)
                Target.title("Target Heart Rate")
                Target.geometry("300x200")
                Target.resizable("False","False")
                Label(Target,text="TARGET EXERCISE HEART RATE(bpm)").pack()
                Label(Target,text="Enter Age(18+)").pack()
                Age=Entry(Target)
                Age.pack()
                var = StringVar(master=win)
                Label(Target,textvariable=var).pack()
                Button(Target,text="submit",command=lambda: Target_Rate(Age.get(),var)).pack()
        def Target_Rate(x,p):
            try:
                y=int(x)
            except Exception:
                messagebox.showerror("Error","Invalid Age")
            if y<18:
                messagebox.showerror("Error","Invalid Age")
            elif 18<=y<=20:
                p.set("120bpm-160bpm")
            elif 20<y<=25:
                p.set("117bpm-156bpm")
            elif 25<y<=30:
                p.set("114bpm-152bpm")
            elif 30<y<=35:
                p.set("111bpm-148bpm")
            elif 35<y<=40:
                p.set("108bpm-144bpm")
            elif 40<y<=45:
                p.set("105bpm-140bpm")
            elif 45<y<=50:
                p.set("102bpm-136bpm")
            elif 50<y<=55:
                p.set("99bpm-132bpm")
            elif 55<y<=60:
                p.set("96bpm-128bpm")
            elif 60<y<=65:
                p.set("93bpm-124bpm")
            elif 65<y<=70:
                p.set("90bpm-120bpm")
            elif 70<y<=75:
                p.set("87bpm-116bpm")
            elif 75<y<=80:
                p.set("84bpm-112bpm")
            elif 80<y<=85:
                p.set("81bpm-108bpm")
            elif 85<y<=90:
                p.set("78bpm-104bpm")
            elif 90<y<=95:
                p.set("75bpm-100bpm")
            elif 95<y<=100:
                p.set("72bpm-96bpm")
            else:
                messagebox.showerror("Error","Age is out of range")
                
                
    output=Button(win,text="submit",fg="black",command=lambda: calculate(Heart.get(),assess.get()))
    output.pack()

    win.mainloop()

#this is Main window
root = Tk()
root.title("FITIUM")
window_width=500
window_height=332
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x_position=(screen_width-window_width)//2
y_position=(screen_height-window_width)//2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

bgimg = PhotoImage(master=root,file ="fitium.png")
label1 = Label( root, image = bgimg) 
label1.place(x = 0, y = 0) 

# Button to open a bp window
button_open_bp = Button(root, text="Blood Pressure Monitoring System", command=open_bp_monitor)
button_open_bp.grid(row=2,column=8,padx=250,pady=5)

# Button to open a heart rate window
button_open_heart = Button(root, text="Sugar Level Analysis", command=open_sugar_analyse)
button_open_heart.grid(row=3,column=8,padx=275,pady=5)

button_open_heart = Button(root, text="BMI Calculation", command=open_bmi_calculation)
button_open_heart.grid(row=4,column=8,padx=275,pady=5)

button_open_heart = Button(root, text="Calorie Burn Estimation", command=open_calorie_burn)
button_open_heart.grid(row=5,column=8,padx=275,pady=5)

button_open_heart = Button(root, text="Drink Water Alarm", command=open_water_alarm)
button_open_heart.grid(row=6,column=8,padx=275,pady=5)

button_open_heart = Button(root, text="Pulse Rate Monitor", command=pulse_rate_monitor)
button_open_heart.grid(row=7,column=8,padx=275,pady=5)

root.mainloop()

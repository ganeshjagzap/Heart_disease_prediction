from tkinter import *
import numpy as np
import pandas as pd
import joblib

# define functions

def inputlist():


    Show()
    disp = Tk()

    disp.title("output screen")
    disp.geometry("932x532")
    disp.maxsize(932, 532)
    disp.minsize(932, 532)
    disp.config(bg="ghost white")

    age = Ageval1.get()
    gender0 = sexVal1.get()
    gender1=1
    if (gender0 == 'Female'):
        gender1 = 1
    elif (gender0 == 'Male'):
        gender1 = 0
    l1 = [ age, gender1, Cpval1.get(), trestbpsval1.get(), cholval1.get(), FBSval1.get(), restecgval1.get(), thalachval1.get(), exangval1.get(), oldpeakval1.get(), slopeval1.get(), caval1.get(), thalval1.get()]

    # emptylabel = Label(disp, fg="green", bg="pink", padx=1232, pady=732).grid(row=0, column=0)
    print("Submitting form")
    print(
        f"{age, gender1, Cpval1.get(), trestbpsval1.get(), cholval1.get(), FBSval1.get(), restecgval1.get(), thalachval1.get(), exangval1.get(), oldpeakval1.get(), slopeval1.get(), caval1.get(), thalval1.get()}")

    global pickle_prediction

    x= StringVar()

    with open('heartmodel', 'rb') as f:
        loaded_model = joblib.load(f)
    predictionarray = np.asarray(l1)

    input_data_reshape = predictionarray.reshape(1, -1)
    pickle_prediction = loaded_model.predict(input_data_reshape)
    for i in pickle_prediction:
        x=i
    print(x)
    if (x==1):
        finalheartprediction="You have heart disease"
    elif(x==0):
        finalheartprediction="You don't have heart disease"
    # l3=Entry(disp,textvariable=pickle_prediction_val).place(x=400,y=400)

    def PrintOutput():

        emptylable = Label(disp, fg="green", bg="seashell2", font="time 25 italic", padx=200, pady=40)
        emptylable.config(text=f"Result : {finalheartprediction}")
        emptylable.place(x=0,y=100)


    pdata=Button(disp,text="Check",font="Arial 20 bold",fg="white",bg="black",padx=20,pady=20,borderwidth=10,command=PrintOutput).place(x=360,y=300)
    note = Label(disp, text="Note : This model is 98% accurate",
                 font="time 20 bold italic", fg="blue",bg="seashell2").place(x=200, y=460)


def Show():

    age = Ageval1.get()
    gender0 = sexVal1.get()
    gender1=1
    if (gender0 == 'Female'):
        gender1 = 1
    elif (gender0 == 'Male'):
        gender1 = 0
    l1 = [ age, gender1, Cpval1.get(), trestbpsval1.get(), cholval1.get(), FBSval1.get(), restecgval1.get(), thalachval1.get(), exangval1.get(), oldpeakval1.get(), slopeval1.get(), caval1.get(), thalval1.get()
]
    name=[nameval.get()]
    age1=[age]
    gender2=[gender1]
    cp=[Cpval1.get()]
    restbps=[trestbpsval1.get()]
    cholestrol=[cholval1.get()]
    fbs=[FBSval1.get()]
    restecg=[restecgval1.get()]
    thalach=[thalachval1.get()]
    exangval=[exangval1.get()]
    oldpeak=[oldpeakval1.get()]
    slope=[slopeval1.get()]
    ca=[caval1.get()]
    thalach=[thalachval1.get()]



    dict={"name":name,"age":age,"sex":gender2,"cp":cp,"trestbps":restbps,"chol":cholestrol,"fbs":fbs,"restecg":restecg,"thalach":thalach,"exang":exangval,"oldpeak":oldpeak,"slope":slope,"ca":ca,"thal":thalach}
    df=pd.DataFrame(dict)
    # df.to_csv("D:\\Learning only\\patientdatabase.csv")
    with open("patientdatabase.csv",'a') as f:
        df.to_csv(f,mode='a',index=False,header=False)




    print("Submitting form")
    print(
        f"{ age, gender1, Cpval1.get(), trestbpsval1.get(), cholval1.get(), FBSval1.get(), restecgval1.get(), thalachval1.get(), exangval1.get(), oldpeakval1.get(), slopeval1.get(), caval1.get(), thalval1.get()}")

    global pickle_prediction
    pickle_prediction=StringVar()



    with open('heartmodel', 'rb') as f:
        loaded_model = joblib.load(f)
    predictionarray = np.asarray(l1)

    input_data_reshape = predictionarray.reshape(1, -1)
    pickle_prediction = loaded_model.predict(input_data_reshape)





def predict1():
    root.destroy()
    global pred
    pred = Tk()
    pred.title("Heart Disease prediction model by Prathamesh and Ganesh ")

    pred.config(bg="ghost white")

    pred.geometry("1232x732")
    pred.maxsize(1232, 732)
    pred.minsize(1232, 732)
    lable1=Label(text="Heart disease prediction model",font="time 20 bold",fg="green",bg="ghost white").place(x=380,y=20)
    name = Label(pred, text="Name", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=100)
    Age = Label(pred, text="age", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=100)
    height = Label(pred, text="Height", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=150)
    weight = Label(pred, text="Weight", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=200)
    sex = Label(pred, text="Gender", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=150)
    cp_type = Label(pred, text="Chest pain type", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=200)
    Resting_BP = Label(pred, text="trestbps", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=250)
    SC = Label(pred, text="Serum Cholesterol", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=250)
    FBS = Label(pred, text="Fasting Blood Sugar", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=300)
    RER = Label(pred, text="Resting ECG Results", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=300)
    MHR = Label(pred, text="thalach", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=350)
    EIA = Label(pred, text="exang", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=350)
    ST_d = Label(pred, text="oldpeak", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=400)
    SPE = Label(pred, text="Slop", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=400)
    NMV = Label(pred, text="ca", font="time 12 bold", fg="black", bg="ghost white").place(x=200,y=450)
    Thalassemia = Label(pred, text="Thalassemia", font="time 12 bold", fg="black", bg="ghost white").place(x=650,y=450)


    global Ageval1, sexVal1, Cpval1, trestbpsval1, cholval1, FBSval1, restecgval1, thalachval1, exangval1, oldpeakval1, slopeval1, caval1, thalval1, nameval

    nameval = StringVar()
    heightval = StringVar()
    weightval = StringVar()
    Ageval1 = IntVar()
    sexVal1 = StringVar()
    Cpval1 = IntVar()
    trestbpsval1 = IntVar()
    cholval1 = IntVar()
    FBSval1 = IntVar()
    restecgval1 =IntVar()
    thalachval1 = IntVar()
    exangval1 = IntVar()
    oldpeakval1 = IntVar()
    slopeval1 = IntVar()
    caval1 = IntVar()
    thalval1 = IntVar()
    sextype = {"Male ", "Female"}
    nameentry = Entry(pred, textvariable=nameval).place(x=400,y=100)
    entry1 = Entry(pred, textvariable=Ageval1).place(x=850,y=100)
    entry2 = Radiobutton(pred, text="Female", variable=sexVal1, value="Female", font="time 8 bold", fg="black",
                         bg="seashell2").place(x=400,y=150)
    entry21 = Radiobutton(pred, text="Male", variable=sexVal1, value="Male", font="time 8 bold", fg="black",
                          bg="seashell2").place(x=470,y=150)
    heightentry = Entry(pred, textvariable=heightval, font="time 8 bold").place(x=850,y=150)
    entry3 = Entry(pred, textvariable=Cpval1).place(x=400,y=200)
    weightentry = Entry(pred, textvariable=weightval).place(x=850,y=200)
    entry4 = Entry(pred, textvariable=trestbpsval1).place(x=400,y=250)
    entry5 = Entry(pred, textvariable=cholval1).place(x=850,y=250)
    entry6 = Entry(pred, textvariable=FBSval1).place(x=400,y=300)
    entry7 = Entry(pred, textvariable=restecgval1).place(x=850,y=300)
    entry8 = Entry(pred, textvariable=thalachval1).place(x=400,y=350)
    entry9 = Entry(pred, textvariable=exangval1).place(x=850,y=350)
    entry10 = Entry(pred, textvariable=oldpeakval1).place(x=400,y=400)
    entry11 = Entry(pred, textvariable=slopeval1).place(x=850,y=400)
    entry12 = Entry(pred, textvariable=caval1).place(x=400,y=450)
    entry13 = Entry(pred, textvariable=thalval1).place(x=850,y=450)

    show = Button(pred, text="Next", font="time 20 bold", padx=60, pady=20, fg="red", bg="black", borderwidth=10,command=inputlist).place(x=480,y=550)
root = Tk()

# define  window size
root.geometry("1232x732")
root.maxsize(1232, 732)
root.minsize(1232, 732)

root.config(bg="ghost white")

root.title("Heart Disease prediction model by Prathamesh and Ganesh")

# labeling

l1 = Label(root, text="Welcome to disease prediction model", fg="maroon", bg="ghost white", font="comicsansns 40 bold").place(x=140,y=150)
b2 = Button(root, text="User registration", font="time 20 bold", fg="ghost white", bg="lightsteelblue4", padx=20, pady=20,
            command=predict1, borderwidth=13).place(x=460,y=300)
#

root.mainloop()
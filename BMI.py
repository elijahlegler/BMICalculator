#import TK
from tkinter import *

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("BMI Calculator")
        #creating labels, text boxes, and buttons oh my
        self.lblHeight = Label(self, text = "HEIGHT")
        self.lblHeight.grid(row = 0,columnspan = 4)
        
        self.lblFeet = Label(self, text = "Feet:")
        self.lblFeet.grid(row = 1, column = 1, sticky = W)
        
        self.txtFeet = Entry(self)
        self.txtFeet.grid(row = 1, column = 2)

        self.lblInches = Label(self, text = "Inches:")
        self.lblInches.grid(row = 2, column = 1, sticky = W)

        self.txtInches = Entry(self)
        self.txtInches.grid(row = 2, column = 2)
        
        self.lblWeight = Label(self, text = "WEIGHT")
        self.lblWeight.grid(row = 3, columnspan = 4)

        self.lblPounds = Label(self, text = "Pounds:")
        self.lblPounds.grid(row = 4, column = 1, sticky = W)

        self.txtPounds = Entry(self)
        self.txtPounds.grid(row = 4, column = 2)

        self.btnCalculate = Button(self, text = "Calculate", command = self.Calculate)
        self.btnCalculate.grid(row = 5, columnspan = 4)

        self.lblBodyMassIndex = Label(self, text = "BMI:")
        self.lblBodyMassIndex.grid(row = 6, column = 1, sticky = W)

        self.lblbmiOutput = Label(self, text = " ")
        self.lblbmiOutput.grid(row = 6, column = 2)

        self.lblJudgment = Label(self, text = "Generally, you are:")
        self.lblJudgment.grid(row = 7, column = 1)

        self.lblCategory = Label(self, text = " ")
        self.lblCategory.grid(row =7, column = 2)
    
        self.mainloop()

    def setHeight(self):
        x = int(self.txtFeet.get())
        #setting feet to 5 if user inputs invalid text
        if x <= 0:
            self.txtFeet = 5
        x = int(self.txtFeet.get())
        y = int(self.txtInches.get())
        #calculating height in inches
        height = (x * 12) + y
        return height
        
    def setWeight(self):
        #setting weight to 150 if user input invalid text
        if int(self.txtPounds.get()) <= 0:
            self.txtPounds = 150
            self.txtPounds["text"] = "150"
        weight = self.txtPounds.get()
        return weight
    
    def Calculate(self):
        height = int(self.setHeight())
        weight = int(self.setWeight())
        #calculates and outputs BMI
        bmi = round(((weight/(height * height)) * 703), 1)
        BMIcategory = self.lblbmiOutput["text"] = "{}".format(bmi)
        #determine which category to output
        if float(BMIcategory) <= 18.5:
            self.lblCategory["text"] = "Underweight"
        elif float(BMIcategory) >18.5 and float(BMIcategory) <= 25:
            self.lblCategory["text"] = "Normal"
        elif float(BMIcategory) >25.0 and float(BMIcategory) <= 29.9:
            self.lblCategory["text"] = "Overweight"
        elif float(BMIcategory) >30.0 and float(BMIcategory) <= 34.9:
            self.lblCategory["text"] = "Obese"
            
        
def main():
    a = app()

if __name__ == '__main__':
    main()



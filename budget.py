#Budget project by Malay Patel

# all the necessary libraries imported
import os
from datetime import datetime
import math
import time as t
from pathlib import Path
from tkinter import *
import matplotlib.pyplot as plot
import pandas as pd

# main class where every function is held
class MyBudegt:

    main_list=[] # all data goes here
    expense_details = {"date":"", "amount":00, "category":"", "type":""} # divides data accordingly

    def __init__(self, path, fileName = None):
        if fileName != None:
            self.path = path
            self.fileName = fileName
        elif fileName == None:
            self.path = path
            self.fileName = None

    # creates new file
    def FileCreator(self):
        full_path =  os.path.join(self.path, self.fileName)

        y = open(full_path,"x")
        y.write(f"{self.fileName} Month \n\n")
        y.write("Date       |Amt |Type  |In/Out/Invest/Savings   \n")
        y.write("-" * 50 + "\n")
        t.sleep(1.1)
        y.close()

    # adds new transaction in the created file and calls DataBase
    def TransactionAdder(self):
        x = open(self.fileName, "a")

        format = "%d-%m-%Y"
        check = True
        date_input = input("(dd-mm-yyyy) Date: ") # date input

        if check == bool(datetime.strptime(date_input, format)): # checks date format
            MyBudegt.expense_details['date'] = date_input
            print("Date added to list successfully.")
        else:
            print("Wrong date format.")

        amt_input = float(input("Amount: ")) # amount input
        MyBudegt.expense_details['amount'] = amt_input
        print("Amount added to list successfully.")

        cate_input = input("Category/Type: ").capitalize() # category input
        MyBudegt.expense_details['category'] = cate_input
        print("Category added to list successfully.")

        descr_input = input("Type(In/Out/Invest/Savings): ").capitalize() # type input
        MyBudegt.expense_details['type'] = descr_input
        print("Details added to list successfully.")

        MyBudegt.main_list.append(MyBudegt.expense_details) # expense_details appended to main_list
        print("List has been updated")
        print("Now printing in external file....")
        t.sleep(1.1)

        x.write(f"{MyBudegt.expense_details['date']} | ${MyBudegt.expense_details['amount']} | {MyBudegt.expense_details['category']} | {MyBudegt.expense_details['type']} \n")
        x.close()

        self.DataBase() # calls DataBase function

    # deletes the given files
    def FileRemover(self):
        
        file_type = input("Which file would you like to remove(Data or Main): ").capitalize() 
        file_name = input("Name the file: ").capitalize()
        
        match file_type:
        
            case "Data": # case for data file
                full_path = self.path+"\\data_"+file_name
                if os.path.exists(full_path):
                    os.remove(full_path)
                    t.sleep(1.1)
                    print(f"File '{file_name}' has been removed successfully.")
                else:
                    print(f"File '{file_name}' not found.")

            case "Main": # case for main file
                full_path = self.path+"\\"+file_name
                if os.path.exists(full_path):
                    os.remove(full_path)
                    t.sleep(1.1)
                    print(f"File '{file_name}' has been removed successfully.")
                else:
                    print(f"File '{file_name}' not found.")

    # used to see the data from Main file in terminal
    def DataViewer(self):
        with open(self.path+"\\"+self.fileName) as k:
            lines = k.readlines()
            for line in lines:
                print(line)

    # Creates new database file to store data in data_file
    def DataBase(self):
        data_fileName = "data_"+self.fileName
        full_dataPath = Path(os.path.join(self.path, data_fileName))

        if full_dataPath.exists():
            z = open(full_dataPath, "a")
            z.write(f"${MyBudegt.expense_details['amount']} - {MyBudegt.expense_details['type']}\n")
            z.close()
        else:
            z = open(full_dataPath, "x")
            z.write(f"{self.fileName} DataBase \n")
            z.write(f"${MyBudegt.expense_details['amount']} - {MyBudegt.expense_details['type']}\n")
            z.close()

    # Function to calculate all the required data for DataStats function
    def DataCalc(self):
        #part-1 :- extracts data from the data_file, filters and stores in dictionary 
        num_array = []
        status_array = []
        m = open(self.path+"\\data_"+self.fileName)
        lines = m.readlines()
        for line in lines:
            if '$' in line.strip():
                split_list= line.split()
                status_array.append(split_list[2])
                num_array.append(split_list[0])
        filterednum_array = [float(element[1:]) for element in num_array]
        pair_dict = dict(zip(filterednum_array,status_array))

        #part-2 :- divides data into 4 categories
        self.income = 0
        self.expenses = 0
        self.investment = 0
        self.savings = 0
        for keys,values in pair_dict.items():
            if values == 'In':
                self.income += keys
            elif values == 'Out':
                self.expenses += keys
            elif values == 'Invest':
                self.investment += keys
            elif values == 'Savings':
                self.savings += keys
        self.cash_flow = self.income - self.expenses

        #part-3 :- gives a ratio
        self.expense_ratio = round(((self.expenses/self.income)*100),2)

        #part-4 :- estimates input from user
        self.estimated_expenses = int(input("What is your estimated expenses for this month:-  "))
        self.estimated_income = int(input("What is your estimated income for this month:-  "))
        self.diff_expense = self.estimated_expenses - self.expenses
        self.diff_income = self.income - self.estimated_income

        #part-5 savings,expenses,income,investment
        self.fixed_investment = 200.0
        self.estimated_savings = float(input("What is your estimated savings target: "))    
    
    # display all the calculated stats in terminal
    def DataStats(self):
        self.DataCalc()

        # part-2
        print(f"Your total income until now for this month is ${self.income}.")  
        print(f"Your total expenses until now for this month is ${self.expenses}.")
        print(f"Thus your cash-flow is ${self.cash_flow}.")
        t.sleep(1.1)

        #part-3
        if self.cash_flow <= 0:
            print("Expenses are higher and Income is less")
        elif self.cash_flow > 0 and self.cash_flow <= 100:
            print("Case-1: Expenses are higher and Income is stable or comparatively less.")
            print("Case-2: Expenses are similar or comparatively less and Income is less.")
        elif self.cash_flow > 100 and self.cash_flow <= 500:
            print("Case-1: Income is stable. But Expenses are more.")
            print("Case-2: Expenses are stable. But Income is less.")
        else:
            print("The Expenses are less and Income is good enough.")
        t.sleep(1.1)

        #part-4
        print("Calculating your expense ratio...")
        print(f"You spent {self.expense_ratio}% of your income.")
        t.sleep(1.1)

        #part-5
        print(f"Expenses Estimates --> ${self.estimated_expenses}")
        print(f"Actual Expenses --> ${self.expenses}")
        if self.diff_expense > 0:
            print(f"Your expenses are less compared to your estimateds. You still have a gap of ${self.diff_expense} to your estimateds.")
        elif self.diff_expense < 0:
            print(f"Your expenses are higher this month than your estimates. Higher by ${self.diff_expense}")
        elif self.diff_expense == 0:
            print(f"Your expenses are exact as you estimated. The difference is ${self.diff_expense}")

        print(f"Income Estimates --> ${self.estimated_income}")
        print(f"Actual Income --> ${self.income}")

        if self.diff_income > 0:
            print(f"Your Actual Income is greater than your Estimateds. It is higher by ${self.diff_income}.")
        elif self.diff_income < 0:
            print(f"Your Actual Income is lesser than your Estimateds. It is lesser by ${self.diff_income}.")
        elif self.diff_income == 0:
            print(f"Your Actual Income is same as Estimateds. The gap is ${self.diff_income}.")
        t.sleep(1.1)

        #part-6
        print(f"Actual Investment --> {self.investment}")
        print(f"Fixed Investment --> {self.fixed_investment}")

        if self.investment == self.fixed_investment:
            print("You are upto date.")
        else:
            print(f"You are {(self.fixed_investment)-(self.investment)} up or down than target($200).")

        print(f"Actual Savings --> {self.savings}")
        print(f"Estimated Savings --> {self.estimated_savings}")

        if self.savings == self.estimated_savings:
            print(f"You have saved the exact amount as estimated {self.savings}")
        elif self.savings < self.estimated_savings:
            print(f"You saved less this month by --> {self.savings - self.estimated_savings}")
        elif self.savings > self.estimated_savings:
            print(f"You saved more this month by --> {self.savings - self.estimated_savings}")
        
    # creates separate tables for each categories in external display using Tkinter 
    def Sorted_DataDisplayer(self):
        income_dataList = []
        expenses_dataList = []
        invests_dataList = []
        savings_dataList = []

        fileOpener = open(self.path+"\\data_"+self.fileName, 'r')
        lineReader = fileOpener.readlines()

        for line in lineReader:
            if '$' in line.strip():
                table_splitList = line.split()
                table_splitList = [table_splitList[0], table_splitList[2]]
                if table_splitList[1] == 'In':
                    income_dataList.append(table_splitList)
                elif table_splitList[1] == 'Out':
                    expenses_dataList.append(table_splitList)
                elif table_splitList[1] == 'Invest':
                    invests_dataList.append(table_splitList)
                elif table_splitList[1] == 'Savings':
                    savings_dataList.append(table_splitList)
        
        root = Tk()
        root.title('Monthly Budget Data')

        # helper function to create display for the data
        def table_displayer(parent, title, data, row_position, col_position):

            frame = LabelFrame(parent, text=title, padx=10, pady=10, font=('Arial', 12, 'bold'))
            frame.grid(row=row_position, column=col_position, padx=10, pady=10) # creates a grid to properly separate and display data

            header = ['Amount', 'Category']
            full_data = [header] + data

            # this loop fills data in the grid cells
            for i,row in enumerate(full_data):
                for j, val in enumerate(row):
                    label = Label(frame, text=val, width=15, fg="black", font=('Arial', 12), borderwidth=1, relief='solid')
                    label.grid(row=i, column=j)

        table_displayer(root, "Income", income_dataList, 0, 0)
        table_displayer(root, "Expenses", expenses_dataList, 0, 1)
        table_displayer(root, "Investments", invests_dataList, 1, 0)
        table_displayer(root, "Savings", savings_dataList, 1, 1)

        root.mainloop()

    # compares previous month's data with current
    def Compare_MonthlyData(self):
        compare_fileName = input(f"Give the name of month you want to compare {self.fileName} month with: ")

        month1_filePath = open(self.path+"\\data_"+self.fileName, 'r')
        month2_filePath = open(self.path+"\\data_"+compare_fileName, 'r')

        mth1_linerdr = month1_filePath.readlines()
        mth2_linerdr = month2_filePath.readlines()

        # list of lists to store data categorically
        mth1_incomedataList = []
        mth1_expensesdataList = []
        mth1_investdataList = []
        mth1_savingsdataList = []
        mth2_incomedataList = []
        mth2_expensesdataList = []
        mth2_investdataList = []
        mth2_savingsdataList = []

        for line in mth1_linerdr:
            if '$' in line.strip():
                temp_splitList = line.split()
                temp_splitList = [temp_splitList[0], temp_splitList[2]]
                if temp_splitList[1] == 'In':
                    mth1_incomedataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Out':
                    mth1_expensesdataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Invest':
                    mth1_investdataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Savings':
                    mth1_savingsdataList.append(float(temp_splitList[0][1:]))

        for line in mth2_linerdr:
            if '$' in line.strip():
                temp_splitList = line.split()
                temp_splitList = [temp_splitList[0], temp_splitList[2]]
                if temp_splitList[1] == 'In':
                    mth2_incomedataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Out':
                    mth2_expensesdataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Invest':
                    mth2_investdataList.append(float(temp_splitList[0][1:]))
                elif temp_splitList[1] == 'Savings':
                    mth2_savingsdataList.append(float(temp_splitList[0][1:]))
        
        # data is stored by adding all the data from above lists for graphs
        data = {self.fileName: [sum(mth1_incomedataList), 
                                sum(mth1_expensesdataList), 
                                sum(mth1_investdataList), 
                                sum(mth1_savingsdataList)],
                compare_fileName: [sum(mth2_incomedataList), 
                                sum(mth2_expensesdataList), 
                                sum(mth2_investdataList), 
                                sum(mth2_savingsdataList)]}
        
        # using pandas dataframe to plot graphs
        df = pd.DataFrame(data, columns=[self.fileName, compare_fileName], index = ['Income', 'Expenses', 'Investments', 'Savings'])

        # plotting graph
        df.plot.bar()

        plot.show()

    # main function where collection of above funcs will be called
    def Main(self):
        
        # match case of user_choice
        match user_choice:

            case 1:
                print("Case 1")
                obj1.FileCreator()
            case 2:
                print("Case 2") 
                obj1.TransactionAdder()
            case 3:
                print("Case 3")
                obj1.FileRemover()
            case 4:
                print("Case 4")
                obj1.DataViewer()
            case 5:
                print("Case 5")
                obj1.DataStats()
            case 6:
                print("Case 6")
                obj1.Sorted_DataDisplayer()
            case 7:
                print("Case 7")
                obj1.Compare_MonthlyData()


input_path = "C:\\Users\\malay\\OneDrive\\Desktop\\Budget"

print("Welcome to Personal Budget Program!")
t.sleep(1.1)

print("Modes:\n1. Create a new budget file.\n" \
    "2. Add a new transaction to existing file.\n" \
    "3. Delete an existing budget file.\n" \
    "4. View existing data in terminal.\n" \
    "5. See your stats and conditions in terminal.\n" \
    "6. See the data in a sorted table in different window.\n" \
    "7. See the comparison of different months in graphs.\n" \
    "0. Exit the Program.\n")

# error handling
while True:
    try:
        user_choice = int(input("Choose what you would like to do today: "))
        if user_choice < 0 or user_choice > 7 or type(user_choice) != int :
            raise ValueError("Invalid Input.")
        break
    except ValueError as v:
        print(f"{v} Please try again")

if user_choice == 0:
    print("Exitting the Program.....")
    t.sleep(1.1)

# infinite loop until user chooses to leave
while user_choice != 0:
    if user_choice != 3:
        input_fileName = input("Give the name of the month you would like to work on: ").capitalize()
        obj1 = MyBudegt(input_path, input_fileName) # MyBudget object created
        obj1.Main()
    else:
        obj1 = MyBudegt(input_path) # MyBudget object is created
        obj1.Main()
    user_choice = int(input("Enter the mode number here to do anything more: "))
# 💰 MyBudegt - Personal Budget Management Tool

**MyBudegt** is a terminal-based and partially GUI-integrated Python project to help you manage your personal finances efficiently. It allows you to record, analyze, and visualize your monthly income, expenses, investments, and savings.

---

## 📂 Features

### 🔧 Core Functionalities

1. **FileCreator** - Create a new budget file for a specific month.
2. **TransactionAdder** - Add transactions (Income, Expenses, Savings, or Investment) with date, amount, and category.
3. **FileRemover** - Delete old or unused budget files.
4. **DataViewer** - View raw transaction data in the terminal.
5. **DataBase** - Stores summarized monthly data for calculations.
6. **DataCalc** - Calculates income, expenses, savings, cash-flow, and investment performance.
7. **DataStats** - Displays detailed financial statistics and comparisons to user estimates.
8. **Sorted_DataDisplayer** - Visual display of data (Income, Expenses, Investment, Savings) using a Tkinter window.
9. **Compare_MonthlyData** - Compare financial data of two different months using a bar graph.
10. **Main** - Central logic that calls all the above features based on user input.

---

## 🚀 Technologies Used

- **Python 3**
- `tkinter` - for GUI-based display of sorted data.
- `matplotlib` - for visual comparison graphs.
- `pandas` - for tabular comparison and data analysis.
- `datetime`, `os`, `pathlib`, `math`, `time` - for core logic and file handling.

---

## 🔑 How to Use

### 📥 Clone the repository

```bash
git clone https://github.com/yourusername/MyBudegt.git
```

### ▶️ Run the program

```bash
python mybudegt.py
```

### 🧭 Choose an option

```
Modes:
1. Create a new budget file.
2. Add a new transaction to existing file.
3. Delete an existing budget file.
4. View existing data in terminal.
5. See your stats and conditions in terminal.
6. See the data in a sorted table in a different window.
7. See the comparison of different months in graphs.
0. Exit the Program.
```

---

## 📝 Transaction Format

Each transaction must include:
- Date (`dd-mm-yyyy`)
- Amount
- Category/Type (e.g., Rent, Grocery, Salary)
- Transaction Type (`In`, `Out`, `Invest`, or `Savings`)

---

## 📊 Output Summary

- **Terminal View**: Summary of income, expenses, savings, and financial health.
- **Tkinter Window**: Tabular categorized display.
- **Matplotlib Graph**: Monthly comparison of key financial metrics.

---

## ⚠️ Important Notes

- Ensure files are named with the month (e.g., `April.txt`, `May.txt`) for better comparison.
- A separate `data_<filename>` file is auto-generated to store summary data.
- Modify `fixed_investment` and other static values in code as per your preference.

## 📄 License

MIT License © 2025 [Malay Patel]

---

## 🙌 Acknowledgements

Inspired by the need to manage student finances manually in an intuitive way.

---

## 💬 Feedback

Feel free to submit issues or pull requests to improve this tool!

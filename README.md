# 💼 Pay Calculator with Overtime

This is an extended version of the basic pay calculator written in Python.  
It includes overtime calculation: if the employee works more than 40 hours, they are paid 1.5 times the hourly rate for extra hours.

## 📌 How It Works

1. Prompts the user to enter hours worked and hourly rate.
2. Converts both inputs to `float`.
3. Applies this logic:
   - If hours ≤ 40: pay = hours × rate
   - If hours > 40:  
     - Regular pay = 40 × rate  
     - Overtime pay = (hours - 40) × rate × 1.5  
     - Total pay = regular pay + overtime pay
4. Displays total pay using `print()
   
## 🧠 Skills Practiced

- Conditional logic (`if` / `else`)
- Arithmetic operations
- Type conversion (`float`)
- User input and output

## 🔗 Related Projects
[Basic Pay Calculator] https://github.com/AaishahMunir/pay-calculator-python

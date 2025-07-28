import datetime

class Expense:

    expenses = []

    def __init__(self,amount,category,note,date=None,tracked=False):
        self.amount = float(amount)
        self.category = category
        self.note = note
        self.date = date if date else datetime.date.today()
        self.time = datetime.datetime.now().time()
        self.tracked = tracked
        if not self.tracked:
            Expense.expenses.append(self)


    def to_dict(self):
        return {
            "amount":self.amount,
            "category":self.category,
            "note":self.note,
            "date":self.date
        }

    @staticmethod
    def show_all_expenses():
        for expense in Expense.expenses:
            print(expense)

    def __str__(self):
        return f"{self.date} | ${self.amount:.2f} | {self.category} | {self.note}"



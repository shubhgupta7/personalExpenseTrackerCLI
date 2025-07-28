import datetime
from tokenize import String

from expense import Expense
import csv
import os

class ExpenseTracker:

    tracker_counter = 0
    existing_user = {}

    def __init__(self,user):
        self.user = user
        self.filename = f"{user}-expenses"
        self.expenses = []
        ExpenseTracker.tracker_counter+=1
        self.date_created = datetime.datetime.today()
        self.time_created = datetime.datetime.now().time()
        ExpenseTracker.existing_user[user] = self


    @staticmethod
    def User_exists(user):
        if user in ExpenseTracker.existing_user:
            return True
        else:
            return False

    @staticmethod
    def getUser(name):
        return ExpenseTracker.existing_user.get(name)

    def __str__(self):
        return f"Expense tracker for {self.user} is created at {self.time_created} on {self.date_created}"

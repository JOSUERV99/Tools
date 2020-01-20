import time

class Movement:
    def __init__(self, category, detail, amount, factor=1):
        self.category = category
        self.detail = detail
        self.amount = factor*amount
        self.factor = factor
        self.date = time.strftime("%d/%m/%y")
        self.hour = time.strftime("%H:%M:%S")
    def __str__(self):
        return "[ {} ]:'[{} {}]{}'= {}".format(self.category, self.date, self.hour, self.detail, self.amount)

    def __dict__(self):
        return {"detail":self.detail, "date":self.date, "hour":self.hour, "amount":self.amount}

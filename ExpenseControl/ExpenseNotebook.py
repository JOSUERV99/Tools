import json
from Movement import Movement

class ExpenseNotebook:
    def __init__(self):
        self.movements = []
        self.money = 0

    def __dict__(self):
        dict_ = dict()
        for m in self.movements:
            if m.category in dict_:
                dict_[m.category] += [m.__dict__()]
            else:
                dict_[m.category] = [m.__dict__()]
        return dict_

    def __resume__(self):
        resume = dict()
        total = sum( [m.amount for m in self.movements] )
        low = sum( [m.amount for m in self.movements if m.factor == -1] )
        high = sum( [m.amount for m in self.movements if m.factor == 1] )
        resume["total"] = total
        resume["entry"] = high
        resume["egress"] = low
        return {"resume":resume}

    def saveJSON(self):
        with open('expenses.json', 'w') as f:
            jsonParse  = self.__resume__()
            jsonParse.update({"movements":self.__dict__()})
            json.dump(jsonParse, f)

notebook = ExpenseNotebook()
notebook.movements += [Movement("Trabajo", "Arreglo de computadora", 5000)]
notebook.movements += [Movement("Alimentacion", "Tennis blancas", 5000, factor=-1)]
notebook.movements += [Movement("Ropa", "Camisetas", 5000, factor=-1)]
notebook.movements += [Movement("Transporte", "Paraiso-Cartago", 3000, factor=-1)]
notebook.movements += [Movement("Trabajo", "Arreglo de computadora", 7000)]

notebook.saveJSON()

class HistoryDict:
    history=[]

    def __init__(self, start_list):
        self.history.append(start_list)

    def set_value(self, *new_value):
        new_value={new_value[0]:new_value[1]}
        if len(self.history)<=10:
            self.history.append(new_value)
        else:
            del self.history[0]
            self.history.append(new_value)

    def get_history(self):
        print(self.history)
        return self.history

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("foo", 1)
d.set_value("bar", 4)
d.set_value("bar", 3)
d.set_value("foo", 5)
d.set_value("bar", 53)
d.set_value("bar", 45)
d.set_value("foo", 4)
d.set_value("bar", 44)
d.set_value("bar", 42)
d.set_value("foo", 6)
d.set_value("bar", 49)
d.set_value("bar", 413)
d.set_value("foo", 99)
d.set_value("bar", 430)
d.set_value("bar", 43)
d.set_value("foo", 1)
d.set_value("bar", 4)
d.set_value("bar", 3)
d.set_value("foo", 5)
d.set_value("bar", 53)
d.set_value("bar", 45)
d.set_value("foo", 4)
d.set_value("bar", 44)
d.set_value("bar", 42)
d.set_value("foo", 6)
d.set_value("bar", 49)
d.set_value("bar", 413)
d.set_value("foo", 99)
d.set_value("bar", 430)
d.get_history()
import datetime as dt
import Message as m
import pickle

class DueDateOrganizer:

    def __init__(self):
        self.dat = dict()

    def addDueDate(self,dd):
        self.dat[dd._key] = dd

    def pickle(self):
        return pickle.dumps(self)

    @classmethod
    def unpickle(cls, pickled):
        unpickled = pickle.loads(pickled)
        return unpickled

    def __str__(self):
        myStr = "DueDateOrganizer Object <"
        for k in self.dat:
            myStr += "%s: %s "%(k,self.dat[k])
        myStr+= ">"
        return myStr


class DueDate:
    
    def __init__(self, message= m.Message()):
        self.dueDate = dt.datetime(1900,1,1)
        self.issuer = "John Smith"
        self._key = message.fromEmail
        self._datMessage = message

    def __str__(self):
        return str("<DueDate Object: " + str(vars(self)) + ">")


def main():
    dd = DueDate()
    print("Default Due Date:\n" + str(dd))

    ddorg = DueDateOrganizer()
    ddorg.addDueDate(dd)

    print("\nAdded Due Date to Org:\n" + str(ddorg))

    pickledstr = ddorg.pickle()

    print("\nPickle Test: %s" % pickledstr)

    
    ddorgcopy = DueDateOrganizer.unpickle(pickledstr)
    print("\nCopy of pickled %s" % ddorgcopy)

if __name__ == '__main__':
    main()
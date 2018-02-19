from datetime import *
import Message as m

class DueDateOrganizer:

    def __init__(self):
        self.dat = dict()

    def addDueDate(self,dd):
        self.dat[dd._key] = dd

    def __str__(self):
        myStr = "DueDateOrganizer Object <"
        for k in self.dat:
            myStr += "%s: %s "%(k,self.dat[k])
        myStr+= ">"
        return myStr


class DueDate:
    
    def __init__(self, message= m.Message()):
        self.dueDate = datetime(1900,1,1)
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

if __name__ == '__main__':
    main()
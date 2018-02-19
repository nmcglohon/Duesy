from datetime import *

class Message:

    def __init__(self, toEmail, fromEmail, subject, body, date, _id):
        self.toEmail = toEmail
        self.fromEmail = fromEmail
        self.subject = subject
        self.body = body
        self.date = date
        self.id = _id

    @staticmethod
    def convert_ms_epoch(msEpoch):
        sEpoch = msEpoch / 1000.0
        return datetime.fromtimestamp(sEpoch)
        

    def __str__(self):
        return str(self.__dict__)

    


def main():
    print("Testing Message Instantiation")
    mess = Message('nmcglohon@gmail.com', 'otheremail@gmail.com','Hello There!','This is body text', date(2018,2,18), 523405)
    print(str(mess))
    print()

    print("Testing Static Time Converter Method")
    ts = 1514167200000
    print('%d -> %s' % (ts,Message.convert_ms_epoch(ts)))



if __name__ == '__main__':
    main()

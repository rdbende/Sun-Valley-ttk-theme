
from CTkMessagebox import CTkMessagebox

class CTKMESSAGEBOX:
    def __init__(self):
        pass

    @staticmethod
    def showinfo(title, message):
        return CTkMessagebox(title=title, message=message)

    @staticmethod
    def showwarning(title, message):
        return CTkMessagebox(title=title, message=message, icon="warning")

    @staticmethod
    def showerror(title, message):
        return CTkMessagebox(title=title, message=message, icon="cancel")

    @staticmethod
    def askquestion(title, message):
        msg = CTkMessagebox(title=title, message=message, icon="question", option_1="No", option_2="Yes")
        return msg.get() == "Yes"

    @staticmethod
    def askokcancel(title, message):
        msg = CTkMessagebox(title=title, message=message, icon="question", option_1="Cancel", option_2="OK")
        return msg.get() == "OK"

    @staticmethod
    def askyesno(title, message):
        msg = CTkMessagebox(title=title, message=message, icon="question", option_1="No", option_2="Yes")
        return msg.get() == "Yes"

    @staticmethod
    def askretrycancel(title, message):
        msg = CTkMessagebox(title=title, message=message, icon="warning", option_1="Cancel", option_2="Retry")
        return msg.get() == "Retry"



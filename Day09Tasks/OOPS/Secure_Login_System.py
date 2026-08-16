# Secure Login System (Decorators)


def login(func):
    def wrapper(status):
        if status==True:
            func(status)
        else:
            print("Access Denied Please Login:")
    return wrapper

@login
def dashboard(status):
      print("Welcome to Dashboard")

status=input("Are you logged in?(yes/no):")
if status.lower()=="yes":
    dashboard(True)
else:
    dashboard(False)

    


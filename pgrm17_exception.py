from p4print import p
def myFin():
    try:
        deno = int(input("Enter a value: "))
        print(f"{1/deno:.3f}")  
        return 1
    except ValueError:
        print("Value Error occurred.")
        return 0
    except TypeError:  # Indentation fixed
        print("An integer was expected")
        return 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0
    finally:
        print("This will run anyway. Even after the return statement")
x = myFin()
print(bool(x))  # Prints True if x == 1, False if x == 0

#**********************************************************************
class BankIsCrying(Exception):
    """Custom exception class"""
    def __init__(self, message):
        self.message = "How bank will survive with such a low balance?"
        super().__init__(self.message)
#**********************************************************************

p("*".center(60,"*"))
p("\nRaising Custom Excetions")
try:
    amount = int(input("Enter the amount: "))
    if amount > 5000:
        raise ValueError("Amount is not in the limit.")
    elif amount <1000:
        raise BankIsCrying("Error")
    else:
        p("You are safe")
except ValueError as e:
        p(e)
except BankIsCrying as e:
        p(e)
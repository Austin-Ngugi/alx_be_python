def perform_operation(num1, num2, operation):
    #float num1
    #float num2
    #str operation
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            try:
                return num1 / num2
            except: ZeroDivisionError
            return(" you cannot divide by zero")
                
        case _:
            print("enter a valid operator")
            
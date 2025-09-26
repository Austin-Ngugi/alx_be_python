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
            if num2 == 0:
                return("Zero division error, you cannot dividie by zero")
            else:
                return num1 / num2         
        case _:
            print("enter a valid operator")
            
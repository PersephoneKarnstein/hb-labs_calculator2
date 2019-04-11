import arithmetic

print("It's calculatin' time!")
query = ""

while True:
    query = input("> ")
    query = query.strip().split(" ")

    if query[0] not in ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q", "quit"]:
        print("please enter a valid operand.")
        continue
    elif query[0]=="q" or query[0]=="quit":
        break
    else:
        try:
            if len(query[1:]) != 2 and query[0] in ["+", "-", "*", "/", "pow"]:
                print("the +, -, *, /, pow, and mod functions all take exactly 2 arguments following the operand.")
            elif len(query[1:]) != 1 and query[0] in ["square", "cube"]:
                print("the square and cube functions both take exactly one argument following the operand.")
            else:
                if "+" in query[0]:
                    print(float(query[1])+float(query[2]))
                if "-" in query[0]:
                    print(float(query[1])-float(query[2]))
                if "*" in query[0]:
                    print(float(query[1])*float(query[2]))
                if "/" in query[0]:
                    print(arithmetic.divide(query[1], query[2]))
                if "pow" in query[0]:
                    print(float(query[1])**float(query[2]))
                if "mod" in query[0]:
                    print(float(query[1])%float(query[2]))
                if "square" in query[0]:
                    print(float(query[1])**2)
                if "cube" in query[0]:
                    print(float(query[1])**3)
            

        except ValueError:
            print("please enter valid arguments.")
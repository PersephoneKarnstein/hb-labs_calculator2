import arithmetic

print("It's calculatin' time!")
query = ""

while query!='q' or query!="quit":
    query = imput("> ")
    query = query.strip().split(" ")

    if query[0] not in ["+", "-", "*", "/", "square", "cube", "pow", "mod"]:
        print("please enter a valid operand.")
        continue
    else:
        try:
            if len(query[1:]) != 2 and query[0] != not in ["+", "-", "*", "/", "pow"]:
                print("the +, -, *, /, pow, and mod functions all take exactly 2 arguments following the operand.")
            elif len(query[1:]) != 2 and query[0] != not in ["square", "cube"]:
            else:
                if "+" in query[0]:
                    print(float(query[1])+float(query[2]))
                if "-" in query[0]:
                    print(float(query[1])-float(query[2]))
                if "*" in query[0]:
                    print(float(query[1])*float(query[2]))
                if "/" in query[0]:
                    print(float(query[1])/float(query[2]))
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
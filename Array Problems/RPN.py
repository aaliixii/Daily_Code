def evalRPN(tokens):
    i = 0
    while True:
        try:
            tokens[i] = int(tokens[i])
            i+=1

        except ValueError:
            
            tokens[i-1] = operation(int(tokens[i-2]), int(tokens[i-1]), tokens[i])
            tokens.remove(tokens[i-2])
            tokens.remove(tokens[i-1])
            i = 0

        if len(tokens) == 1:
            return tokens[0]

            
def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
            return int(float(a)/b)
    elif op == '*':
        return a * b

print(evalRPN(["-11","5","+","-10","+","4","10","+","-","35","-","23","+","-17","-9","-","24","-20","-","-","38","-20","1","-","+","-","+","-7","-","-13","+","-19","+","-12","-","-15","35","-","+","16","+","-15","-17","+","+","3","+","-9","-","16","6","38","-","22","1","/","+","-","-","33","-","33","32","+","-","20","-","13","+","38","23","-20","25","+","+","-","21","23","-","+","+","10","-7","-","1","-10","37","+","+","+","-","-20","-","-20","-","1","34","18","-","+","-","2","+","7","+","37","+","-13","-","5","-","32","*","34","+","26","12","+","-","1","28","-14","-","+","24","18","-16","+","-","+","+","19","-","38","-","-1","20","34","16","38","11","22","-","-","-6","+","+","-","-","+","34","18","-","/","-","14","24","-","-","-6","+","10","+","30","-","16","-","25","+","-10","-","39","+","-19","+","21","32","-","-5","-","-11","/","12","-","+","-1","-17","+","+","-2","-","37","-","-8","*","15","+","-1","-","-8","4","36","+","-","+","17","15","14","+","34","9","-","-","+","-","38","-","-20","38","-15","+","+","-","37","+","-17","-13","+","-","-18","36","-","-","27","*","4","-","12","-15","16","+","-","+","34","35","28","3","+","-","+","-","4","+","29","*","9","-14","+","-","-3","8","-","20","22","-","+","-","28","9","-","+","6","+","8","+","3","-","20","17","-","34","10","-16","-","37","28","31","-","+","+","4","33","23","36","-","7","8","-","14","16","-","-","6","-","+","+","+","-","+","+","+","33","11","-18","-","-17","15","-","-","27","+","32","-","+","+","32","-","32","-20","-","+","24","+","15","+","36","-","4","-16","-2","29","+","-","/","-16","17","-","-18","-","-1","+","+","28","-","+","-9","+","19","+","-20","+","-4","1","+","-15","-6","+","14","-1","+","-12","*","+","*","-3","-","+","3","-","39","-","-18","37","*","+","-4","+","-19","+","10","+","-20","-","25","1","+","+","17","-","3","32","-","-7","+","-","16","-","-6","19","+","+","17","-","14","+","-5","-","10","-","0","+","20","14","+","-","14","-","30","+","6","20","-","+","4","+","18","+","37","28","+","+","14","+","12","+","20","8","36","22","37","-","+","-","26","-12","-","-","20","-","+","-","11","-9","26","3","-","+","38","26","-15","-","-","6","+","+","-","+","19","-","4","20","-6","-","+","20","5","28","-","/","-","-8","+","-13","-5","2","14","/","36","-","+","25","+","/","-","+","23","21","-17","+","+","-","0","-","-13","-","-18","+","28","-","-17","-","37","+","-5","-","-8","+","13","20","-","-","3","+","-3","-19","-","-","2","+","28","-19","-","-","17","+","32","-","10","-8","-","12","-2","+","-","+","33","-","32","-","32","+","35","17","+","+","19","-","-19","-","-6","-","-9","35","*","-","25","13","-","+","-13","-3","-19","*","+","10","24","-5","28","30","23","-","*","24","13","-","7","-","10","+","10","+","5","+","-","-","30","/","-9","-","-2","-","-","8","/","+","-","-","33","33","29","-15","+","-","-","-2","-","10","+","17","-14","-14","+","10","+","23","-","5","+","-","39","23","-1","+","-","23","+","37","23","-","5","+","-","+","+","35","7","-9","+","-","19","-4","+","+","*","+","22","+","33","34","-","22","-","+","-1","+","23","-","7","19","+","-","-16","2","36","-","20","-","-3","-","+","-","-4","37","+","-","11","/","29","-7","-","+","-18","+","36","-","13","+","17","-14","14","+","-","-","30","-","-8","-","-4","+","-10","+","17","+","-17","5","+","+","21","+","29","*","14","+","27","-","-10","+","11","-","20","/","13","29","-10","17","-","-","4","37","+","-","+","+","11","16","-2","-","9","+","-","-","-5","+","28","-","5","10","+","27","-","+","-11","+","7","-","33","-","11","-","-17","-","-5","-10","+","-","16","-","1","-","13","+","14","-","4","-","33","-","3","+","-5","-","-4","+","-15","-","5","-","39","+","-15","-","12","-","25","32","22","+","15","33","-","16","+","-","-","+","6","+","29","28","+","-","12","-","2","29","23","-","-11","-","-","+","8","32","-1","+","+","+","28","+","19","-","6","-15","-","11","-","+","-7","18","+","-11","1","+","-5","-","+","8","+","-","18","-","-16","+","-1","+","-9","+","-9","22","12","-","+","-","4","-","-19","+","28","-","-2","-","-20","17","-","-9","-","+","39","+","0","+","-8","-"]))
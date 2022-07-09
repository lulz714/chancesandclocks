import time

selection = 0
file_n = "main.txt"

print("***************************************\n"
    "Please enter your decision: "
      "\n1. Make a new entry for counter."
      "\n2. Add a value to counter."
      "\n3. Start counting."
      "\n4. Show average tag results."
      "\n***************************************")

while True:
    selection = input()
    if selection == "1" or selection == "2" or selection == "3" or selection == "4":
        break
    else:
        print("Try again.")
        continue

if selection == "1":
    file = open(file_n,"a")
    print("Please enter the tag for the entry.")
    tag = ""
    while True:
        tag = input()
        if len(tag)>0:
            break
    file.write("[" + tag + "]:")
    file.write("\n$"+tag+": \n")
    file.close()
    file = open(file_n,"r")
    print(file.read())
    file.close()
elif selection == "2":
    counter = 0
    selection1 = 0
    selections = {}
    file = open(file_n,"r")
    lines = file.readlines()
    for line in lines:
        #print(line + " " + str(lines.index(line)))
        if line.find("["):
            register_line = ""
            try:
                counter += 1
                line_number = lines.index(line)
                #print(lines[line_number-1])
                used_line = lines[line_number-1]
                first_paranthesis = used_line.index("[")
                last_paranthesis = used_line.index("]")
                register_line = used_line[first_paranthesis+1:last_paranthesis]
                selections[str(counter)] = register_line
            except ValueError:
                continue
    file.close()
    print("\n**********************************************"
          "\nPlease select your option."
          "\n**********************************************\n")
    for x in selections:
        print(str(x)+". "+selections[x])
    while True:
        selection1 = input()

        if str(selection1) in selections:
            break
        else:
            print("Try again.")
            continue
    print("Enter the value you want to add: ")
    value = 0
    while True:
        value = input()
        if value.isnumeric():
            break
        else:
            print("Try again.")
            continue
    file = open(file_n,"r")
    file_string = file.read()
    try:
        selections[str(int(selection1)+1)]
        startingbyte = file_string.find("[" + selections[str(selection1)] + "]") + 3 + len(selections[str(selection1)])
        print(startingbyte)
        lastbyte = file_string[startingbyte:].find("[")
        print(lastbyte)
        appendbyte = lastbyte + startingbyte
        file.close()
        print(appendbyte)
        firsthalf = file_string[:appendbyte-1]
        secondhalf = file_string[appendbyte-1:]
        modified_string = firsthalf + str(value) + " " + secondhalf
        file = open(file_n, "w")
        file.truncate()
        file.write(modified_string)
        file.close()
    except KeyError:
        file = open(file_n,"a")
        file.write(str(value)+" ")
        file.close()
elif selection == "3":
    print()
elif selection == "4":
    file = open(file_n,"r")
    file_string = file.read()
    titlestart = file_string.find("[")
    titleend = file_string.find("]")
    title = file_string[titlestart+1:titleend] + ": "
    firstbyte = file_string.find("$")
    startingbyte = file_string[firstbyte:].find(":") + 2
    endbyte = file_string[startingbyte+firstbyte:].find("[")-2
    mainstart = firstbyte+startingbyte
    productstring = file_string[mainstart:mainstart+endbyte]
    productvalues = productstring.split(" ")
    result = 0
    hours = 0
    minutes = 0
    for x in productvalues:
        result = result + int(x)
    result = result/len(productvalues)
    hours = result // 60
    minutes = result % 60
    print(title + str(format(hours,".0f")) +"h, " + str(format(minutes,".1f")) + "m")
"""
counter += 1
currentline = lines.index(line)
selections[str(counter)] = lines.index(line)
print(line + " " + str(lines.index(line)))
"""
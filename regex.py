import re 

#expression  = 'Calculate this 64 // 23 = '

expression=input("What do you want to do today: ")

number =re.findall(r'\d+',expression)
operator =re.findall(r'[+*-/]|//|\*\*',expression)

#print(number,operator)

op_result=''
for i in range(len(operator)):
    op_result+=operator[i]
    
# print(op_result)
number1=int(number[0])
number2=int(number[1])

if (op_result == '+'):
    print(f"The addition of {number1} and {number2}: {number1 + number2}")
elif(op_result == '-'):
    print(f"The substraction of {number1} and {number2}:{number1 - number2}")
elif(op_result == '*'):
    print(f"The multiplication of {number1} and {number2}:{number1 * number2}")
elif(op_result == '/'):
    print(f"The division of {number1} and {number2}:{number1 / number2}")
elif(op_result == '**'):
    print(f"The exponential of {number1} and {number2}:{number1 ** number2}")
elif(op_result == '//'):
    print(f"The floor division of {number1} and {number2}:{number1 // number2}")
else:
    print("Invalid operator")
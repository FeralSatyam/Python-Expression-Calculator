def main():
    user_input = input("Expression: ")
    calculate(user_input)
def calculate(user_input):
    parts = user_input.split()
    num = []
    num.append(float(parts[0]))
    num.append(parts[1])
    num.append(float(parts[2]))
    match num[1]:
        case '+':
            print(num[0] + num[2])
        case '-':
            print(num[0] - num[2])
        case '*':
            print(num[0] * num[2])
        case '/':
            print(num[0] / num[2])
main()

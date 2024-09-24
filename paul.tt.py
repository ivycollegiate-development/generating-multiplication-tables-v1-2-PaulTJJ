def main():
    while True:
        try:
            a = float(input ('please enter a number: '))
            multi_table(a)
        except ValueError:
            print('Invalid input, please enter a number value')
            continue
        choice = input('do you want to generate another table?') . lowwer()
        
import this
#El tipado es ignorado por Python pero ayuda al programador y linters
def add(num1:int, num2:int) -> int:
    """Returns the sum of the two input integers"""
    return num1 + num2

def loops():
    """Basic loops"""
    for i in range(10):
        print(i, end=' ')
    random_list = [1, 6, 'hola', 3.8, [1, 2, 3]]
    for item in random_list:
        print(item)

def main():
    """Main function"""
    print(add(1, 2))
    print(add('Hello', 'World'))
    loops()

if __name__ == "__main__":
    main()
    dic = {'a': 1, 'b': 2, 'c': 3}
    print(dic)
    dic['d']=4
    print(dic)
    list3 = list()
    print(list3)
#El tipado es ignorado por Python pero ayuda al programador y linters
def add(num1:int, num2:int) -> int:
    """Returns the sum of the two input integers"""
    return num1 + num2

def main():
    """Main function"""
    print(add(1, 2))
    print(add('Hello', 'World'))

if __name__ == "__main__":
    main()
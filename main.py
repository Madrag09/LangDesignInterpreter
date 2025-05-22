import sys
from scanner import Scanner
from parser import Parser
from interpreter import Interpreter


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    expression = parser.parse()
    interpreter = Interpreter()
    result = interpreter.evaluate(expression)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as file:
            run(file.read())
    else:
        while True:
            try:
                line = input(">>> ")
                if line.strip() == "": continue
                run(line)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")

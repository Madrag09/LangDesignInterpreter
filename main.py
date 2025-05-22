from scanner import Scanner
from parser import Parser
from interpreter import Interpreter

interpreter = Interpreter()  # <- Persistent across REPL input

def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    statements = parser.parse()

    interpreter.interpret(statements)

if __name__ == "__main__":
    while True:
        try:
            line = input(">>> ")
            if line.strip() == "":
                continue
            run(line)
        except Exception as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            break

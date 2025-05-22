from scanner import Scanner
from parser import Parser
from interpreter import Interpreter

interpreter = Interpreter()  # Persistent across REPL input


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    parser = Parser(tokens)
    statements = parser.parse()

    interpreter.interpret(statements)


def is_incomplete_code(source):
    # Simple heuristic: more opening braces than closing ones
    return source.count("{") > source.count("}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # If a file is passed in, run it
        with open(sys.argv[1]) as f:
            run(f.read())
    else:
        # Interactive REPL
        while True:
            try:
                source = ""
                prompt = ">>> "
                while True:
                    line = input(prompt)
                    source += line + "\n"
                    if not is_incomplete_code(source):
                        break
                    prompt = "... "  # Continue prompt for block input
                run(source)
            except Exception as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nExiting REPL.")
                break

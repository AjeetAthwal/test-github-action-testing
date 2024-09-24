def print_hello(str: str) -> None:
    print(f"hello {str}")

def return_hello(str: str) -> str:
    return "hello " + str


if __name__ == "__main__":
    print_hello("world")
    print(return_hello("world"))
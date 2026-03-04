import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    
    # looks for numbers with some digits after decimal and surrounded by spaces
    pattern = r"\s\d+\.\d+\s"

    # Adding the spaces to cover cases when the number is in the beginning or in the end
    matches = re.finditer(pattern, f" {text} ")
    
    for match in matches:
        # changes the type from str to float to make math operations with the match and strips off the spaces for proper calculation
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
   
    # calling the function with the generator as a variable
    return sum(func(text))

    
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: " \
    "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
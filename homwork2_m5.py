# find all numbers (integers and floats) in the given text and calculate their sum
from typing import Callable
import re
text = "Загальний дохід працівника складається з декількох частин: " \
"1000.01 як основний дохід, " \
"доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str): # generator to find numbers in text
    for number in re.findall(r"(?<=\s)\d+\.\d+(?=\s)", text): # regex to find integers and floats
        if number: # check if the number is not empty
            yield float(number) 

def sum_profit(text: str, func: Callable): # function to sum numbers from generator
    total = 0
    for number in func(text): # iterate over the generator
        total += number
    return total
        
total_income = sum_profit(text, generator_numbers) # calculate total income
print(f"Загальний дохід: {total_income}")
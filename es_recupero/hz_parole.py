from string import ascii_lowercase
from string import punctuation
import re

def count_unique_words(testo:str) -> dict[str, int]:

    result:list[str] = re.findall(r'\b\w+\b', testo.lower())
    output: dict[str, int] = {}
    for i in result:
        if i not in output:
            output[i] = 1
        else:
            output[i] += 1
    return output

        

    

text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)

print(output)
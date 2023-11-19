# Original glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A named storage location in a computer program.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'conditional': 'A statement that performs different actions depending on whether a condition is true or false.',
    'list': 'An ordered collection of items, which can be of different types.'
}

# Loop through the dictionary and print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")

# Additional Python terms to add to the glossary
additional_glossary = {
    'tuple': 'An immutable ordered collection of items.',
    'dictionary': 'An unordered collection of items, each with a key-value pair.',
    'module': 'A file containing Python definitions and statements.',
    'string': 'A sequence of characters, enclosed in quotes.',
    'boolean': 'A data type that has one of two possible values: True or False.'
}

# Update the original glossary with the additional terms
programming_glossary.update(additional_glossary)

# Print the updated glossary with the new terms
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
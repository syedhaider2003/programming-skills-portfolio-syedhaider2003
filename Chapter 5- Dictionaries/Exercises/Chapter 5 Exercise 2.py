# Create a glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A named storage location in a computer program.',
    'function': 'A reusable block of code that performs a specific task.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'conditional': 'A statement that performs different actions depending on whether a condition is true or false.',
    'list': 'An ordered collection of items, which can be of different types.'
}

# Print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
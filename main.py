import re

token_patterns = [
    ('while|if|else|return|break|continue|int|for|float|void', 'keyword'),
    ('[a-zA-Z][a-zA-Z0-9_]*', 'identifier'),
    ('[0-9]+(\.[0-9]+)?(E[-+]?[0-9]+)?', 'num'),
    # ('-?[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)?', 'num'),

    # ('\+|-', 'addop'),
    # ('\*|/', 'mulop'),
    # ('<|>|<=|>=|==|!=', 'relop'),

    ('\+', '+'),
    ('-', '-'),
    ('\*', '*'),
    ('/', '/'),
    ('=', '='),
    ('<', '<'),
    ('>', '>'),

    ('&&', 'and'),
    ('\|\|', 'or'),
    ('!', 'not'),
    (';', ';'),
    ('\(', '('),
    ('\)', ')'),
    ('{', '{'),
    ('}', '}'),
    ('\[', '['),
    ('\]', ']'),
]

def lexical_analysis(input_file):
    with open(input_file, 'r') as file:
        code = file.read()

    tokens = []
    while code:
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group()
                tokens.append((token_type, value))
                code = code[len(value):].strip()
                break
        else:
            error_match = re.match('.', code)
            print("error_match: ", error_match)
            if error_match:
                value = error_match.group()
                tokens.append(('Error', value))
                code = code[len(value):].strip()

    return tokens

if __name__ == "__main__":
    input_file = "input.txt"
    tokens = lexical_analysis(input_file)

    for token_type, value in tokens:
        print(f"{token_type} : {value}")

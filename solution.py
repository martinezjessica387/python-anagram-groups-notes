def groups(words):
    result = {}
    for word in words:
        signature = ''.join(sorted(word.casefold()))
        result.setdefault(signature, []).append(word)
    return list(result.values())

def solve(value):
    return groups(value)

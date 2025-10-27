brackets = input()


def is_correct_bracket_seq(brackets):
    brackets = list(map(str, brackets))
    if brackets == '':
        return True
    memory = []
    for bracket in brackets:
        if bracket == '(' or bracket == '{' or bracket == '[':
            memory.append(bracket)
            continue
        if memory == []:
            return False
        memory_pop = memory.pop()
        if memory_pop == '(' and bracket == ')':
            continue
        if memory_pop == '[' and bracket == ']':
            continue
        if memory_pop == '{' and bracket == '}':
            continue
        if bracket == ')' or bracket == '}' or bracket == ']':
            return False
        return False
    if memory != []:
        return False
    return True


if __name__ == '__main__':
    print(is_correct_bracket_seq(brackets))

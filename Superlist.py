def list_superset(list_set_1, list_set_2):
    result = []
    if len(list_set_1) < len(list_set_2):
        list_set_1, list_set_2 = list_set_2, list_set_1
    for i in list_set_2:
        if i in list_set_1:
            result.append(i)
    if len(result) == len(list_set_1):
        return 'Наборы равны.'
    if result == list_set_2:
        return f'Набор {list_set_1} - супермножество.'
    else:
        return 'Супермножество не обнаружено.'


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))

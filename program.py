def get_mean(values):
    result = (sum(values) / len(values))
    return f'{result:.2f}'
# Список значений для теста
num_lst = [3, 6, 5, 7, 9, 1]
# Тут вызов функции.
print(get_mean(num_lst))  # Напечатайте результат вызова функции.
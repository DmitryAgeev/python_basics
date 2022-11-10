"""
1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
"""
fruits_1 = ['Mango', 'Papaya', 'Banana', 'Apple', 'Orange', 'Peach', 'Watermelon', 'Melon', 'Grape', 'Pear']
fruits_2 = ['Mango', 'Papaya', 'Apricot', 'Apple', 'Dragon fruit', 'Peach', 'Pineapple', 'Melon', 'Grapefruit', 'Pear']
fruits_all = [fruit for fruit in fruits_1 if fruit in fruits_2]
print(fruits_all)

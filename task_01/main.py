import pulp

# 1. створюємо моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# 2. змінні -->  цілі значення
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# 3. додавання моделі цілі
#  (1 * Лимонад + 1 * Фруктовий сік)
model += lemonade + fruit_juice, "Total_Products"

# 4. додавання обмежень (ресурсів)
# обмеження на Воду: 2 од. на Лимонад + 1 од. на Фруктовий сік <= 100
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# обмеження на Цукор: 1 од. на Лимонад <= 50
model += 1 * lemonade <= 50, "Sugar_Constraint"

# обмеження на Лимонний сік: 1 од. на Лимонад <= 30
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# обмеження на Фруктове пюре: 2 од. на Фруктовий сік <= 40
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# 5. розв'язання моделі
model.solve()

# 6. резальт
print(f"Статус розв'язання: {pulp.LpStatus[model.status]}")
print("-" * 30)
print(f"Вироблено Лимонаду: {lemonade.varValue}")
print(f"Вироблено Фруктового соку: {fruit_juice.varValue}")
print("-" * 30)
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")
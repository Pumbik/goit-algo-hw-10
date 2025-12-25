import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# функція визначення меж
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_points=10000):
    # межі для Y 
    # Для x^2 на [0, 2] максимальне значення y = 4
    x_test = np.linspace(a, b, 100)
    y_max = max(func(x_test))
    
    # випадкові точки
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, y_max, num_points)
    
    # які точки знаходяться під кривою
    points_under_curve = y_random < func(x_random)
    count_under = np.sum(points_under_curve)
    
    # площа прямокутника
    rectangle_area = (b - a) * y_max
    
    # інтеграл ≈ (кількість під кривою / заг. кількість) * площа прямокутника
    integral_mc = (count_under / num_points) * rectangle_area
    
    return integral_mc, x_random, y_random, points_under_curve

# обчисленя інтегралу

# кількість випадкових точок (чим більше, тим точніше)
N = 15000 

# a) обчислення методом Монте-Карло
mc_result, x_rnd, y_rnd, under_mask = monte_carlo_integration(f, a, b, N)

# b) аналітична перевірка (через SciPy quad)
quad_result, error = spi.quad(f, a, b)

# c) теоретичне значення (для довідки): x^3 / 3 | від 0 до 2 = 8/3 ≈ 2.6666...
theory_result = 8/3

print(f"--- Результати ---")
print(f"Метод Монте-Карло ({N} точок): {mc_result:.5f}")
print(f"Функція quad (SciPy):            {quad_result:.5f}")
print(f"Аналітичний розрахунок (8/3):    {theory_result:.5f}")
print(f"-" * 20)
print(f"Абсолютна похибка: {abs(mc_result - quad_result):.5f}")
print(f"Відносна похибка:  {abs(mc_result - quad_result) / quad_result * 100:.2f}%")

# візуалізація методу
plt.figure(figsize=(10, 6))

# малюємо функцію
x = np.linspace(a - 0.5, b + 0.5, 400)
plt.plot(x, f(x), 'r', linewidth=2, label=f'f(x)=x^2')

# малюємо випадкові точки
plt.scatter(x_rnd[under_mask], y_rnd[under_mask], color='green', s=1, alpha=0.3, label='Під кривою')
plt.scatter(x_rnd[~under_mask], y_rnd[~under_mask], color='blue', s=1, alpha=0.3, label='Над кривою')

# межі
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.xlim(a - 0.1, b + 0.1)
plt.ylim(0, max(f(x)) + 0.1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Метод Монте-Карло: N={N}, Результат={mc_result:.4f}')
plt.legend()
plt.grid(True)
plt.show()
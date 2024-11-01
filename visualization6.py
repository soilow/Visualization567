import numpy as np
import matplotlib.pyplot as plt

def gravitational_potential(x, y, m, G=1):
    # Гравитационный потенциал: U = -G * m / r, где r - расстояние до источника масс
    r = np.sqrt(x**2 + y**2)
    return -G * m / r

def elastic_potential(x, y, k):
    # Потенциал упругости: U = 1/2 * k * r^2, где r - расстояние от центра
    r = np.sqrt(x**2 + y**2)
    return 0.5 * k * r**2

# Пользовательский ввод параметров
potential_type = input("Введите тип потенциального поля (gravitational или elastic): ")
if potential_type == "gravitational":
    m = float(input("Введите массу (m): "))
    G = float(input("Введите гравитационную постоянную (G, по умолчанию 1): ") or 1)
elif potential_type == "elastic":
    k = float(input("Введите коэффициент жесткости (k): "))
else:
    raise ValueError("Неизвестный тип потенциального поля")

# Задаем координатную сетку
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисляем потенциальное поле
if potential_type == "gravitational":
    Z = gravitational_potential(X, Y, m, G)
elif potential_type == "elastic":
    Z = elastic_potential(X, Y, k)

# Визуализация потенциального поля
plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(cp, label='Потенциальная энергия U(x, y)')
plt.xlabel('X, координата')
plt.ylabel('Y, координата')
plt.title(f'Потенциальное поле: {"Гравитационное" if potential_type == "gravitational" else "Упругое"}')
plt.show()

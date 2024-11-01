import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation

def equations(t, y, k):
    g = 9.81
    v = np.sqrt(y[1]**2 + y[3]**2)
    dxdt = y[1]
    dvxdt = -k * y[1] * v
    dydt = y[3]
    dvydt = -g - k * y[3] * v
    return [dxdt, dvxdt, dydt, dvydt]

def init_trajectory():
    line1.set_data([], [])
    point1.set_data([], [])
    return line1, point1

def animate_trajectory(i):
    line1.set_data(x[:i+1], y_coord[:i+1])
    point1.set_data([x[i]], [y_coord[i]])
    return line1, point1

def init_speed():
    line2.set_data([], [])
    return line2,

def animate_speed(i):
    line2.set_data(t[:i+1], speed[:i+1])
    return line2,

def init_coords():
    line3_x.set_data([], [])
    line3_y.set_data([], [])
    return line3_x, line3_y

def animate_coords(i):
    line3_x.set_data(t[:i+1], x[:i+1])
    line3_y.set_data(t[:i+1], y_coord[:i+1])
    return line3_x, line3_y


v0 = float(input("Введите начальную скорость (м/с): "))
angle = float(input("Введите угол между вектором скорости и линией горизонта (в градусах): "))
h = float(input("Введите высоту, с которой брошено тело (м): "))
k = float(input("Введите коэффициент сопротивления среды k: "))


angle_rad = np.radians(angle)
vx0 = v0 * np.cos(angle_rad)
vy0 = v0 * np.sin(angle_rad)

y0 = [0, vx0, h, vy0]

t_span = (0, 100)

# Решение задачи с использованием метода Рунге-Кутты 4-го порядка
sol = solve_ivp(equations, t_span, y0, args=(k,), dense_output=True, max_step=0.01)

t = np.linspace(0, t_span[1], 5000)
y = sol.sol(t)

x = y[0]
y_coord = y[2]

valid_indices = y_coord >= 0
t = t[valid_indices]
x = x[valid_indices]
y_coord = y_coord[valid_indices]

vx = y[1][valid_indices]
vy = y[3][valid_indices]
speed = np.sqrt(vx**2 + vy**2)

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlim((0, max(x) * 1.05))
ax1.set_ylim((0, max(y_coord) * 1.1))
ax1.set_aspect('equal')
ax1.set_xlabel('Расстояние по горизонтали (м)')
ax1.set_ylabel('Высота (м)')
ax1.set_title('Анимация траектории движения тела, брошенного под углом к горизонту')

line1, = ax1.plot([], [], lw=2)
point1, = ax1.plot([], [], 'ro')



ani1 = animation.FuncAnimation(fig1, animate_trajectory, frames=len(x), init_func=init_trajectory,
                               interval=30, blit=True)

plt.grid()
plt.show()

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.set_xlim((0, max(t) * 1.05))
ax2.set_ylim((0, max(speed) * 1.1))
ax2.set_xlabel('Время (с)')
ax2.set_ylabel('Скорость (м/с)')
ax2.set_title('Анимация зависимости скорости от времени')

line2, = ax2.plot([], [], lw=2)


ani2 = animation.FuncAnimation(fig2, animate_speed, frames=len(t), init_func=init_speed,
                               interval=30, blit=True)

plt.grid()
plt.show()

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.set_xlim((0, max(t) * 1.05))
ax3.set_ylim((0, max(max(x), max(y_coord)) * 1.1))
ax3.set_xlabel('Время (с)')
ax3.set_ylabel('Координаты (м)')
ax3.set_title('Анимация зависимости координат от времени')

line3_x, = ax3.plot([], [], label='Координата x', lw=2)
line3_y, = ax3.plot([], [], label='Координата y', lw=2)
ax3.legend()


ani3 = animation.FuncAnimation(fig3, animate_coords, frames=len(t), init_func=init_coords,
                               interval=30, blit=True)

plt.grid()
plt.show()

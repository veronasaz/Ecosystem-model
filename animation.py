import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Початкова кількість жертв та хижаків
prey_0 = int(input('Введіть початкову кількість жертв: '))
predator_0 = int(input('Введіть початкову кількість хижаків: '))

# Параметри моделі
alpha = random.uniform(0.1, 0.2)  # Коефіцієнт розмноження жертв
beta = random.uniform(0.01, 0.03)   # Коефіцієнт полювання на жертв хижаками
gamma = random.uniform(0.1, 0.3)   # Коефіцієнт розмноження хижаків
delta = random.uniform(0.005, 0.015)  # Коефіцієнт смертності хижаків

# Початкові умови та параметри інтеграції
t0 = 0
tmax = 200
dt = 0.1
t = np.arange(t0, tmax, dt)
n = len(t)

# Функції, що описують динаміку популяцій
def prey_growth(prey, predator):
    return alpha * prey - beta * prey * predator

def predator_growth(prey, predator):
    return delta * prey * predator - gamma * predator

# Генерація випадкових коефіцієнтів для розмноження та смертності
random_alpha = np.random.normal(1, 0.1, n)
random_delta = np.random.normal(1, 0.1, n)

# Розв'язання диференціальних рівнянь
prey = np.zeros(n)
predator = np.zeros(n)

prey[0] = prey_0
predator[0] = predator_0

for i in range(1, n):
    prey[i] = prey[i-1] + dt * (random_alpha[i] * prey_growth(prey[i-1], predator[i-1]))
    predator[i] = predator[i-1] + dt * (random_delta[i] * predator_growth(prey[i-1], predator[i-1]))

# Візуалізація результатів
fig, ax = plt.subplots()

def plot(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Генерація випадкових позицій
    prey_positions = np.random.rand(int(prey[frame]), 2) * 10
    predator_positions = np.random.rand(int(predator[frame]), 2) * 10

    ax.scatter(prey_positions[:, 0], prey_positions[:, 1], color='green', s=10, label='Жертви')
    ax.scatter(predator_positions[:, 0], predator_positions[:, 1], color='red', s=50, marker='s', label='Хижаки')

    ax.grid(True)

ani = FuncAnimation(fig, plot, frames=range(n), blit=False, interval=50)
plt.show()

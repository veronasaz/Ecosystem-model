'''Imitation of the dynamics of predator-prey populations'''

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

# Чисельне розв'язання диференціальних рівнянь
prey = np.zeros(n)
predator = np.zeros(n)

prey[0] = prey_0
predator[0] = predator_0

for i in range(1, n):
    prey[i] = prey[i-1] + dt * (random_alpha[i] * prey_growth(prey[i-1], predator[i-1]))
    predator[i] = predator[i-1] + dt * (random_delta[i] * predator_growth(prey[i-1], predator[i-1]))

# Візуалізація результатів
animation_time_limit = 30000  # 30 секунд
fig, ax = plt.subplots()

def plot(frame):
    ax.clear()
    ax.plot(t[:frame], prey[:frame], label='Жертви')
    ax.plot(t[:frame], predator[:frame], label='Хижаки')
    ax.set_title('Динаміка популяцій хижаків та жертв')
    ax.set_xlabel('Час')
    ax.set_ylabel('Популяція')
    ax.legend()
    ax.grid(True)

    # Перевірка, чи пройшов час, встановлений для анімації
    if frame * 50 >= animation_time_limit:
        ani.event_source.stop()  # Зупинка анімації після досягнення межі по часу

ani = FuncAnimation(fig, plot, frames=range(n), blit=False, interval=50)
plt.show()

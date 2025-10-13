from math import sqrt

G = 6.67430e-11 
# заглушка стояла там где была строка с pass, я ее заменяю на
def recalculate_space_objects_positions(space_objects, delta_t):
    """Пересчитывает скорости и координаты тел за шаг времени delta_t"""

    for obj in space_objects:
        fx = 0
        fy = 0
        for other in space_objects:
            if obj == other:
                continue
            dx = other.x - obj.x
            dy = other.y - obj.y
            r = sqrt(dx ** 2 + dy ** 2)
            if r == 0:
                continue
            F = G * obj.m * other.m / r ** 2
            fx += F * dx / r
            fy += F * dy / r

        ax = fx / obj.m
        ay = fy / obj.m
        obj.vx += ax * delta_t
        obj.vy += ay * delta_t
        obj.x += obj.vx * delta_t
        obj.y += obj.vy * delta_t
        # это 3.2 здесь модуль расчета угловой скорости 
def calculate_angular_velocity(obj, center):
    """Вычисляет угловую скорость планеты вокруг звезды"""
    dx = obj.x - center.x
    dy = obj.y - center.y
    r = sqrt(dx**2 + dy**2)
    v_tangential = abs(obj.vx * dy - obj.vy * dx) / r
    return v_tangential / r
# в решнии этой задачи глубоко благодарю в помощи chat gpt 
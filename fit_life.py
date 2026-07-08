# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))


user_weight = float(input("Введите ваш вес в кг (пример - 75.5 или 80): "))
user_height = float(input("Введите ваш рост в метрах (пример - 1.75 или 2): "))


# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / (user_height**2), 1)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER


print(f"Отчет для пользователя: {user_name} ({user_age} л.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")

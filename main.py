# main.py
import random
from exercises import EXERCISES, SPLITS


def generate_workout_plan(days: int):
    """Генерирует план тренировок на указанное количество дней."""
    if days not in SPLITS:
        print("\n❌ Ошибка: выберите от 1 до 3 тренировочных дней.")
        return

    selected_split = SPLITS[days]
    print(f"\n==========================================")
    print(f"   🏃 ВАШ ПЛАН ТРЕНИРОВОК НА {days} ДН. В НЕДЕЛЮ   ")
    print(f"==========================================")

    for day_num, muscle_groups in enumerate(selected_split, 1):
        print(f"\n📅 ДЕНЬ {day_num}:")
        for group in muscle_groups:
            available_exercises = EXERCISES.get(group, [])
            if available_exercises:
                # Берем 2 случайных упражнения для каждой группы мышц
                count = min(2, len(available_exercises))
                chosen = random.sample(available_exercises, k=count)
                
                group_name = group.upper()
                print(f"  💪 {group_name}:")
                for ex in chosen:
                    print(f"    • {ex}")


def show_all_exercises():
    """Выводит список всех доступных упражнений по категориям."""
    print("\n==========================================")
    print("        📋 БАЗА ДОСТУПНЫХ УПРАЖНЕНИЙ        ")
    print("==========================================")
    for group, items in EXERCISES.items():
        print(f"\n🔹 Категория: {group.upper()}")
        for item in items:
            print(f"   • {item}")


def main():
    """Главный цикл консольного интерфейса."""
    while True:
        print("\n" + "=" * 35)
        print("    🏋️‍♂️ FIT PLAN GENERATOR 🏋️‍♂️")
        print("=" * 35)
        print("1. Сгенерировать план тренировок")
        print("2. Посмотреть базу упражнений")
        print("0. Выйти из программы")

        choice = input("\nВыберите действие (0-2): ").strip()

        if choice == "1":
            try:
                days = int(input("На сколько дней сгенерировать план (1-3)? "))
                generate_workout_plan(days)
            except ValueError:
                print("\n❌ Введите корректное число!")
        elif choice == "2":
            show_all_exercises()
        elif choice == "0":
            print("\nУдачи на тренировках! До связи! 👋")
            break
        else:
            print("\n❌ Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
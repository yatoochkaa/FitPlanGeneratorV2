import random

from exercises import EXERCISES


def generate_workout(exercises, count=4):
    return random.sample(exercises, count)


if __name__ == "__main__":
    exercises = []

    for group in EXERCISES.values():
        exercises.extend(group)

    workout = generate_workout(exercises)

    print("Ваша тренировка:")
    for exercise in workout:
        print("-", exercise)
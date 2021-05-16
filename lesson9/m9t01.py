def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "отлично",
        "B": "очень хорошо",
        "C": "хорошо",
        "D": "удовлетворительно",
        "E": "достаточно",
        "FX": "неудовлетворительно",
        "F": "неудовлетворительно",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == 'grade':
        return get_grade
    elif option == 'description':
        return get_description
    return None


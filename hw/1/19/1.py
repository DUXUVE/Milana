class Student:
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def set_name(self, name):
        if name == "":
            raise ValueError("Имя не может быть пустым")
        self.__name = name

    def set_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Оценка должна быть от 0 до 100")
        self.__grade = grade

    def save(self):
        print(f"Сохранение студента: ID={self.__id}, Имя={self.__name}, Оценка={self.__grade}")
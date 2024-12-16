# Сложный уровень:
# 1) Создайте систему регистрации на конференцию.
# Реализуйте классы Conference (конференция), Participant (участник) и RegistrationSystem (система регистрации).
# Класс Conference должен иметь атрибуты name (название) и capacity (вместимость),
# класс Participant - атрибуты name (имя) и email (электронная почта), а
# класс RegistrationSystem - атрибуты conference (конференция) и participants (список участников),

# а также методы
# register(participant) для регистрации участника и
# is_registration_available() для проверки доступности регистрации на конференцию.
# Реализуйте проверку наличия свободных мест на конференции перед регистрацией.


class Conference:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}"


class Participant:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    # def getter(self,attr):

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


class RegistrationSystem:
    def __init__(self, conference: Conference, participants: list[Participant]):
        self.conference = conference
        # Достаточно идентификации по email
        self.participants = {
            participant.email: {"name": participant.name}
            for participant in participants
        }

    def register(self, participant: Participant) -> bool:
        if not self.is_registration_available(participant):
            return False

        self.participants[participant.email] = {"name": participant.name}
        return True

    def is_registration_available(self, participant: Participant) -> bool:
        return (self.conference.capacity > len(self.participants)) & (
            participant.email not in self.participants
        )

    def __str__(self):
        return f"Conference: {self.conference}, Participants: {self.participants}"


RegistrationSystem(
    Conference("Conf", 5),
    [
        Participant("name 1", "email1@mail.ru"),
        Participant("name 2", "email2@mail.ru"),
        Participant("name 3", "email3@mail.ru"),
        Participant("name 4", "email4@mail.ru"),
    ],
).register(Participant("name 1", "email1@mail.ru"))


# 2) Создайте игру "Магазин животных".
# Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
# а также методом sound(), который возвращает звук, издаваемый животным.
# От него унаследуйте классы Dog, Cat и Bird,
# каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.

# Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
# а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
# Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.


class Animals:
    _sound: str = ""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def sound(self) -> str:
        return self._sound

    def __str__(self):
        return f"Name: {self.name} Price: {self.price}"


class Dog(Animals):
    _sound = "Woof!"


class Cat(Animals):
    _sound = "Meow!"


class Bird(Animals):
    _sound = "Chirps!"


class Shop:
    def __init__(self, animals: list[Animals], budget: float):
        self.animals = {animal.name: vars(animal) for animal in animals}
        self.budget = budget

    def buy_animal(self, animal: Animals) -> bool | float:
        # name - условно уникальный идентификатор
        if animal.name in self.animals:
            print(f"Животное {animal.name} уже куплено")
            return False
        if self.budget < animal.price:
            print(f"Не хватает денег. Баланс: {self.budget}")
            return False

        self.animals[animal.name] = vars(animal)
        self.budget -= animal.price

        print(f"{animal.name} успешно куплен!")

        return self.budget

    def sell_animal(self, animal: Animals) -> bool | float:
        # name - условно уникальный идентификатор
        if animal.name not in self.animals:
            print(f"{animal.name} нет в списке доступных")
            return False

        del self.animals[animal.name]
        self.budget += animal.price

        print(f"{animal.name} успешно продан!")

        return self.budget


dog = Dog("Dog", 100)
dog1 = Dog("1Dog", 100)
cat = Cat("Cat", 50)
bird = Bird("Bird", 20)

shop = Shop([dog, cat, bird], 150)

print(shop.buy_animal(dog1))
print(shop.sell_animal(dog1))

# Средний уровень:
# 1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец). Реализуйте методы deposit(amount) для внесения средств на счет и
# withdraw(amount) для снятия средств со счета.
# Учтите возможность проверки наличия достаточного баланса перед снятием.
# 2) Создайте класс Library, представляющий библиотеку. Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки).
# Реализуйте методы
# add_book(book) для добавления книги в библиотеку, remove_book(book) для удаления книги из библиотеки,
# add_member(member) для добавления нового члена библиотеки
# remove_member(member) для удаления члена библиотеки.
# Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки и
# return_book(book, member) для возврата книги в библиотеку.


class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount: float) -> str | float:
        if amount <= 0:
            return "Ошибка - введите сумму больше нуля"

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> str | float:
        if amount <= 0:
            return "Ошибка - введите сумму больше нуля"
        if self.balance < amount:
            return "Ошибка - недостаточный баланс"

        self.balance -= amount
        return self.balance

    def __str__(self) -> str:
        return f"Owner: {self._owner}, Balance: {self._balance}"


class Library:
    def __init__(self, books: list[str], members: list[str]):
        # Пусть название книги будет уникальным
        self._books = {b: {"id": n} for n, b in enumerate(books, start=1)}
        # Имена могут быть одинаковыми
        # Для навигации по members используем ID
        self._members = {
            n: {"name": b, "book_ids": set()} for n, b in enumerate(members, start=1)
        }

    def add_book(self, book: str) -> dict[str:dict] | str:
        _book = book.strip()
        if _book in self._books:
            return f"Ошибка - книга '{_book}' уже добавлена ранее"

        self._books[_book] = {"id": len(self._books) + 1}
        return self._books

    def add_member(self, member: str) -> dict:
        _member = member.strip()

        self._members[len(self._members) + 1] = {"name": _member}

        return self._members

    def remove_member(self, member_id: int) -> dict | str:
        # Так как используем ID, то участники удаляются по нему
        if member_id not in self._members:
            return f"Ошибка - участник с ID {member_id} не существует"

        del self._members[member_id]
        return self._members

    def checkout_book(self, book: str, member_id: int) -> bool | str:
        _book = book.strip()

        if _book not in self._books:
            return f"Ошибка - книга '{_book}' не существует"
        # Определяем участника по id
        if self._books[_book]["id"] in self._members[member_id]["book_ids"]:
            return f"Ошибка - книга '{_book}' уже выдана участнику с ID {member_id}"

        self._members[member_id]["book_ids"].add(self._books[_book]["id"])

        return True

    def return_book(self, book: str, member_id: int) -> bool | str:
        _book = book.strip()

        if _book not in self._books:
            return f"Ошибка - книга '{_book}' не существует"
        # Определяем участника по id
        if self._books[_book]["id"] not in self._members[member_id]["book_ids"]:
            return f"Ошибка - книга '{_book}' не была выдана участнику с ID {member_id}"

        self._members[member_id]["book_ids"].remove(self._books[_book]["id"])

        return True


lib = Library(["книга 1", "книга 2", "книга 3"], ["member 1", "member 2", "member 3"])

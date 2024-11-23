class Telephone:
    def __init__(self, number, model):
        """Конструктор класу"""
        self.number = number
        self.model = model
        self.call_list = []

    def call(self, name, caller_number):
        """Метод для прийняття дзвінка"""
        self.call_list.append((name, caller_number))
        print(f"Вхідний дзвінок від {name} ({caller_number})")

    def delete_call(self):
        """Видалити останній номер із вхідного списку"""
        if self.call_list:
            removed_call = self.call_list.pop()
            print(f"Видалено дзвінок: {removed_call[0]} ({removed_call[1]})")
        else:
            print("Список дзвінків порожній!")

    def display_calls(self):
        """Вивести список усіх дзвінків"""
        if not self.call_list:
            print("Список дзвінків порожній!")
        else:
            print("Список дзвінків:")
            for i, (name, caller_number) in enumerate(self.call_list, start=1):
                print(f"{i}. {name} ({caller_number})")
phone = Telephone("+380123456789", "Samsung Galaxy S21")
phone.call("Іван", "+380987654321")
phone.call("Оксана", "+380665432123")
print("\nСписок дзвінків:")
phone.display_calls()
phone.delete_call()
print("\nОновлений список дзвінків:")
phone.display_calls()

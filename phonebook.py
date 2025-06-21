import json
import os

CONTACTS_FILE = "contacts.json"

# Загрузка контактов из файла
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Сохранение контактов в файл
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

# Добавление контакта
def add_contact(contacts):
    name = input("Имя: ")
    phone = input("Телефон: ")
    contacts[name] = phone
    print(f"Контакт {name} добавлен.")

# Поиск контакта
def search_contact(contacts):
    name = input("Введите имя для поиска: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Контакт не найден.")

# Удаление контакта
def delete_contact(contacts):
    name = input("Введите имя для удаления: ")
    if name in contacts:
        del contacts[name]
        print(f"Контакт {name} удален.")
    else:
        print("Контакт не найден.")

# Главное меню
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("Список контактов пуст.")
        elif choice == "5":
            save_contacts(contacts)
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


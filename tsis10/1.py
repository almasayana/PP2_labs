import psycopg2  
import csv       

# Устанавливаем соединение с PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="db",
    user="postgres",
    password="passw"
)

# Создание таблицы phonebook, если она ещё не существует
def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,        
        user_name VARCHAR(255),            
        user_phone VARCHAR(20)             
    )
    """
    with conn.cursor() as cur:
        cur.execute(command)          # Выполняем SQL-команду
        conn.commit()                 # Сохраняем изменения

# Вставка одного контакта вручную
def insert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    command = "INSERT INTO phonebook(user_name, user_phone) VALUES (%s, %s)"
    with conn.cursor() as cur:
        cur.execute(command, (name, phone)) 
        conn.commit()

# Вставка данных из CSV-файла
def insert_from_csv():
    filename = "users.csv"
    command = "INSERT INTO phonebook(user_name, user_phone) VALUES (%s, %s)"
    with open(filename, 'r') as file:     # Открываем CSV-файл для чтения
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        with conn.cursor() as cur:
            for row in reader:
                name, phone = row
                cur.execute(command, (name, phone))  # Вставляем каждую строку
        conn.commit()

# Обновление информации о контакте по номеру телефона
def update_contact():
    name = input("Enter the name of the contact to update: ")

    with conn.cursor() as cur:
        # Проверим, существует ли пользователь с таким именем
        cur.execute("SELECT user_phone FROM phonebook WHERE user_name = %s", (name,))
        result = cur.fetchone()
        if not result:
            print("Contact with this name not found.")
            return

        current_phone = result[0]
        print(f"Current phone number: {current_phone}")

        new_phone = input("Enter new phone number: ")
        if not new_phone:
            print("No new number entered. Update canceled.")
            return

        # Обновим номер
        cur.execute("UPDATE phonebook SET user_phone = %s WHERE user_name = %s", (new_phone, name))
        conn.commit()


# Поиск данных с разными фильтрами
def query_data():
    filter_by = input("Filter by (name/phone/all/sw): ").lower()   #sw - starts with
    with conn.cursor() as cur:
        if filter_by == 'name':
            name = input("Enter name: ")
            cur.execute("SELECT * FROM phonebook WHERE user_name = %s", (name,))
        elif filter_by == 'phone':
            phone = input("Enter phone: ")
            cur.execute("SELECT * FROM phonebook WHERE user_phone = %s", (phone,))
        elif filter_by == 'sw':
            prefix = input("Enter first letter(s): ")
            cur.execute("SELECT * FROM phonebook WHERE user_name ILIKE %s", (prefix + '%',))
        else:
            cur.execute("SELECT * FROM phonebook")

        rows = cur.fetchall() 

    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")


# Удаление контакта по имени или номеру
def delete_contact():
    choice = input("Delete by (name/phone): ").lower()
    value = input("Enter value: ")  # Имя или номер
    with conn.cursor() as cur:
        if choice == 'name':
            cur.execute("DELETE FROM phonebook WHERE user_name = %s", (value,))
        else:
            cur.execute("DELETE FROM phonebook WHERE user_phone = %s", (value,))
        conn.commit()

# Главное меню приложения
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Insert manually")  # Добавить контакт вручную
        print("2 - Insert from CSV")  # Загрузить из CSV
        print("3 - Update user")      # Обновить контакт
        print("4 - Query users (name / phone / all / sw)")  # Поиск
        print("5 - Delete user")      # Удалить контакт
        print("6 - Exit")             # Выйти из программы
        choice = input("Choose option: ")
        if choice == '1':
            insert()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid option!")

create_table()
# Запуск меню
menu()

conn.close()

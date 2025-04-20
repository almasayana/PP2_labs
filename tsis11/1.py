import psycopg2  

conn = psycopg2.connect(
    host="host",
    database="dbname",
    user="user",
    password="passw"
)

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,        
        user_name VARCHAR(255),            
        user_phone VARCHAR(20)             
    )
    """
    with conn.cursor() as cur:
        cur.execute(command)          
        conn.commit()                

def insert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    command = "INSERT INTO phonebook(user_name, user_phone) VALUES (%s, %s)"
    with conn.cursor() as cur:
        cur.execute(command, (name, phone)) 
        conn.commit()

def update_contact():
    name = input("Enter the name of the contact to update: ")

    with conn.cursor() as cur:
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

        cur.execute("UPDATE phonebook SET user_phone = %s WHERE user_name = %s", (new_phone, name))
        conn.commit()


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


def delete_contact():
    choice = input("Delete by (name/phone): ").lower()
    value = input("Enter value: ")  
    with conn.cursor() as cur:
        if choice == 'name':
            cur.execute("DELETE FROM phonebook WHERE user_name = %s", (value,))
        else:
            cur.execute("DELETE FROM phonebook WHERE user_phone = %s", (value,))
        conn.commit()
        
        
def create_function():
    command = """
    CREATE OR REPLACE FUNCTION return_by_pattern(pattern VARCHAR)
    RETURNS TABLE (user_id INT, user_name VARCHAR, user_phone VARCHAR) AS
    $$
    BEGIN
        RETURN QUERY
        SELECT phonebook.user_id, phonebook.user_name, phonebook.user_phone
        FROM phonebook
        WHERE phonebook.user_name LIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()
        print("Function 'return_by_pattern' has been created in PostgreSQL.")
create_function()       


def create_insert_procedure():
    command = """
    CREATE OR REPLACE PROCEDURE insert_new_user(
        in_name VARCHAR,
        in_phone VARCHAR
    )
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = in_name) THEN
            UPDATE phonebook SET user_phone = in_phone WHERE user_name = in_name;
        ELSE
            INSERT INTO phonebook(user_name, user_phone) VALUES (in_name, in_phone);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()
        print("Procedure 'insert_new_ser' created.")
create_insert_procedure()


def create_delete_procedure():
    command = """
    CREATE OR REPLACE PROCEDURE delete_user_by_value(
        del_value VARCHAR,
        by_name BOOLEAN
    )
    AS $$
    BEGIN
        IF by_name THEN
            DELETE FROM phonebook WHERE user_name = del_value;
        ELSE
            DELETE FROM phonebook WHERE user_phone = del_value;
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """
    with conn.cursor() as cur:  
        cur.execute(command)
        conn.commit()
        print("Procedure 'delete_user_by_value' has been created.")
create_delete_procedure()

def query_by_pattern():
    pattern = input("Enter pattern to search in user name: ")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM return_by_pattern(%s)", (pattern,))
        rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")


def insert_new_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with conn.cursor() as cur:
        cur.execute("CALL insert_new_user(%s, %s)", (name, phone))
        conn.commit()
        print("Insert new user operation completed.")


def delete_user_procedure():
    choice = input("Delete by (name/phone): ").strip().lower()
    value = input("Enter value to delete: ").strip()
    by_name = True if choice == "name" else False

    with conn.cursor() as cur:
        cur.execute("CALL delete_user_by_value(%s, %s)", (value, by_name))
        conn.commit()
        print("Delete operation completed.")

 
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Insert manually") 
        print("2 - Update user")      
        print("3 - Query users (name / phone / all / sw)")  
        print("4 - Delete user")      
        print("5 - Query by pattern")
        print("6 - Insert new user")     
        print("7 - Delete data by username or phone")        
        print("8 - Exit")        
        choice = input("Choose option: ")
        if choice == '1':
            insert()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            query_data()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            query_by_pattern()
        elif choice == '6':
            insert_new_user()
        elif choice == '7':
            delete_user_procedure()
        elif choice == '8':
            break
        else:
            print("Invalid option!")

create_table()
menu()
conn.close()

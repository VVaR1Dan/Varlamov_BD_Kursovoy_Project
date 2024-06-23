import mysql.connector


# ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ К БД

def search_book_janr(conn, janr):
    sql = """
    SELECT Музыкальные_инструменты, Оборудование, Микрофоны, Track_id FROM Recording_room WHERE Музыкальные_инструменты = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (janr,))
    results = cur.fetchmany(10)
    print('Список музыкальных инструментов доступных в данной комнате записи')
    for row in results:
        print(row, '\n')


def search_book_avtor(conn, avtor):
    sql = """
    SELECT Музыкальные_инструменты, Оборудование, Микрофоны, Track_id FROM Recording_room WHERE Оборудование = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (avtor,))
    results = cur.fetchmany(10)
    print('Имеющееся музыкальное оборудование для записи треков')
    for row in results:
        print(row, '\n')


def search_book_year(conn, year):
    sql = """
    SELECT Музыкальные_инструменты, Оборудование, Микрофоны, Track_id FROM Recording_room WHERE Микрофоны = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (year,))
    results = cur.fetchmany(10)
    print('Имеющиеся микрофоны для записи инструментов и вокала')
    for row in results:
        print(row, '\n')


def search_book_cost(conn, cost1):
    sql = """
    SELECT Мастеринг, Эквализация, Процесс_звукозаписи, Track_id FROM Sound_engineer WHERE Sound_engineer_id = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (cost1,))
    results = cur.fetchmany(10)
    print('Услуги предоставляемые звукорежиссёром для конкретного трека')
    for row in results:
        print(row, '\n')


# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ Recording_room
def create_book(conn, book):
    sql = """
    INSERT INTO Recording_room(Музыкальные_инструменты, Оборудование, Микрофоны, Track_id)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()


def get_book(conn, book_id):
    sql = """
    SELECT *
    FROM Recording_room
    WHERE Recording_room_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (book_id,))
    return cur.fetchone()


def update_book(conn, book):
    sql = """
    UPDATE Recording_room
    SET Музыкальные_инструменты = %s, Оборудование = %s, Микрофоны = %s, Track_id = %s
    WHERE Recording_room_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()


def delete_book(conn, book_id):
    sql1 = "DELETE FROM Recording_room WHERE Recording_room_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (book_id,))
    conn.commit()


# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ Sound_engineer
def create_client(conn, client):
    sql = """
    INSERT INTO Sound_engineer(Мастеринг, Эквализация, Процесс_звукозаписи, Track_id)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()


def get_client(conn, client_id):
    sql = """
    SELECT * 
    FROM Sound_engineer
    WHERE Sound_engineer_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (client_id,))
    return cur.fetchone()


def update_client(conn, client):
    sql = """
    UPDATE Sound_engineer
    SET Мастеринг = %s, Эквализация = %s, Процесс_звукозаписи = %s, Track_id = %s
    WHERE Sound_engineer_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()


def delete_client(conn, client_id):
    sql1 = "DELETE FROM Sound_engineer WHERE Sound_engineer_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (client_id,))
    conn.commit()


# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ Master_mixing
def create_order(conn, order):
    sql = """
    INSERT INTO Master_mixing(Выпуск_трека, Сведение, Наложение_эффектов, Track_id)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()


def get_order(conn, order):
    sql = """
    SELECT *
    FROM Master_mixing
    WHERE Master_mixing_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (order,))
    return cur.fetchone()


def update_order(conn, order):
    sql = """
    UPDATE Master_mixing
    SET Выпуск_трека = %s, Сведение = %s, Наложение_эффектов = %s, Track_id = %s
    WHERE Master_mixing_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()


def delete_order(conn, order):
    sql1 = "DELETE FROM Master_mixing WHERE Master_mixing_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (order,))
    conn.commit()


# ФУНКЦИИ ДЛЯ ПОДКЛЮЧЕНИЯ И ОТКЛЮЧЕНИЯ ОТ БД
def connect_to_db(host, user, password, database):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Успешное подключение к {database} с помощью MySQL Connector/Python\n")
    except Exception as e:
        print(f"Произошла ошибка при подключении к базе данных: {e}")
    return conn


def close_connection(conn):
    if conn:
        conn.close()
        print("\nСоединение с базой данных закрыто")


# ОСНОВНАЯ ФУНКЦИЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ ПРОГРАММЫ
def main():
    host = "127.0.0.1"
    user = "root"
    password = "12345"
    database = "Recording_studio"
    conn = connect_to_db(host, user, password, database)

    while True:
        print("\nВыберите таблицу с которой хотите взаимодействовать \n или одно из функциональных требований:")
        print("1) Recording_room")
        print("2) Sound_engineer")
        print("3) Master_mixing")
        print(" ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ")
        print("4) Установленные и подготовленные музыкальные инструменты")
        print("5) Установленное и готовое к использованию оборудование")
        print("6) Настроенные и готовые к использованию микрофоны")
        print("7) Услуги предоставляемые звукорежиссёром для конкретного трека")
        print("8) Выход")
        table_choice = input("Введите номер пункта: ")

        if table_choice == '8':
            break
        if (table_choice == '1' or table_choice == '2' or table_choice == '3'):
            print("\nВыберите действие:")
            print("1) Добавить запись")
            print("2) Просмотреть запись")
            print("3) Обновить запись")
            print("4) Удалить запись")
            print("5) Назад")
            action_choice = input("Введите номер пункта: ")
            if action_choice == '5':
                continue

        if table_choice == '1':  # Recording_room

            if action_choice == '1':
                new_order = tuple(input(
                    "Введите данные комнаты через запятую(Музыкальные_инструменты, Оборудование, Микрофоны, Track_id): ").split(
                    ','))
                create_book(conn, new_order)

            elif action_choice == '2':
                ID_order = input("Введите ID комнаты: ")
                order = get_book(conn, ID_order)
                print(order)

            elif action_choice == '3':
                updated_book_id = input("Введите ID комнаты для обновления: ")
                updated_book = list(input(
                    "Введите обновленные данные комнаты через запятую(Музыкальные_инструменты, Оборудование, Микрофоны, Track_id): ").split(
                    ','))
                updated_book.append(updated_book_id)
                updated_book_tuple = tuple(updated_book)
                update_book(conn, updated_book_tuple)

            elif action_choice == '4':
                ID_order_del = input("Введите ID комнаты для удаления: ")
                delete_book(conn, ID_order_del)


        elif table_choice == '2':  # Sound_engineer

            if action_choice == '1':
                new_client = tuple(input(
                    "Введите данные для звукорежиссёра об услугах через запятую(Мастеринг, Эквализация, Процесс_звукозаписи, Track_id): ").split(
                    ','))
                create_client(conn, new_client)

            elif action_choice == '2':
                ID_client = input("Введите ID звукорежиссёра: ")
                client = get_client(conn, ID_client)
                print(client)

            elif action_choice == '3':
                updated_client_id = input("Введите ID звукорежиссёра для обновления: ")
                updated_client = list(input(
                    "Введите обновленные данные для звукорежиссёра об услугах через запятую(Мастеринг, Эквализация, Процесс_звукозаписи, Track_id): ").split(
                    ','))
                updated_client.append(updated_client_id)
                updated_client_tuple = tuple(updated_client)
                update_client(conn, updated_client_tuple)

            elif action_choice == '4':
                ID_client_del = input("Введите ID звукорежиссёра для удаления: ")
                delete_client(conn, ID_client_del)


        elif table_choice == '3':  # Master_mixing

            if action_choice == '1':
                new_book = tuple(input(
                    "Введите данные для мастера сведения об услугах через запятую\n(Выпуск_трека, Сведение, Наложение_эффектов, Track_id): ").split(
                    ','))
                create_order(conn, new_book)

            elif action_choice == '2':
                ID_book = input("Введите ID мастера сведения: ")
                book = get_order(conn, ID_book)
                print(book)

            elif action_choice == '3':
                updated_order_id = input("Введите ID мастера сведения для обновления: ")
                updated_order = list(input(
                    "Введите обновленные данные для мастера сведения об услугах через запятую\n(Выпуск_трека, Сведение, Наложение_эффектов, Track_id): ").split(
                    ','))
                updated_order.append(updated_order_id)
                updated_order_tuple = tuple(updated_order)
                update_order(conn, updated_order_tuple)

            elif action_choice == '4':
                ID_book_del = input("Введите ID мастера сведения для удаления: ")
                delete_order(conn, ID_book_del)

        elif table_choice == '4':
            janr = input("Введите музыкальные_инструменты: ")
            search_book_janr(conn, janr)
            continue

        elif table_choice == '5':
            avtor = input("Введите оборудование: ")
            search_book_avtor(conn, avtor)
            continue

        elif table_choice == '6':
            year = input("Введите микрофоны: ")
            search_book_year(conn, year)
            continue

        elif table_choice == '7':
            cost1 = input("Введите ID трека: ")
            search_book_cost(conn, cost1)
            continue
        else:
            print("Неверный пункт. Пожалуйста, попробуйте еще раз.")

    close_connection(conn)


if __name__ == "__main__":
    main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

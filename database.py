import sqlite3
DB = 'quises.sqlite3'
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    # CONFIGURACION ADICIONAL
    cursor.execute('PRAGMA foreign_keys=on')


def close():
    cursor.close()
    conn.close()


def execute_query(query):
    cursor.execute(query)
    conn.commit()


def create_tables():
    queries = [
        '''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL);''',

        '''CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_name TEXT NOT NULL,
            correct VARCHAR (100) NOT NULL,
            wrong1 VARCHAR (100) NOT NULL,
            wrong2 VARCHAR (100) NOT NULL,
            wrong3 VARCHAR (100) NOT NULL);''',

        '''CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quiz(id) ON DELETE CASCADE,
            FOREIGN KEY (question_id) REFERENCES question (id) ON DELETE CASCADE);'''
    ]

    open()
    for q in queries:
        execute_query(q)
    close()


def add_quises():
    quizes = [
        ('Propio juego', ),
        ('¿Quién quiere ser millonario?', ),
        ('El más inteligente', )
    ]
    open()
    cursor.executemany('INSERT INTO quiz (name) VALUES (?);', quizes)
    conn.commit()
    close()


def add_question():
    questions = [
        ('¿Cuántos meses en un año tienen 28 días?',
         'Todos', 'Uno', 'Ninguno', 'Dos'),
        ('¿Qué aspecto tendrá el acantilado verde si se cae en el Mar Rojo?',
         'Mojado', 'Rojo', 'No cambiará', 'Púrpura'),
        ('¿Con qué mano es mejor mezclar el té?',
         'Con una cuchara', 'Derecha', 'Izquierda', 'Cualquiera'),
        ('¿Qué no tiene longitud, profundidad, ancho, o altura pero puede medirse?',
         'Tiempo', 'Estupidez', 'El mar', 'Aire'),
        ('¿Cuándo es posible sacar a-gua con una red?', 'Cuando el agua está congelada',
         'Cuando no hay peces', 'Cuando los peces de colores nadan lejos', 'Cuando la red se rompe'),
        ('¿Qué es más grande que un elefante y no pesa nada?',
         'La sombra de un elefante', 'Un globo', 'Un paracaídas', 'Una nube')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question_name, correct,         wrong1, wrong2, wrong3)
    VALUES (?, ?, ?, ?, ?);''', questions)
    conn.commit()
    close()


def drop_tables():
    open()
    tables = ['quiz_content', 'quiz', 'question']
    for table in tables:
        execute_query(f'DROP TABLE IF EXISTS {table};')
    close()


def create_links():
    links = []
    link = input('Quieres crear un link? (y/n): ')

    while link.lower() == 'y':
        quiz_id = int(input('ID del quiz: '))
        question_id = int(input('ID de la pregunta: '))

        links.append((quiz_id, question_id))
        link = input('Desea agregar otro link? (y/n): ')

    if links:
        query = '''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)'''

        open()
        cursor.executemany(query, links)
        conn.commit()
        close()


def show_tables():
    tables = ['quiz_content', 'quiz', 'question']
    open()
    for table in tables:
        print(f'=== TABLA: {table.upper()} ===')
        try:
            cursor.execute(f'SELECT * FROM {table}')
            result = cursor.fetchall()

            for i in result:
                print(i)

        except sqlite3.DatabaseError as error:
            print('SE ENCONTRO EL SIGUIENTE ERROR:', error)

    close()


def fetch_data(sql, data=None):
    open()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    result = cursor.fetchall()
    close()

    return result


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


def add_questions():
    questions = [
    ('¿En qué año se lanzó la consola original Nintendo Entertainment System (NES) en Norteamérica?',
     '1985', '1983', '1987', '1989'),
    ('¿Cuál es el nombre del protagonista principal de la saga de videojuegos "The Legend of Zelda"?',
     'Link', 'Zelda', 'Ganon', 'Epona'),
    ('¿Qué videojuego actual es considerado el más vendido de la historia?',
     'Minecraft', 'Grand Theft Auto V', 'Tetris', 'Wii Sports'),
    ('¿Cuál era el nombre original de Mario en su primera aparición en el juego Donkey Kong de 1981?',
     'Jumpman', 'Mr. Video', 'Plumber', 'Luigi'),
    ('¿En qué juego actual de 2022 exploras un mundo postapocalíptico controlando a un gato callejero?',
     'Stray', 'Cat Quest', 'Little Kitty, Big City', 'Night in the Woods'),
    ('¿Qué consola retro de SEGA fue la principal competidora de la Super Nintendo (SNES)?',
     'SEGA Genesis / Mega Drive', 'SEGA Master System', 'SEGA Dreamcast', 'SEGA Saturn'),
    ('¿Cómo se llama la inteligencia artificial que acompaña al Jefe Maestro en la saga Halo?',
     'Cortana', 'Serina', 'Isabel', 'The Weapon'),
    ('¿Qué fruta debe recolectar Crash Bandicoot en sus juegos clásicos y modernos?',
     'Fruta Wumpa', 'Manzana', 'Durazno', 'Mango'),
    ('¿Cuál de los siguientes juegos populares pertenece al género "Battle Royale"?',
     'Fortnite', 'Overwatch 2', 'Valorant', 'League of Legends'),
    ('¿En cuál videojuego retro de arcade debías evitar a los fantasmas Blinky, Pinky, Inky y Clyde?',
     'Pac-Man', 'Space Invaders', 'Galaga', 'Dig Dug'),
    ('¿Qué estudio de desarrollo creó el aclamado juego de rol de 2023 "Baldur\'s Gate 3"?',
     'Larian Studios', 'CD Projekt Red', 'BioWare', 'Bethesda Game Studios'),
    ('¿Cuál es el nombre del reino digital donde se desarrollan las partidas de League of Legends?',
     'Runaterra', 'Azeroth', 'Santuario', 'Tamriel'),
    ('¿Qué consola de sobremesa de la quinta generación utilizaba cartuchos en lugar de CD-ROM?',
     'Nintendo 64', 'PlayStation', 'SEGA Saturn', 'Atari Jaguar'),
    ('¿Quién es el creador de la famosa franquicia Metal Gear y el juego moderno Death Stranding?',
     'Hideo Kojima', 'Shigeru Miyamoto', 'Hidetaka Miyazaki', 'Shinji Mikami'),
    ('¿Qué juego indie de 2018 destaca por su alta dificultad en plataformas y su historia sobre salud mental?',
     'Celeste', 'Hollow Knight', 'Dead Cells', 'Ori and the Blind Forest'),
    ('¿Qué mítico RPG de 1997 para PlayStation incluía a personajes como Cloud Strife y Sephiroth?',
     'Final Fantasy VII', 'Chrono Cross', 'Xenogears', 'Vagrant Story'),
    ('¿Cuál es el nombre de la región de mundo abierto donde transcurre la historia de Grand Theft Auto V?',
     'Los Santos', 'Liberty City', 'Vice City', 'San Fierro'),
    ('¿Qué periférico de la consola NES te permitía jugar al título "Duck Hunt"?',
     'NES Zapper', 'Power Glove', 'NES Advantage', 'R.O.B.'),
    ('¿Qué juego de software actual desarrollado por FromSoftware ganó el premio al Juego del Año (GOTY) en 2022?',
     'Elden Ring', 'Dark Souls III', 'Bloodborne', 'Sekiro: Shadows Die Twice'),
    ('¿Cuál es el nombre de la corporación farmacéutica enemiga principal en la saga Resident Evil?',
     'Umbrella Corporation', 'Aperture Science', 'Abstergo Industries', 'Vault-Tec')
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
    print('🥲')


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

def get_next_question(question_id=0, quiz_id=1):
    open()
    query = '''
        SELECT 
            quiz_content.id,
            question.question_name,
            question.correct,
            question.wrong1,
            question.wrong2,
            question.wrong3
        FROM quiz_content JOIN question
        ON quiz_content.question_id = question.id
        WHERE quiz_content.id > ?
        AND quiz_content.quiz_id = ?
        ORDER BY quiz_content.id
        LIMIT 1;'''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def get_quises():
    open()
    cursor.execute('SELECT * FROM quiz ORDER BY id;')
    result = cursor.fetchall()
    close()
    return result

def run():
    drop_tables()
    create_tables()
    add_questions()
    add_quises()
    show_tables()


if __name__ == "__main__":
    print('Base de datos estructurada correctamente')
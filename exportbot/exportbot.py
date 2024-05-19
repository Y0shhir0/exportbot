import telebot
import sqlite3

# сначала нужно запустить этот код что бы создать бдешку
# потом нужно код удалить этот
# import sqlite3
# conn = sqlite3.connect('standent13.db')
# cursor = conn.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS "Group" (
#     id INTEGER PRIMARY KEY,
#     name TEXT
# )
# ''')
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Student (
#     id INTEGER PRIMARY KEY,
#     f TEXT,
#     i TEXT,
#     o TEXT,
#     groupid INTEGER,
#     FOREIGN KEY (groupid) REFERENCES "Group"(id)
# )
# ''')
# cursor.execute('''
# INSERT INTO "Group" (id, name) VALUES
# (1, '215 группе'),
# (2, '215 группе')
# ''')
#
# cursor.execute('''
# INSERT INTO Student (id, f, i, o, groupid) VALUES
# (1, 'Бобылев', 'Артем', 'Денисович', 1),
# (2, 'Семенов', 'Денис', 'Дмитриевич', 2)
# ''')
#
# conn.commit()
# conn.close()


#
#
bot = telebot.TeleBot('7087326911:AAGJD26jpVeZ80qYOqwyo0ilzrGBZawDZFo')
conn = sqlite3.connect('standent13.db', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите вашу фамилию:")

@bot.message_handler(func=lambda message: True)
def check_student(message):
    surname = message.text.strip()

    cursor.execute('SELECT s.f, s.i, s.o, g.name FROM Student s JOIN "Group" g ON s.groupid = g.id WHERE s.f = ?',
                   (surname,))
    result = cursor.fetchone()

    if result:
        response = f"Студент {result[0]} {result[1]} {result[2]} учится в {result[3]}."
    else:
        response = "Студент с такой фамилией не найден."

    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)
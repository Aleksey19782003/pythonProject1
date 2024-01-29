import sqlite3

conn = sqlite3.connect('Task.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists tabl_1(col_1 text, col_2 text, col_3 text)""")
cursor.execute("""insert into tabl_1(col_1, col_2, col_3) values('morning','day','night')""")
conn.commit()
conn.close()
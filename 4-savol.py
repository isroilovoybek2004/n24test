import psycopg2
db_data={
    'dbname':'qaytatopshirish',
    'user':'postgres',
    'host':'localhost',
    'port':5432,
    'password':'464'
}
con = psycopg2.connect(**db_data)
cur = con.cursor()

cur.execute(f"""create table students(id bigint primary key not null,name varchar(20),age int,country varchar(20));""")
cur.execute("""insert into students values(1,'Ali',19,'uzb'),(2,'vali',20,'uzb'),(3,'hasan',20,'ru'),(4,'husan',22,'usa');""")

cur.execute(f"""create table math(id bigint primary key not null,teacher_name varchar(20),student_id int);""")
cur.execute("""insert into math values(1,'sardor',1),(2,'dilshod',2),(3,'akbar',3),(4,'ulugbek',4);""")

cur.execute(f"""create table english(id bigint primary key not null,teacher_name varchar(20),student_id int);""")
cur.execute("""insert into english values(1,'shaxriyor',1),(2,'ibodulla',2),(3,'sherzod',3),(4,'otabek',4),(5,'otabek',5),(6,'otabek',5);""")

cur.execute(" select students.country,count(students.id) as student_count from math join students on students.id=math.student_id join english on students.id=english.student_id group by students.country order by student_count desc limit 1;")

data = cur.fetchall()
with open('s.txt','w') as txt:
    txt.write(f'{data}')

con.commit()
cur.close()
con.close()

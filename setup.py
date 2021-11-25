import mysql.connector as mysql

db = mysql.connect(
    host = input("host ? "),
    user = input("user ? "),
    password = input("password ? ")
)

cursor = db.cursor()
cursor.execute("create database photomate;")
cursor.execute("use photomate;")
cursor.execute("create table comptes (user_id int primary key auto_increment not null,pseudo varchar(250) not null, mdp varchar(250) not null, avatar varchar(250));")
cursor.execute("create table images (post_id int primary key auto_increment not null, post_img varchar(250) not null, user_id int not null, foreign key (user_id) references comptes(user_id));")
cursor.execute("create table amis (id_friends int primary key auto_increment not null, user_1 int not null, user_2 int not null, foreign key (user_1) references comptes(user_id), foreign key (user_2) references comptes(user_id));")
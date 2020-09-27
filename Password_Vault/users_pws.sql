--Creating and using database "main"
CREATE DATABSE main;

USE main;

--Create table "users_pws"
create TABLE users_pws(
	id INT primary key auto_increment,
    	for_website varchar(1000),
    	username varchar(1000),
    	password_ varchar(1000)
);

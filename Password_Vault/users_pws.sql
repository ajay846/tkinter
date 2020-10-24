use main;

create table users_pws(
	id INT primary key auto_increment,
    	for_website varchar(1000),
    	username varchar(1000),
    	password_ varchar(1000)
);

create table mainPass(
    	password_ varchar(2000)
);

ALTER TABLE mainPass ADD COLUMN id INT PRIMARY KEY;
INSERT INTO mainPass(id, password_) VALUES(9, 'mysafe');

use main;

create table users_pws(
	id INT primary key auto_increment,
    for_website varchar(1000),
    username varchar(1000),
    password_ varchar(1000)
);

select * from users_pws;
delete from users_pws where id=24;

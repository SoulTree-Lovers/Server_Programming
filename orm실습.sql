DROP DATABASE IF EXISTS restaurant;
use restaurant;
SET sql_safe_updates=0;

select * from restaurant;

select * from menu_item;

select * from menu_item where name = "Veggie Burger";

select * from menu_item where id = 3;

select * from menu_item where name = "Spinach Ice Cream";

DELETE FROM menu_item;

insert into restaurant (id, name)
values(10, "Test");

insert into restaurant (name)
values("Test 2");
14:03:07	DELETE FROM menu_item	Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.00087 sec

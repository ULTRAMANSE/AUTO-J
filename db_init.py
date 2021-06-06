import pymysql


def db_init():
	conn = pymysql.connect(host="127.0.0.1", user='root', passwd='111111', port=3306)
	cur = conn.cursor()
	cur.execute("create database IF NOT EXISTS autoj_db")
	cur.execute("use autoj_db")
	cur.execute("""create table if not exists staff_tb(
	id int(6) primary key,
	sname char(15) not null,
	Permissions enum("0","1","2") not null
	)""")

	cur.execute("""
	create table if not exists entrust_tb(
	entrust_id int(4) zerofill primary key,
	ename varchar(100) not null,
	contact char(15) not null,
	address varchar(100) not null,
	phone char(11) not null check(char_length(phone) = 11),
	postcode char(6) not null check(char_length(postcode) = 6),
	email varchar(50) not null
	)""")

	cur.execute("""
	create table if not exists project_tb(
	project_id int(4) zerofill primary key ,
	entrust_id int(4) zerofill not null ,
	pname varchar(100) not null,
	version char(20) not null,
	foreign key(entrust_id) references entrust_tb(entrust_id)
	)""")

	cur.execute("""
	create table if not exists dispatch_tb(
	project_id int(4) zerofill not null,
	staff_id int(6) not null,
	dtime date not null,
	primary key(project_id,staff_id),
	foreign key(staff_id) references staff_tb(id),
	foreign key(project_id) references project_tb(project_id)
	)
	""")

	cur.execute("""
 	create table if not exists authorization_tb(
 	project_id int(4) zerofill not null,
 	auth_id int(4) zerofill not null,
 	primary key(project_id,auth_id),
 	foreign key(project_id) references project_tb(project_id)
 	)""")

	cur.execute("""
	create table if not exists deviceuse_tb(
 	project_id int(4) zerofill not null,
 	use_id int(4) zerofill not null,
 	primary key(project_id,use_id),
 	foreign key(project_id) references project_tb(project_id)
 	)""")

	cur.close()
	conn.close()


if __name__ == '__main__':
	db_init()

CREATE DATABASE flask_tasks;
USE flask_task;

CREATE TABLE users ( 
	id int(11) unsigned NOT NULL AUTO_INCREMENT, 
	username varchar(100) DEFAULT NULL, 
	password varchar(255) DEFAULT NULL,
	email varchar(100) DEFAULT NULL, 
	PRIMARY KEY(id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE tasks ( 
	id int(11) unsigned NOT NULL AUTO_INCREMENT,
	user_id int(11) unsigned DEFAULT NULL,
	description varchar(255) DEFAULT NULL, 
	due_date int(11) DEFAULT NULL,
	priority int(2) DEFAULT NULL,
	status int(1) DEFAULT 1,
	PRIMARY KEY(id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE tokens ( 
	id int(11) unsigned NOT NULL AUTO_INCREMENT,
	user_id int(11) unsigned DEFAULT NULL,
	access_token varchar(255) DEFAULT NULL, 
	secret_token varchar(255) DEFAULT NULL, 
	PRIMARY KEY(id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


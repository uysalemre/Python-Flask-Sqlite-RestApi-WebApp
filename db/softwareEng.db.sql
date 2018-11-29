BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `user` (
	`id`	INTEGER NOT NULL,
	`email`	VARCHAR ( 255 ) UNIQUE,
	`username`	VARCHAR ( 255 ),
	`password`	VARCHAR ( 255 ),
	`active`	BOOLEAN,
	`last_time`	DATETIME,
	PRIMARY KEY(`id`),
	CHECK(activeIN(0,1))
);
CREATE TABLE IF NOT EXISTS `staticnav` (
	`id`	INTEGER NOT NULL,
	`header`	VARCHAR ( 80 ),
	`link`	TEXT,
	`activated`	BOOLEAN,
	CHECK(activatedIN(0,1)),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `setup` (
	`id`	INTEGER NOT NULL,
	`appname`	VARCHAR ( 50 ) NOT NULL UNIQUE,
	`settted`	BOOLEAN,
	CHECK(setttedIN(0,1)),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `roles_users` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`role_id`	INTEGER,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `user`(`id`),
	FOREIGN KEY(`role_id`) REFERENCES `role`(`id`)
);
CREATE TABLE IF NOT EXISTS `role` (
	`id`	INTEGER NOT NULL,
	`name`	VARCHAR ( 80 ) UNIQUE,
	`description`	VARCHAR ( 255 ),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `photos` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`photo1`	TEXT,
	`photo2`	TEXT,
	`photo3`	TEXT,
	`photo4`	TEXT,
	`photo5`	TEXT,
	`photo6`	TEXT,
	`photo7`	TEXT,
	`photo8`	TEXT,
	`photo9`	TEXT,
	`photo10`	TEXT,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `actors`(`id`)
);
CREATE TABLE IF NOT EXISTS `normalcontact` (
	`id`	INTEGER NOT NULL,
	`name`	VARCHAR ( 80 ),
	`email`	TEXT NOT NULL,
	`subject`	VARCHAR ( 80 ),
	`message`	TEXT,
	`document`	TEXT,
	`time`	DATETIME,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `logs` (
	`id`	INTEGER NOT NULL,
	`ip`	INTEGER,
	`describe`	TEXT,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `categories` (
	`id`	INTEGER NOT NULL,
	`name`	VARCHAR ( 80 ) NOT NULL,
	`description`	TEXT,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `agency` (
	`id`	INTEGER NOT NULL,
	`company`	VARCHAR ( 80 ),
	`phone`	INTEGER,
	`director`	VARCHAR ( 80 ),
	`photo`	TEXT,
	`description`	TEXT,
	`instagram`	TEXT,
	`facebook`	TEXT,
	`twitter`	TEXT,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `actorsoul` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`facebook`	TEXT,
	`twitter`	TEXT,
	`instagram`	TEXT,
	`description`	TEXT,
	FOREIGN KEY(`user_id`) REFERENCES `actors`(`id`),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `actors` (
	`id`	INTEGER NOT NULL,
	`name`	VARCHAR ( 80 ) NOT NULL,
	`surname`	VARCHAR ( 80 ) NOT NULL,
	`email`	TEXT NOT NULL UNIQUE,
	`activated`	BOOLEAN,
	`gender`	VARCHAR ( 50 ) NOT NULL,
	`age`	INTEGER NOT NULL,
	`phone`	INTEGER NOT NULL,
	PRIMARY KEY(`id`),
	CHECK(activatedIN(0,1))
);
CREATE TABLE IF NOT EXISTS `actormodel` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`category_id`	INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `actors`(`id`),
	FOREIGN KEY(`category_id`) REFERENCES `categories`(`id`),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `actorbody` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`height`	VARCHAR ( 20 ),
	`weight`	VARCHAR ( 20 ),
	`bodycolor`	VARCHAR ( 50 ),
	`haircolor`	VARCHAR ( 50 ),
	`hairtype`	VARCHAR ( 50 ),
	`eyecolor`	VARCHAR ( 50 ),
	`top`	INTEGER,
	`middle`	INTEGER,
	`bottom`	INTEGER,
	`foot`	INTEGER,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `actors`(`id`)
);
CREATE TABLE IF NOT EXISTS `Tempphotos` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`photo1`	TEXT,
	`photo2`	TEXT,
	`photo3`	TEXT,
	`photo4`	TEXT,
	`photo5`	TEXT,
	`photo6`	TEXT,
	`photo7`	TEXT,
	`photo8`	TEXT,
	`photo9`	TEXT,
	`photo10`	TEXT,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `Tempactors`(`id`)
);
CREATE TABLE IF NOT EXISTS `Tempactorsoul` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`facebook`	TEXT,
	`twitter`	TEXT,
	`instagram`	TEXT,
	`description`	TEXT,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `Tempactors`(`id`)
);
CREATE TABLE IF NOT EXISTS `Tempactors` (
	`id`	INTEGER NOT NULL,
	`name`	VARCHAR ( 80 ) NOT NULL,
	`surname`	VARCHAR ( 80 ) NOT NULL,
	`email`	TEXT NOT NULL UNIQUE,
	`activated`	BOOLEAN,
	`gender`	VARCHAR ( 50 ) NOT NULL,
	`age`	INTEGER NOT NULL,
	`phone`	INTEGER NOT NULL,
	CHECK(activatedIN(0,1)),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `Tempactormodel` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`category_id`	INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `Tempactors`(`id`),
	PRIMARY KEY(`id`),
	FOREIGN KEY(`category_id`) REFERENCES `categories`(`id`)
);
CREATE TABLE IF NOT EXISTS `Tempactorbody` (
	`id`	INTEGER NOT NULL,
	`user_id`	INTEGER,
	`height`	VARCHAR ( 20 ),
	`weight`	VARCHAR ( 20 ),
	`bodycolor`	VARCHAR ( 50 ),
	`haircolor`	VARCHAR ( 50 ),
	`hairtype`	VARCHAR ( 50 ),
	`eyecolor`	VARCHAR ( 50 ),
	`top`	INTEGER,
	`middle`	INTEGER,
	`bottom`	INTEGER,
	`foot`	INTEGER,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`user_id`) REFERENCES `Tempactors`(`id`)
);
COMMIT;

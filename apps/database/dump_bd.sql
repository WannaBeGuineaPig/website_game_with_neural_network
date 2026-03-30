CREATE TABLE `category` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `name_category` varchar(90) NOT NULL,
  PRIMARY KEY (`id_category`)
);

CREATE TABLE `game` (
  `id_game` int NOT NULL AUTO_INCREMENT,
  `id_topic` int NOT NULL,
  `start_play` datetime DEFAULT NULL,
  `end_play` datetime DEFAULT NULL,
  PRIMARY KEY (`id_game`),
  KEY `id_topic_fk_idx` (`id_topic`),
  CONSTRAINT `id_topic_fk` FOREIGN KEY (`id_topic`) REFERENCES `topic` (`id_topic`)
);

CREATE TABLE `game_lobby` (
  `id_user` int NOT NULL,
  `id_game` int NOT NULL,
  `place_in_the_game` int DEFAULT NULL,
  `percentage_of_similarity` decimal(7,5) DEFAULT NULL,
  `draw_image` blob,
  PRIMARY KEY (`id_user`,`id_game`),
  KEY `id_user_idx` (`id_user`),
  KEY `id_game` (`id_game`),
  CONSTRAINT `id_game` FOREIGN KEY (`id_game`) REFERENCES `game` (`id_game`),
  CONSTRAINT `id_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`)
);

CREATE TABLE `topic` (
  `id_topic` int NOT NULL AUTO_INCREMENT,
  `id_category` int NOT NULL,
  `name_topic` varchar(90) NOT NULL,
  PRIMARY KEY (`id_topic`),
  KEY `id_category_fk_idx` (`id_category`),
  CONSTRAINT `id_category_fk` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`)
);

CREATE TABLE `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `login` varchar(100) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `password` longtext NOT NULL,
  `icon` blob,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `mail_UNIQUE` (`mail`),
  UNIQUE KEY `login_UNIQUE` (`login`)
);
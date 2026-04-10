CREATE DATABASE  IF NOT EXISTS `deal_with_pixel`;
USE `deal_with_pixel`;

DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `name_category` varchar(90) NOT NULL,
  PRIMARY KEY (`id_category`)
);

INSERT INTO `category` VALUES (1,'Животные'),(2,'Средства передвижения'),(3,'Геометрические фигуры');

DROP TABLE IF EXISTS `game`;
CREATE TABLE `game` (
  `id_game` int NOT NULL AUTO_INCREMENT,
  `id_topic` int NOT NULL,
  `start_play` datetime DEFAULT NULL,
  `end_play` datetime DEFAULT NULL,
  PRIMARY KEY (`id_game`),
  KEY `id_topic_fk_idx` (`id_topic`),
  CONSTRAINT `id_topic_fk` FOREIGN KEY (`id_topic`) REFERENCES `topic` (`id_topic`)
);

DROP TABLE IF EXISTS `game_lobby`;
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

DROP TABLE IF EXISTS `topic`;
CREATE TABLE `topic` (
  `id_topic` int NOT NULL AUTO_INCREMENT,
  `id_category` int NOT NULL,
  `name_topic` varchar(90) NOT NULL,
  PRIMARY KEY (`id_topic`),
  KEY `id_category_fk_idx` (`id_category`),
  CONSTRAINT `id_category_fk` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`)
);

INSERT INTO `topic` VALUES (1,1,'Кот'),(2,1,'Собака'),(3,1,'Корова'),(4,1,'Панда'),(5,1,'Муравей'),(6,1,'Рыба'),(7,2,'Самолёт'),(8,2,'Велосипед'),(9,2,'Машина'),(10,2,'Вертолёт'),(11,3,'Круг'),(12,3,'Квадрат'),(13,3,'Шестиугольник'),(14,3,'Треугольник');

DROP TABLE IF EXISTS `user`;
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
CREATE TABLE `beer`
(
 `beer_idx`    int NOT NULL ,
 `name`        varchar(45) NOT NULL ,
 `country`     varchar(45) NOT NULL ,
 `type`        varchar(45) NOT NULL ,
 `ABV`         float NOT NULL ,
 `description` text NULL ,
 `image`       varchar(100) NOT NULL ,

PRIMARY KEY (`beer_idx`)
);

CREATE TABLE `beer_taste`
(
 `beer_idx` int NOT NULL ,
 `sweet`    int NOT NULL ,
 `sour`     int NOT NULL ,
 `tender`   int NOT NULL ,
 `bitter`   int NOT NULL ,
 `abundant` int NOT NULL ,

PRIMARY KEY (`beer_idx`),
KEY `fkIdx_186` (`beer_idx`),
CONSTRAINT `FK_185` FOREIGN KEY `fkIdx_186` (`beer_idx`) REFERENCES `beer` (`beer_idx`)
);

CREATE TABLE `beer_rank`
(
 `beer_idx`         int NOT NULL ,
 `user_click_count` int NOT NULL ,rankbeer_rank
 `recommend_count`  int NOT NULL ,

PRIMARY KEY (`beer_idx`),
KEY `fkIdx_196` (`beer_idx`),
CONSTRAINT `FK_195` FOREIGN KEY `fkIdx_196` (`beer_idx`) REFERENCES `beer` (`beer_idx`)
);
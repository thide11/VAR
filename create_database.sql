CREATE TABLE IF NOT EXISTS `meets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `size` bigint DEFAULT NULL,
  `video_url` text,
  `duration` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Data exporting was unselected.

-- Dumping structure for table meet_indexer.transcription
CREATE TABLE IF NOT EXISTS `transcription` (
  `id` int NOT NULL,
  `meets_id` int NOT NULL,
  `start_time` float NOT NULL DEFAULT '0', 
  `transcription` text NOT NULL,
  `end_time` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`meets_id`),
  KEY `fk_transcription_meets_idx` (`meets_id`),
  CONSTRAINT `fk_transcription_meets` FOREIGN KEY (`meets_id`) REFERENCES `meets` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
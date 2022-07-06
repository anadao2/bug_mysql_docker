USE bill_system;
DROP TABLE IF EXISTS `bills`;

CREATE TABLE `bills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `document` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` DECIMAL(6,2) NOT NULL DEFAULT '0.00',
  `date` DATE NOT NULL,
  `reference` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` TINYINT(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

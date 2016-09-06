CREATE TABLE IF NOT EXISTS `obslog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `type` ENUM('error', 'warning', 'info') NOT NULL,
  `source` text NOT NULL,
  `message` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

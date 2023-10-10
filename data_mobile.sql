-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.28-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para olx_mobile
CREATE DATABASE IF NOT EXISTS `olx_mobile` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_german2_ci */;
USE `olx_mobile`;

-- Copiando estrutura para tabela olx_mobile.data_mobile
CREATE TABLE IF NOT EXISTS `data_mobile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` varchar(50) DEFAULT NULL,
  `Modelo` varchar(128) DEFAULT NULL,
  `Marca` varchar(128) DEFAULT NULL,
  `Condicao` varchar(128) DEFAULT NULL,
  `Memoria_interna` varchar(128) DEFAULT NULL,
  `cor` varchar(128) DEFAULT NULL,
  `Saude_da_bateria` varchar(128) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL,
  `url` varchar(1024) DEFAULT NULL,
  `last_update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8 COLLATE=utf8_german2_ci;

-- Exportação de dados foi desmarcado.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

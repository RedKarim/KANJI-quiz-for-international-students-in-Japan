-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 25, 2024 at 05:02 PM
-- Server version: 10.6.16-MariaDB-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_manage_dv`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_tbl`
--

CREATE TABLE `user_tbl` (
  `user_id` int(11) NOT NULL COMMENT 'ユーザ主キー',
  `email` varchar(50) NOT NULL COMMENT 'メールアドレス',
  `passwd` varchar(20) DEFAULT NULL COMMENT 'パスワード',
  `security_code` varchar(10) DEFAULT NULL COMMENT 'セキュリティコード',
  `date_of_expiry` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '有効期限',
  `auth_regist_flag` tinyint(1) DEFAULT NULL COMMENT 'auth_registフラグ'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_tbl`
--

INSERT INTO `user_tbl` (`user_id`, `email`, `passwd`, `security_code`, `date_of_expiry`, `auth_regist_flag`) VALUES
(1, 'yamada@gmail.com', '123456', NULL, '2023-11-30 08:34:34', NULL),
(8, 'karim@gmail.com', '123456', '3183123', '2024-02-06 05:24:04', NULL),
(9, 'abc@gmail.com', '123456', NULL, '2023-11-30 01:07:20', NULL),
(10, 'sakurako2002@icloud.com', '0117', NULL, '2024-01-11 08:25:15', NULL),
(11, 'webweavers74@gmail.com', '123456', NULL, '2024-02-06 05:26:11', NULL),
(13, 'aaｍvi110@gmail.com', '12345678', NULL, '2024-02-07 05:03:02', NULL),
(14, 'aaa@11.com', NULL, NULL, '2024-02-07 04:56:40', NULL),
(15, 'saefsfdsf@fvss.sv', 'rxafjdcvgsdhf', NULL, '2024-02-07 05:04:55', NULL),
(16, 'rhlkr7474@gmail.com', '123456', NULL, '2024-02-07 05:21:55', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_tbl`
--
ALTER TABLE `user_tbl`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_tbl`
--
ALTER TABLE `user_tbl`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ユーザ主キー', AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

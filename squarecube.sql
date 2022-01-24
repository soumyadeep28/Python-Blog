-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2022 at 07:08 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `squarecube`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(165) NOT NULL,
  `phone` int(13) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone`, `msg`, `date`) VALUES
(1, 'Blank Post', 'This is the first post', 123456789, 'blank msg', '2022-01-22 07:44:19'),
(2, 'soumya', 'ssg@gmail.com', 25834889, 'super cool hai humm', '0000-00-00 00:00:00'),
(3, 'shaon', 'gmail@gmail.com', 123456789, 'super cool hai hum', '0000-00-00 00:00:00'),
(4, 'susrut', 'susrut@gmail.com', 123654987, 'password de', '2022-01-22 12:49:55'),
(5, 'Ramakrishna', 'soumyadeepsen97@gmail.com', 25834776, 'goooooood morning guys', '2022-01-23 13:35:14'),
(6, 'Ramakrishna', 'soumyadeepsen97@gmail.com', 25834776, 'goooooood morning guys', '2022-01-23 13:45:16'),
(7, 'Ramakrishna', 'soumyadeepsen97@gmail.com', 25834776, 'goooooood morning guys', '2022-01-23 13:50:00'),
(8, 'Ramakrishna', 'soumyadeepsen97@gmail.com', 25834776, 'goooooood morning guys', '2022-01-23 13:50:49'),
(9, 'super', 'soumyadeepbest@gmail.com', 123654789, 'goood morning', '2022-01-23 13:52:19'),
(10, 'super', 'soumyadeepbest@gmail.com', 123654789, 'goood morning', '2022-01-23 13:58:56'),
(11, 'super', 'soumyadeepbest@gmail.com', 123654789, 'goood morning', '2022-01-23 13:59:28'),
(12, 'super', 'soumyadeepbest@gmail.com', 25834776, 'mail testing\r\n', '2022-01-23 14:03:27'),
(13, 'soumya', 'soumyadeepsen97@gmail.com', 25834776, 'good mornig', '2022-01-23 14:08:38'),
(14, 'soumya', 'soumyadeepsen97@gmail.com', 25834776, 'good mornig', '2022-01-23 14:12:17'),
(15, 'soumya', 'soumyadeepsen97@gmail.com', 25834776, 'good mornig', '2022-01-23 14:12:54'),
(16, 'supercool', 'soumyadeepsen97@gmail.com', 123456987, 'super ', '2022-01-23 14:13:31'),
(17, 'sajna', 'soumyadepps@gmail.com', 123456, 'sdfmjsdfkmsdf', '2022-01-23 14:16:54'),
(18, 'sajna', 'soumyadepps@gmail.com', 123456, 'sdfmjsdfkmsdf', '2022-01-23 14:18:12'),
(19, 'soumya', 'soumyadeepbest@gmail.com', 123654789, 'boss', '2022-01-23 14:19:24'),
(20, 'soumya', 'soumyadeepbest@gmail.com', 123654789, 'boss', '2022-01-23 14:20:56'),
(21, 'name', 'soumyadeepsen97@gmail.com', 2147483647, 'password de', '2022-01-23 14:21:25'),
(22, 'name', 'soumyadeepsen97@gmail.com', 2147483647, 'password de', '2022-01-23 14:22:06'),
(23, 'name', 'soumyadeepsen97@gmail.com', 2147483647, 'password de', '2022-01-23 19:34:56');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` varchar(500) NOT NULL,
  `date` int(11) NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'super updated post', 'updated-one', 'updating', 2022, 'images.jpg'),
(2, '2nd post', '2ndpost', ' 2nd post and now it is updating', 2022, 'about-bg.jpg'),
(4, 'super title', 'admin-pass', 'content', 2022, 'images.jpg'),
(5, 'Post 5', 'Post-5', 'Post 5', 0, 'Post 5'),
(6, 'Post 6', 'Post-6', 'Post 6', 20220124, 'Post 5'),
(7, 'Post 7', 'post7', 'Post7', 20220124, 'img.jpeg'),
(8, 'Post 8', 'post6', 'wow tu greta', 20220124, 'imga.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

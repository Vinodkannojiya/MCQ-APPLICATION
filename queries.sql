CREATE DATABASE learning;
drop table `learning`.`question_table`;
CREATE TABLE `learning`.`question_table` (
  `question_id` BIGINT NOT NULL AUTO_INCREMENT,
  `subject_name` VARCHAR(45) NOT NULL,
  `question_number` INT NOT NULL,
  `question` VARCHAR(45) NOT NULL,
  `option1` VARCHAR(45) NOT NULL,
  `option2` VARCHAR(45) NOT NULL,
  `option3` VARCHAR(45) NOT NULL,
  `option4` VARCHAR(45) NOT NULL,
  `answer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`question_id`));

insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',1,'WATER MEANING IS','A','PANI','C','D','PANI');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',2'BED MEANING IS ','PALANG','B','C','D','PALANG');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',3'ALMARI MEANING IS','ALMIRA','B','C','D','ALMIRA');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',4'MOBILE MEANING IS','A','B','C','MOBILE','MOBILE');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',5'LAPTOP MEANING IS','A','B','LAPTOP','D','LAPTOP');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',6'CHARGER MEANING IS ','A','B','C','CHARGER','CHARGER');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',7'TYPING MEANING IS ','TYPING','B','C','D','TYPING');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',8'POSTER MEANING IS ','A','POSTER','C','D','POSTER');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',9'CURTAIN MEANING IS ','A','B','CURTAIN','D','CURTAIN');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_01',10'WINDOW MEANING IS','WINDOW','B','C','D','WINDOW');

insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',1,'WATER MEANING IS','A','PANI','C','D','PANI');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',2,'BED MEANING IS ','PALANG','B','C','D','PALANG');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',3,'ALMARI MEANING IS','ALMIRA','B','C','D','ALMIRA');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',4,'MOBILE MEANING IS','A','B','C','MOBILE','MOBILE');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',5,'LAPTOP MEANING IS','A','B','LAPTOP','D','LAPTOP');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',6,'WATER MEANING IS','A','PANI','C','D','PANI');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',7,'BED MEANING IS ','PALANG','B','C','D','PALANG');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',8,'ALMARI MEANING IS','ALMIRA','B','C','D','ALMIRA');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',9,'MOBILE MEANING IS','A','B','C','MOBILE','MOBILE');
insert into `learning`.`question_table` (subject_name,question_number,question,option1,option2,option3,option4,answer) values ('ENGLISH_02',10,'LAPTOP MEANING IS','A','B','LAPTOP','D','LAPTOP');

drop table `learning`.`result_table`;
CREATE TABLE `learning`.`result_table` (
  `result_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `subject_name` VARCHAR(45) NOT NULL,
  `date_of_exam` TIMESTAMP NOT NULL,
  `score` INT NOT NULL,
  `total` INT NOT NULL,
  `percentage` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`result_id`));

insert into   `learning`.`result_table` (user_name,subject_name,date_of_exam,score,total,percentage) values ('vinod','ENGLISH_01','2022-08-08',9,10,90.00);
insert into   `learning`.`result_table` (user_name,subject_name,date_of_exam,score,total,percentage) values ('vinod','ENGLISH_02','2022-08-09',9,10,90.00);

CREATE TABLE `learning`.`user_table` (
  `user_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`));

  CREATE TABLE `learning`.`user_table` (
  `user_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`));

drop table `learning`.`response_table`;
CREATE TABLE `learning`.`response_table` (
  `response_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `subject_name` VARCHAR(45) NOT NULL,
  `date_of_exam` TIMESTAMP NOT NULL,
  `res1` VARCHAR(45) NOT NULL,
  `res2` VARCHAR(45) NOT NULL,
  `res3` VARCHAR(45) NOT NULL,
  `res4` VARCHAR(45) NOT NULL,
  `res5` VARCHAR(45) NOT NULL,
  `res6` VARCHAR(45) NOT NULL,
  `res7` VARCHAR(45) NOT NULL,
  `res8` VARCHAR(45) NOT NULL,
  `res9` VARCHAR(45) NOT NULL,
  `res10` VARCHAR(45) NOT NULL,
   PRIMARY KEY (`response_id`));

drop table `learning`.`answer_table`;
CREATE TABLE `learning`.`answer_table` (
  `answer_id` BIGINT NOT NULL AUTO_INCREMENT,
  `subject_name` VARCHAR(1000) NOT NULL,
  `ans1` VARCHAR(1000) NOT NULL,
  `ans2` VARCHAR(1000) NOT NULL,
  `ans3` VARCHAR(1000) NOT NULL,
  `ans4` VARCHAR(1000) NOT NULL,
  `ans5` VARCHAR(1000) NOT NULL,
  `ans6` VARCHAR(1000) NOT NULL,
  `ans7` VARCHAR(1000) NOT NULL,
  `ans8` VARCHAR(1000) NOT NULL,
  `ans9` VARCHAR(1000) NOT NULL,
  `ans10` VARCHAR(1000) NOT NULL,
   PRIMARY KEY (`answer_id`));

insert into   `learning`.`answer_table` (subject_name, ans1, ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10) values ('ENGLISH_01','PANI','PALANG','ALMIRA','MOBILE','LAPTOP','CHARGER','TYPING','POSTER','CURTAIN','WINDOW');
insert into   `learning`.`answer_table` (subject_name, ans1, ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10) values ('ENGLISH_02','PANI','PALANG','ALMIRA','MOBILE','LAPTOP','CHARGER','TYPING','POSTER','CURTAIN','WINDOW');



drop table `learning`.`user_table`;
CREATE TABLE `learning`.`user_table` (
  `user_id` BIGINT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(1000) NOT NULL,
  `password` VARCHAR(1000) NOT NULL,
   PRIMARY KEY (`user_id`));






select sum(case
    when a.ans1 == b.res1 then 1 else 0
    when a.ans2 == b.res2 then 1 else 0
    when a.ans3 == b.res3 then 1 else 0
    when a.ans4 == b.res4 then 1 else 0
    when a.ans5 == b.res5 then 1 else 0
    when a.ans6 == b.res6 then 1 else 0
    when a.ans7 == b.res7 then 1 else 0
    when a.ans8 == b.res8 then 1 else 0
    when a.ans9 == b.res9 then 1 else 0
    when a.ans10 == b.res10 then 1 else 0
end ) score , '10' total,
from answer_table a inner join response_table on a.sub_name =b.sub_name
where user_name = 'vinod' and response_id = (select (max(response_id) from response_table))
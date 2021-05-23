insert into api_user_types (user_type_name)
values
('Student'),
('Teacher')

insert into api_users (full_name, email, "password", user_type_id, birthday, gender) values
('Tôn Thất Quỳnh Anh', '0@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Nguyễn Thị Minh Châu', '1@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Trần Văn Thanh Công', '2@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Huỳnh Bá Cường', '3@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Trần Thế Dâng', '4@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Nguyễn Tiến Đạt', '5@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Phan Thị Diễm', '6@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Phan Khương Duy', '7@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Đỗ Trung Hiếu', '8@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Nguyễn Nguyên Hoàng', '9@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Đặng Quang Huy', '10@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Nguyễn Hồng Huy', '11@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Nguyễn Văn Quang Huy', '12@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Trần Văn Huy', '13@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Đỗ Oanh Khải', '14@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Đỗ Văn Anh Khoa', '15@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Phạm Mai Văn Lai', '16@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Châu Trường Long', '17@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Lương Thế Long', '18@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Trần Chí Minh', '19@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Đặng Bảo Ngân', '20@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Nguyễn Xuân Nghĩa', '21@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Bùi An Nguyên', '22@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Đỗ Lý Nhân', '23@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Phan Minh Phú', '24@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Nguyễn Xuân Phương', '25@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Nguyễn Phước Quốc', '26@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Nguyễn Đặng Trường Sơn', '27@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Nguyễn Đức Tài', '28@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Lê Đức Thiết', '29@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Lê Quang Thông', '30@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Huỳnh Trần Khánh Toàn', '31@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Võ Minh Trí', '32@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Lê Tiến Trung', '33@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Phan Anh Tú', '34@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Lê Anh Tuấn', '35@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Phan Thế Tuệ', '36@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Mai Thế Viễn', '37@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Hồ Nguyên Vũ', '38@dut.udn.vn', '123', 1, '2000-01-01', 'male') ,
('Dương Thảo Vy', '39@dut.udn.vn', '123', 1, '2000-01-01', 'female') ,
('Phạm Minh Tuấn', '40@dut.udn.vn', '123', 2, '2000-01-01', 'female') ,
('Phạm Công Thắng', '41@dut.udn.vn', '123', 2, '2000-01-01', 'male') ;

insert into api_subjects (subject_name)
values
('Trí tuệ nhân tạo'),
('Lập trình Java'),
('Khoa học dữ liệu')

insert into api_classes (subject_id, teacher_id)
values
(1, 1),
(2, 1),
(3, 2)


insert into api_details_student_attend_class (student_id, course_id) 
values
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(3, 3);


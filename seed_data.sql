insert into api_user_types (user_type_name)
values
('Student'),
('Teacher')

insert into api_users (user_name, email, "password", user_type_id) values 
('Tôn Thất Quỳnh Anh', '0@pye.net', '123', 1), 
('Nguyễn Thị Minh Châu', '1@pye.net', '123', 1), 
('Trần Văn Thanh Công', '2@pye.net', '123', 1), 
('Huỳnh Bá Cường', '3@pye.net', '123', 1), 
('Trần Thế Dâng', '4@pye.net', '123', 1), 
('Nguyễn Tiến Đạt', '5@pye.net', '123', 1), 
('Phan Thị Diễm', '6@pye.net', '123', 1), 
('Phan Khương Duy', '7@pye.net', '123', 1), 
('Đỗ Trung Hiếu', '8@pye.net', '123', 1), 
('Nguyễn Nguyên Hoàng', '9@pye.net', '123', 1), 
('Đặng Quang Huy', '10@pye.net', '123', 1), 
('Nguyễn Hồng Huy', '11@pye.net', '123', 1), 
('Nguyễn Văn Quang Huy', '12@pye.net', '123', 1), 
('Trần Văn Huy', '13@pye.net', '123', 1), 
('Đỗ Oanh Khải', '14@pye.net', '123', 1), 
('Đỗ Văn Anh Khoa', '15@pye.net', '123', 1), 
('Phạm Mai Văn Lai', '16@pye.net', '123', 1), 
('Châu Trường Long', '17@pye.net', '123', 1), 
('Lương Thế Long', '18@pye.net', '123', 1), 
('Trần Chí Minh', '19@pye.net', '123', 1), 
('Đặng Bảo Ngân', '20@pye.net', '123', 1), 
('Nguyễn Xuân Nghĩa', '21@pye.net', '123', 1), 
('Bùi An Nguyên', '22@pye.net', '123', 1), 
('Đỗ Lý Nhân', '23@pye.net', '123', 1), 
('Phan Minh Phú', '24@pye.net', '123', 1), 
('Nguyễn Xuân Phương', '25@pye.net', '123', 1), 
('Nguyễn Phước Quốc', '26@pye.net', '123', 1), 
('Nguyễn Đặng Trường Sơn', '27@pye.net', '123', 1), 
('Nguyễn Đức Tài', '28@pye.net', '123', 1), 
('Lê Đức Thiết', '29@pye.net', '123', 1), 
('Lê Quang Thông', '30@pye.net', '123', 1), 
('Huỳnh Trần Khánh Toàn', '31@pye.net', '123', 1), 
('Võ Minh Trí', '32@pye.net', '123', 1), 
('Lê Tiến Trung', '33@pye.net', '123', 1), 
('Phan Anh Tú', '34@pye.net', '123', 1), 
('Lê Anh Tuấn', '35@pye.net', '123', 1), 
('Phan Thế Tuệ', '36@pye.net', '123', 1), 
('Mai Thế Viễn', '37@pye.net', '123', 1), 
('Hồ Nguyên Vũ', '38@pye.net', '123', 1), 
('Dương Thảo Vy', '39@pye.net', '123', 1),
('Phạm Minh Tuấn', '40@pye.net', '123', 2),
('Phạm Công Thắng', '41@pye.net', '123', 2);

insert into api_subjects (subject_name)
values
('Trí tuệ nhân tạo'),
('Lập trình Java'),
('Khoa học dữ liệu')

--insert into api_class (class_name, subject_id, teacher_id)
--values
--('18N15',)
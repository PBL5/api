insert into api_user_types (user_type_name)
values
('Student'),
('Teacher')

insert into api_users (full_name, email, "password", user_type_id) values 
('Tôn Thất Quỳnh Anh', '0@dut.udn.vn', '123', 1), 
('Nguyễn Thị Minh Châu', '1@dut.udn.vn', '123', 1), 
('Trần Văn Thanh Công', '2@dut.udn.vn', '123', 1), 
('Huỳnh Bá Cường', '3@dut.udn.vn', '123', 1), 
('Trần Thế Dâng', '4@dut.udn.vn', '123', 1), 
('Nguyễn Tiến Đạt', '5@dut.udn.vn', '123', 1), 
('Phan Thị Diễm', '6@dut.udn.vn', '123', 1), 
('Phan Khương Duy', '7@dut.udn.vn', '123', 1), 
('Đỗ Trung Hiếu', '8@dut.udn.vn', '123', 1), 
('Nguyễn Nguyên Hoàng', '9@dut.udn.vn', '123', 1), 
('Đặng Quang Huy', '10@dut.udn.vn', '123', 1), 
('Nguyễn Hồng Huy', '11@dut.udn.vn', '123', 1), 
('Nguyễn Văn Quang Huy', '12@dut.udn.vn', '123', 1), 
('Trần Văn Huy', '13@dut.udn.vn', '123', 1), 
('Đỗ Oanh Khải', '14@dut.udn.vn', '123', 1), 
('Đỗ Văn Anh Khoa', '15@dut.udn.vn', '123', 1), 
('Phạm Mai Văn Lai', '16@dut.udn.vn', '123', 1), 
('Châu Trường Long', '17@dut.udn.vn', '123', 1), 
('Lương Thế Long', '18@dut.udn.vn', '123', 1), 
('Trần Chí Minh', '19@dut.udn.vn', '123', 1), 
('Đặng Bảo Ngân', '20@dut.udn.vn', '123', 1), 
('Nguyễn Xuân Nghĩa', '21@dut.udn.vn', '123', 1), 
('Bùi An Nguyên', '22@dut.udn.vn', '123', 1), 
('Đỗ Lý Nhân', '23@dut.udn.vn', '123', 1), 
('Phan Minh Phú', '24@dut.udn.vn', '123', 1), 
('Nguyễn Xuân Phương', '25@dut.udn.vn', '123', 1), 
('Nguyễn Phước Quốc', '26@dut.udn.vn', '123', 1), 
('Nguyễn Đặng Trường Sơn', '27@dut.udn.vn', '123', 1), 
('Nguyễn Đức Tài', '28@dut.udn.vn', '123', 1), 
('Lê Đức Thiết', '29@dut.udn.vn', '123', 1), 
('Lê Quang Thông', '30@dut.udn.vn', '123', 1), 
('Huỳnh Trần Khánh Toàn', '31@dut.udn.vn', '123', 1), 
('Võ Minh Trí', '32@dut.udn.vn', '123', 1), 
('Lê Tiến Trung', '33@dut.udn.vn', '123', 1), 
('Phan Anh Tú', '34@dut.udn.vn', '123', 1), 
('Lê Anh Tuấn', '35@dut.udn.vn', '123', 1), 
('Phan Thế Tuệ', '36@dut.udn.vn', '123', 1), 
('Mai Thế Viễn', '37@dut.udn.vn', '123', 1), 
('Hồ Nguyên Vũ', '38@dut.udn.vn', '123', 1), 
('Dương Thảo Vy', '39@dut.udn.vn', '123', 1),
('Phạm Minh Tuấn', '40@dut.udn.vn', '123', 2),
('Phạm Công Thắng', '41@dut.udn.vn', '123', 2);

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

insert into api_details_student_attend_class (student_id, class_id) 
values
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(3, 3);


# Recruitment & HR Management API

Tài liệu này hướng dẫn người dùng cách chạy, đăng nhập và test toàn bộ API của hệ thống Recruitment & HR Management bằng Swagger UI hoặc công cụ như Postman.

## Mục lục
1. Mục đích tài liệu
2. Yêu cầu trước khi sử dụng
3. Chạy hệ thống
4. Mở tài liệu API
5. Quy trình test đầy đủ
6. Test từng nhóm API
7. Cách truyền JWT token
8. Dữ liệu mẫu để test
9. Các lỗi thường gặp
10. Gợi ý quy trình demo
    
## 1. Mục đích tài liệu

**Tài liệu này giúp bạn:**

- Chạy project trên máy local
- Đăng ký và đăng nhập hệ thống
- Lấy token JWT
- Test đầy đủ các module:
Auth
Users
Candidates
Jobs
Applications
Interviews
Employees
Integrations
- Hiểu luồng nghiệp vụ tuyển dụng từ đầu đến cuối
## 2. Yêu cầu trước khi sử dụng

**Trước khi test API, cần chuẩn bị:**

- Python 3.10 trở lên
- Đã clone source code project
- Đã cài dependencies bằng requirements.txt
- Có môi trường ảo venv hoặc .venv
- Có file .env nếu project dùng config môi trường
- Có kết nối internet nếu muốn test tích hợp bên ngoài
## 3. Chạy hệ thống
### Bước 1: kích hoạt môi trường ảo**
``` bash
Windows

.venv\Scripts\activate
```

``` bash
Linux / macOS

source .venv/bin/activate
```
### Bước 3: Cài dependencies
``` bash
pip install -r requirements.txt
```
### Bước 3: chạy server**
``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
**Bước 4: kiểm tra server**
``` bash
Mở trình duyệt:

API root: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
```
``` bash
uvicorn app.main:app --reload --port 8001
```
## 4. Mở tài liệu API

**Project hỗ trợ Swagger UI để test trực tiếp.**

Swagger UI

``` bash
Truy cập:

http://127.0.0.1:8000/docs
```

**Tại đây bạn có thể:**

- Xem danh sách endpoint
- Nhập request body
- Bấm Execute để test
- Xem response trả về
## 5. Quy trình test đầy đủ

**Để test đầy đủ luồng nghiệp vụ, nên thực hiện theo đúng thứ tự dưới đây:**

- Đăng ký tài khoản
- Đăng nhập để lấy JWT token
- Gọi GET /users/me
- Tạo candidate
- Tạo job
- Tạo application
- Tạo interview
- Tạo employee
- Test các API integration nếu đã cấu hình

**Đây là luồng test khuyến nghị vì các module có liên kết dữ liệu với nhau.**

## 6. VÍ DỤ test API
### Đăng ký tài khoản

#### Endpoint
``` bash
POST /api/v1/auth/register
```

#### Request body
``` bash
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "123456",
  "role": "admin"
}
```
### Tạo ứng viên

#### Endpoint
``` bash
POST /api/v1/candidates
```

#### Request body
``` bash

{
  "full_name": "Nguyen Van A",
  "email": "nguyenvana@gmail.com",
  "phone": "0900000000",
  "linkedin_url": "https://linkedin.com/in/nguyenvana",
  "cv_url": "https://example.com/cv-a.pdf",
  "skills": "Python, FastAPI, SQL",
  "experience_years": 2
}
```

### Kết quả mong đợi

- Tạo ứng viên thành công
- Response trả về có id

 ## 7. Dữ liệu mẫu để test

 Bạn có thể dùng bộ dữ liệu mẫu sau để test nhanh.

### User admin
``` bash
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "123456",
  "role": "admin"
}
```
### User interviewer
``` bash
{
  "username": "interviewer01",
  "email": "interviewer01@example.com",
  "password": "123456",
  "role": "interviewer"
}
```
### Candidate
``` bash
{
  "full_name": "Tran Van B",
  "email": "tranvanb@gmail.com",
  "phone": "0911111111",
  "linkedin_url": "https://linkedin.com/in/tranvanb",
  "cv_url": "https://example.com/cv-b.pdf",
  "skills": "Python, FastAPI, PostgreSQL",
  "experience_years": 3
}
```
### Job
``` bash
{
  "title": "Python Backend Developer",
  "department": "IT",
  "description": "Develop APIs and backend services",
  "requirements": "Python, FastAPI, SQLAlchemy",
  "salary_min": 1200,
  "salary_max": 2500,
  "status": "open"
}
```

# Recruitment & HR Management API 

Microservice cho hệ thống tuyển dụng & nhân sự:

- Quản lý ứng viên (candidates)
- Quản lý tin tuyển dụng (Jobs)
- Quản lý hồ sơ ứng tuyển (Applications)
- Lên lịch phỏng vấn (Interviews)
- Quản lý nhân sự (Employees)
- Tích hợp Email, Google Calendar, LinkedIn

## Tính năng

- **Tích hợp Google Calendar**: Quản lý sự kiện lịch qua `calendar.js`
- **Tích hợp Gmail**: Xử lý các thao tác email qua `gmail.js`
- **Tích hợp LinkedIn**: Kết nối với các dịch vụ LinkedIn qua `linkedin.js`
- **Máy chủ Express**: Máy chủ API RESTful chạy trên cổng 8000 (có thể cấu hình)
- **Hỗ trợ dịch vụ Windows**: Có thể cài đặt như một dịch vụ Windows bằng `node-windows`


## Cài đặt

1. Sao chép kho lưu trữ:
   ```bash
   git clone https://github.com/Trantoan-blip/toanAPI.git
   cd SOA/src
   ```

2. Cài đặt các phụ thuộc:
   ```bash
   npm install
   ```
3. Thiết lập biến môi trường:
   - Thêm các khóa API và cấu hình của bạn:
     ```
     GOOGLE_CLIENT_ID=your_google_client_id
     GOOGLE_CLIENT_SECRET=your_google_client_secret
     LINKEDIN_API_KEY=your_linkedin_api_key
     PORT=3000
     ```

## Sử dụng

### Phát triển
```bash
npm run dev
```

### Sản xuất
```bash
npm start
```

## Cấu trúc dự án

```
app/
├── api/            # API endpoints
├── core/           # Config, DB, Security
├── models/         # Database models
├── schemas/        # Request/Response schemas
├── services/       # Business logic & integrations
├── utils/          # Enums, helpers
└── main.py         # Entry point
```

## Cấu hình

Cấu hình ứng dụng bằng biến môi trường trong `.env.example`:

- `PORT`: Cổng máy chủ (mặc định: 8000)
- `GOOGLE_CLIENT_ID`: ID khách hàng Google API
- `GOOGLE_CLIENT_SECRET`: Bí mật khách hàng Google API
- `LINKEDIN_API_KEY`: Khóa API LinkedIn

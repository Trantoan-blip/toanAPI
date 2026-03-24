# Recruitment & HR Management API (FastAPI)

Microservice cho hệ thống tuyển dụng & nhân sự:

- Quản lý ứng viên (Candidates)
- Quản lý tin tuyển dụng (Jobs)
- Quản lý hồ sơ ứng tuyển (Applications)
- Lên lịch phỏng vấn (Interviews)
- Quản lý nhân sự (Employees)
- Tích hợp Email, Google Calendar, LinkedIn

---

## 1) Cài đặt

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
2) Chạy service
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

API docs:

Swagger UI: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
3) Các endpoint chính
POST /api/v1/auth/register
POST /api/v1/auth/login
GET /api/v1/users/me
Candidates
GET /api/v1/candidates
POST /api/v1/candidates
PUT /api/v1/candidates/{id}
DELETE /api/v1/candidates/{id}
Jobs
GET /api/v1/jobs
POST /api/v1/jobs
PUT /api/v1/jobs/{id}
DELETE /api/v1/jobs/{id}
Applications
GET /api/v1/applications
POST /api/v1/applications
PUT /api/v1/applications/{id}
DELETE /api/v1/applications/{id}
Interviews
GET /api/v1/interviews
POST /api/v1/interviews
PUT /api/v1/interviews/{id}
DELETE /api/v1/interviews/{id}
Employees
GET /api/v1/employees
POST /api/v1/employees
PUT /api/v1/employees/{id}
DELETE /api/v1/employees/{id}
Integrations
POST /api/v1/integrations/linkedin/import-profile
POST /api/v1/integrations/linkedin/publish-job
POST /api/v1/integrations/email/send
POST /api/v1/integrations/calendar/create-event
4) Ví dụ request tạo interview
{
  "application_id": 1,
  "interviewer_id": 2,
  "start_time": "2026-03-25T10:00:00",
  "end_time": "2026-03-25T11:00:00",
  "location": "Online",
  "type": "online"
}

👉 Hệ thống sẽ:

Tạo Google Calendar event
Sinh meeting link
Gửi email cho ứng viên
5) Chạy test
pytest -q
6) Gợi ý tích hợp hệ thống
ESB / Microservice architecture
Queue (RabbitMQ / Kafka) cho email & notification
Background worker (Celery / Redis)
Logging & monitoring (ELK, Prometheus)

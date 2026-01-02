<h1 align="center">MyBigNumber - Large Number Addition</h1>

## Bài toán

Tình huống đặt ra là bạn được giao việc viết hàm cài đặt thuật toán cộng 2 số lớn (được biểu diễn dưới dạng chuỗi) với thuật toán như học sinh Tiểu học 
đã làm.
Hàm này sẽ được đóng gói để bàn giao cho một nhóm khác làm giao diện (hoặc ứng dụng dạng console) để họ gọi hàm của bạn trong dự án lớn hơn.

## Yêu cầu

- Python 3.7+
- Flask 3.0.0+

## Cấu trúc project

```
mybignumber/
├── src/
│   ├── __init__.py
│   └── mybignumber.py      
├── api/
│   ├── __init__.py
│   └── app.py              
├── tests/
│   ├── __init__.py
│   └── test_mybignumber.py # Unit tests
├── requirements.txt
├── README.md
└── .gitignore
```

## Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd mybignumber
```

### 2. Tạo virtual environment

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

## Sử dụng

### Task 1

#### Chạy demo

```bash
python src/mybignumber.py
```

#### Chạy tests

```bash
python tests/test_mybignumber.py
```

### Task 2

#### Khởi động server

```bash
python api/app.py
```

Server chạy tại: `http://localhost:5000`

#### Test API

**1. GET / - API Documentation**
```bash
curl http://localhost:5000/
```

**2. POST /add - Cộng 2 số (JSON)**
```bash
curl -X POST http://localhost:5000/add \
  -H "Content-Type: application/json" \
  -d '{"num1": "1234", "num2": "897"}'
```

Response:
```json
{
  "num1": "1234",
  "num2": "897",
  "result": "2131",
  "success": true
}
```

## Unit Tests

Chạy tất cả tests:

```bash
python tests/test_mybignumber.py
```

## Git Branches

- **core**: Task 1 - Core implementation
- **api**: Task 2 - Flask API

## 📝 API Documentation

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/add` | Cộng hai số(JSON) |
| GET | `/add_get` | Cộng hai số(query params) |

---
**LIÊN HỆ**
---
Cảm ơn bạn đã ghé thăm dự án của tôi❤️

Nếu bạn muốn kết nối, đừng ngần ngại liên hệ với tôi nhé!

📧 Email: ndtoan.work@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/ndtoanwork/

📍 Địa điểm: Bình Thạnh, TP. Hồ Chí Minh, Việt Nam
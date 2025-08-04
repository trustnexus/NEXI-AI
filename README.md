# NEXI Backend API

A FastAPI-based backend for NEXI IoT device management system with user authentication and PostgreSQL database.

## Features

- User Authentication (Register/Login)
- JWT-based Token System
- PostgreSQL Database Models
- CORS Support for Frontend
- Swagger UI Documentation
- Docker Support
- **Week 3: File Upload APIs** (Voice & Face)
- **Week 3: Device Status API** (Dummy Data)

## Database Models

- **User**: User accounts with authentication
- **NexiDevice**: IoT devices managed by users
- **Log**: System logs and device events

## Quick Start

### 1. Environment Setup

Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=postgresql+asyncpg://postgres:1234@localhost/NEXI_db

# JWT Configuration
SECRET_KEY=your-super-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Server Configuration
PORT=8000
```

### 2. Using Docker (Recommended)

```bash
# Start the application with PostgreSQL
docker-compose up --build

# The API will be available at http://localhost:8000
# Swagger UI at http://localhost:8000/docs
```

### 3. Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Start PostgreSQL (make sure it's running on port 5432)

# Initialize database tables
python init_db.py

# Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user info (requires authentication)

### Upload APIs (Week 3)

- `POST /upload/voice` - Upload voice audio file (MP3/WAV)
- `POST /upload/face` - Upload face image file (JPG/PNG)

### Status API (Week 3)

- `GET /status/` - Get status for all devices (dummy data)
- `GET /status/{device_id}` - Get status for specific device (dummy data)

### Example Usage

#### Register a User
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpassword123"
  }'
```

#### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpassword123"
  }'
```

#### Get User Info (with token)
```bash
curl -X GET "http://localhost:8000/auth/me" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### Upload Voice File
```bash
curl -X POST "http://localhost:8000/upload/voice" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "file=@your_voice_file.mp3"
```

#### Upload Face Image
```bash
curl -X POST "http://localhost:8000/upload/face" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "file=@your_face_image.jpg"
```

#### Get Device Status
```bash
curl -X GET "http://localhost:8000/status/NEXI_DEVICE_001" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Testing

Run the test script to verify authentication:

```bash
python test_auth.py
```

### Week 3 API Testing

Run the comprehensive test script for Week 3 APIs:

```bash
python test_week3_apis.py
```

This will test:
- Authentication
- Upload APIs (voice and face)
- Status APIs (all devices and specific device)
- File storage in `/media` directory

## Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique)
- `hashed_password`
- `is_active`
- `is_superuser`
- `created_at`
- `updated_at`

### NexiDevices Table
- `id` (Primary Key)
- `device_id` (Unique)
- `name`
- `device_type`
- `status`
- `location`
- `configuration` (JSON)
- `owner_id` (Foreign Key to Users)
- `created_at`
- `updated_at`

### Logs Table
- `id` (Primary Key)
- `level`
- `message`
- `details` (JSON)
- `user_id` (Foreign Key to Users)
- `device_id` (Foreign Key to NexiDevices)
- `created_at`

## Development

### Project Structure
```
NEXI_Backend/
├── config/          # Configuration settings
├── core/            # Database and core functionality
├── models/          # SQLAlchemy database models
├── routers/         # API route handlers
├── services/        # Business logic and utilities
├── media/           # Uploaded files storage
│   ├── voice/       # Voice files (MP3/WAV)
│   └── face/        # Face images (JPG/PNG)
├── main.py          # FastAPI application entry point
├── requirements.txt # Python dependencies
├── docker-compose.yml # Docker configuration
└── Dockerfile       # Docker image definition
```

### Adding New Endpoints

1. Create a new router in `routers/`
2. Import and include it in `main.py`
3. Add authentication if needed using `Depends(get_current_user)`

## Security Notes

- Change the `SECRET_KEY` in production
- Use strong passwords
- Enable HTTPS in production
- Regularly update dependencies

## License

This project is part of the NEXI IoT Management System. 
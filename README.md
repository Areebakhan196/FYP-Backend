# The Silent Reporter: Anonymous Audio & Text Complaint System

A production-ready, industry-level backend for anonymous reporting, built with Django REST Framework.

## Features
- **True Anonymity**: No IP addresses or user metadata are stored.
- **AES Encryption**: Sensitive text content is encrypted before storage in MySQL.
- **Dual-Mode Submission**: Supports both JSON (Text) and Multi-part form data (Audio + Images).
- **Unique Tracking ID**: Secure, non-sequential IDs for status tracking.
- **Modular Architecture**: Separate apps for Complaints, Security, Administration, and Analytics.
- **Rate Limiting**: Protection against spam and brute force.
- **Audio Processing**: Placeholder integration for audio normalization and metadata stripping.

## Tech Stack
- **Framework**: Django 4.2+ (DRF)
- **Database**: MySQL
- **Security**: Cryptography (Fernet/AES)
- **File Handling**: Pydub for audio processing

## Project Structure
```
silent_reporter/
├── core/               # Project configuration & Global handlers
├── complaints/         # Core reporting logic & ID generation
├── security/           # Encryption/Decryption utilities
├── administration/     # Admin dashboard APIs
├── analytics/          # Reporting summaries
├── media/              # Secure file storage
└── logs/               # System event logs
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd silent_reporter
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-django-secret-key
DATABASE_URL=mysql://user:password@localhost:3306/db_name
ENCRYPTION_KEY=your-32-byte-base64-fernet-key
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (for Admin access)
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

## API Documentation

### Public Endpoints
- **Submit Complaint**: `POST /api/complaints/submit/`
    - Accepts: `multipart/form-data` or `application/json`
    - Fields: `text_content`, `audio_file`, `evidence_image`
- **Check Status**: `GET /api/complaints/status/<tracking_id>/`

### Admin Endpoints (Requires Authentication)
- **List Complaints**: `GET /api/management/complaints/`
- **Complaint Details**: `GET /api/management/complaints/<tracking_id>/` (Shows decrypted text)
- **Update Status**: `PATCH /api/management/complaints/<tracking_id>/update/`
    - Fields: `status` (`PENDING`, `UNDER_REVIEW`, `RESOLVED`)
- **Analytics Summary**: `GET /api/analytics/summary/`

## Security Measures
- **Data Privacy**: `ANONYMITY_STRICT` mode ensures no PII is captured.
- **Encryption**: AES-256 equivalent (Fernet) for database-level encryption.
- **Rate Limiting**: Default 5 requests per minute for submissions.
- **SQLi Protection**: Django ORM handles query parameterization.

## License
MIT License

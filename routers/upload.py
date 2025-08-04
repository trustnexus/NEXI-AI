from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
import shutil
from datetime import datetime
from typing import Optional
from routers.auth import get_current_user
from models import User

router = APIRouter()

# Create media directory if it doesn't exist
MEDIA_DIR = "media"
os.makedirs(MEDIA_DIR, exist_ok=True)

# Create subdirectories for different file types
VOICE_DIR = os.path.join(MEDIA_DIR, "voice")
FACE_DIR = os.path.join(MEDIA_DIR, "face")
os.makedirs(VOICE_DIR, exist_ok=True)
os.makedirs(FACE_DIR, exist_ok=True)

# Allowed file extensions
ALLOWED_VOICE_EXTENSIONS = {".mp3", ".wav"}
ALLOWED_FACE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

def get_file_extension(filename: str) -> str:
    """Extract file extension from filename."""
    return os.path.splitext(filename.lower())[1]

def is_valid_voice_file(filename: str) -> bool:
    """Check if the file is a valid voice file."""
    return get_file_extension(filename) in ALLOWED_VOICE_EXTENSIONS

def is_valid_face_file(filename: str) -> bool:
    """Check if the file is a valid face image file."""
    return get_file_extension(filename) in ALLOWED_FACE_EXTENSIONS

@router.post("/voice")
async def upload_voice(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    Upload voice audio file (MP3/WAV)
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    if not is_valid_voice_file(file.filename):
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_VOICE_EXTENSIONS)}"
        )
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = get_file_extension(file.filename)
    unique_filename = f"voice_{current_user.id}_{timestamp}{file_extension}"
    file_path = os.path.join(VOICE_DIR, unique_filename)
    
    try:
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Voice file uploaded successfully",
                "filename": unique_filename,
                "original_filename": file.filename,
                "file_size": os.path.getsize(file_path),
                "uploaded_by": current_user.username,
                "uploaded_at": timestamp
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

@router.post("/face")
async def upload_face(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    """
    Upload face image file (JPG/PNG)
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    if not is_valid_face_file(file.filename):
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_FACE_EXTENSIONS)}"
        )
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = get_file_extension(file.filename)
    unique_filename = f"face_{current_user.id}_{timestamp}{file_extension}"
    file_path = os.path.join(FACE_DIR, unique_filename)
    
    try:
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Face image uploaded successfully",
                "filename": unique_filename,
                "original_filename": file.filename,
                "file_size": os.path.getsize(file_path),
                "uploaded_by": current_user.username,
                "uploaded_at": timestamp
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}") 
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
import random
from datetime import datetime
from routers.auth import get_current_user
from models import User

router = APIRouter()

# Sample status data
STATUS_OPTIONS = ["Idle", "Active", "Needs Attention"]

def get_dummy_device_status(device_id: str) -> Dict[str, Any]:
    """
    Generate dummy status data for a device
    """
    # Generate random status based on device_id for consistency
    random.seed(hash(device_id) % 1000)
    
    status = random.choice(STATUS_OPTIONS)
    timestamp = datetime.now().isoformat()
    
    # Generate additional dummy data based on status
    if status == "Idle":
        battery_level = random.randint(80, 100)
        temperature = random.uniform(20.0, 25.0)
        last_activity = "2 hours ago"
    elif status == "Active":
        battery_level = random.randint(40, 80)
        temperature = random.uniform(25.0, 35.0)
        last_activity = "5 minutes ago"
    else:  # Needs Attention
        battery_level = random.randint(10, 40)
        temperature = random.uniform(35.0, 45.0)
        last_activity = "1 hour ago"
    
    return {
        "device_id": device_id,
        "status": status,
        "battery_level": battery_level,
        "temperature": round(temperature, 1),
        "last_activity": last_activity,
        "timestamp": timestamp,
        "is_online": status != "Needs Attention",
        "firmware_version": "1.2.3",
        "location": "Room 101",
        "device_type": "NEXI_Sensor_v2"
    }

@router.get("/{device_id}")
async def get_device_status(
    device_id: str,
    current_user: User = Depends(get_current_user)
):
    """
    Get device status by device ID
    Returns dummy status information for the specified device
    """
    if not device_id or len(device_id.strip()) == 0:
        raise HTTPException(status_code=400, detail="Device ID is required")
    
    try:
        status_data = get_dummy_device_status(device_id)
        return status_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get device status: {str(e)}")

@router.get("/")
async def get_all_devices_status(
    current_user: User = Depends(get_current_user)
):
    """
    Get status for all devices (dummy data)
    """
    # Generate dummy data for multiple devices
    devices = []
    for i in range(1, 6):  # Generate 5 dummy devices
        device_id = f"NEXI_DEVICE_{i:03d}"
        status_data = get_dummy_device_status(device_id)
        devices.append(status_data)
    
    return {
        "total_devices": len(devices),
        "devices": devices,
        "timestamp": datetime.now().isoformat()
    } 
import platform
import psutil
import subprocess
import json
from typing import Dict, Any

def get_host_info() -> str:
    """Get host information including system details, memory, and CPU information.
    
    Returns:
        str: The host information in JSON string format
    """
    info: Dict[str, Any] = {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "memory_gb": round(psutil.virtual_memory().total / (1024**3), 2),
    }

    # Get CPU count
    cpu_count = psutil.cpu_count(logical=True)
    info["cpu_count"] = cpu_count if cpu_count is not None else -1
    
    # Get CPU model (cross-platform)
    try:
        if platform.system() == "Darwin":  # macOS
            cpu_model = subprocess.check_output(
                ["sysctl", "-n", "machdep.cpu.brand_string"]
            ).decode().strip()
        elif platform.system() == "Windows":  # Windows
            cpu_model = platform.processor()
        else:  # Linux
            try:
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if line.startswith("model name"):
                            cpu_model = line.split(":")[1].strip()
                            break
                    else:
                        cpu_model = "Unknown"
            except:
                cpu_model = "Unknown"
        info["cpu_model"] = cpu_model
    except Exception:
        info["cpu_model"] = "Unknown"

    # Add memory usage info
    memory = psutil.virtual_memory()
    info["memory_used_gb"] = round(memory.used / (1024**3), 2)
    info["memory_percent"] = memory.percent
    
    # Add disk info
    try:
        disk = psutil.disk_usage('/')
        info["disk_total_gb"] = round(disk.total / (1024**3), 2)
        info["disk_used_gb"] = round(disk.used / (1024**3), 2)
        info["disk_percent"] = round((disk.used / disk.total) * 100, 2)
    except Exception:
        info["disk_info"] = "Unavailable"

    return json.dumps(info, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    print(get_host_info())
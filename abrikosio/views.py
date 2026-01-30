import subprocess
from datetime import datetime, timedelta
import os

import psutil
from django.http.response import HttpResponse, JsonResponse


def get_uptime():
    """
        Calculates and returns the uptime of the current Django process.
        """
    try:
        # Get the current process object
        process = psutil.Process(os.getpid())
        # Get the process creation time as a timestamp
        create_time_timestamp = process.create_time()
        create_time = datetime.fromtimestamp(create_time_timestamp)
        uptime = datetime.now() - create_time
        print(uptime)
        # Format the uptime into a readable string
        days, hours, minutes, seconds = uptime.days, uptime.seconds // 3600, (uptime.seconds // 60) % 60, uptime.seconds % 60
        return f"Django uptime {days} days, {hours:02}:{minutes:02}:{seconds:02}"

    except psutil.NoSuchProcess:
        return "Uptime not available (process not found)"
    except Exception as e:
        return f"Error calculating uptime: {e}"


def get_git_commit():
    try:
        # Run the git command to get the full commit hash (SHA-1)
        # git log -n 1 --format='%s -- %cd' --date=format-local:'%Y-%m-%d %H:%M:%S'
        result = subprocess.run(
            ['git', 'log', '-n 1', '--format=%s -- %cd', "--date=format-local:'%Y-%m-%d %H:%M:%S'"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        # Strip leading/trailing whitespace and return the hash
        return {'commit':result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return f"Error executing git command: {e.stderr}"
    except FileNotFoundError:
        return "Git executable not found. Make sure Git is installed and in the system's PATH."

def get_sysinfo(request):
    return JsonResponse(get_git_commit())
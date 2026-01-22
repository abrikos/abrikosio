from datetime import datetime, timedelta
import os

import psutil
from django.http.response import HttpResponse


def get_uptime(request):
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
        return HttpResponse(f"Django uptime {days} days, {hours:02}:{minutes:02}:{seconds:02}")

    except psutil.NoSuchProcess:
        return HttpResponse("Uptime not available (process not found)")
    except Exception as e:
        return HttpResponse(f"Error calculating uptime: {e}")
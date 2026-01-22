import datetime

import uptime
from django.http.response import HttpResponse


def get_uptime(request):
    boot_time = uptime.boottime()

    # Calculate the time difference
    now = datetime.datetime.now(boot_time.tzinfo)  # Use timezone-aware now if needed
    difference = now - boot_time

    # Format the output (e.g., in minutes, hours, days)
    days, hours, minutes = difference.days, difference.seconds // 3600, (difference.seconds // 60) % 60
    return HttpResponse(f"Server Uptime: {days} days, {hours} hours, {minutes} minutes")
import time
from datetime import datetime

# Path to hosts file
hosts_path = "/etc/hosts"  # Change this on Windows
redirect = "127.0.0.1"

# Websites to block
websites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

# Working hours (24-hour format)
start_hour = 9
end_hour = 17

while True:
    current_time = datetime.now()
    if start_hour <= current_time.hour < end_hour:
        print("Working hours... blocking websites.")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in websites:
                if site not in content:
                    file.write(f"{redirect} {site}\n")
    else:
        print("Outside working hours... unblocking websites.")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()

    time.sleep(300)  # Run every 5 minutes


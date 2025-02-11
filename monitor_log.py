import time

LOG_FILE = "application.log"  # This is the file we are monitoring

def monitor_log():
    """Continuously monitors the log file for errors."""
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to the end of the file

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new lines
                continue

            if "ERROR" in line or "CRITICAL" in line:
                print(f"🚨 ALERT: Issue found in log -> {line.strip()}")

if __name__ == "__main__":
    print("🔍 Starting log monitoring...")
    monitor_log() 

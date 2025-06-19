import os
import time
from datetime import datetime

def update_file_with_datetime():
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_name = "current_datetime.txt"
    
    with open(file_name, 'w') as f:
        f.write(f"Last updated: {current_datetime}")
    print(f"Updated {file_name} with current datetime: {current_datetime}")

def git_operations():
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    commands = [
	'cd /root/farming',
        'git add .',
        f'git commit -m "auto update {current_datetime}"',
        'git push --force'
    ]
    
    for cmd in commands:
        print(f"Executing: {cmd}")
        exit_code = os.system(cmd)
        if exit_code != 0:
            print(f"Command failed with exit code {exit_code}: {cmd}")
            return False
    return True

def setup_cron_job():
    # Get the path to the current script
    script_path = os.path.abspath(__file__)
    
    # Cron job entry (runs every 5 minutes)
    cron_entry = f"*/5 * * * * /usr/bin/python3 {script_path}"
    
    # Add to crontab
    os.system(f'(crontab -l 2>/dev/null; echo "{cron_entry}") | crontab -')
    print(f"Added cron job to run every 5 minutes: {cron_entry}")

def main():
    # Check if we should setup cron (run with --setup-cron argument)
    if len(os.sys.argv) > 1 and os.sys.argv[1] == "--setup-cron":
        setup_cron_job()
        return
    
    # Normal operation
    update_file_with_datetime()
    if git_operations():
        print(f"Operations completed at {datetime.now().strftime('%H:%M:%S')}")
    else:
        print("There was an error during Git operations")

if __name__ == "__main__":
    main()

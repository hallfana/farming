import os
import time
from datetime import datetime

# Configuration
REPO_DIR = "/root/farming"  # Change this to your repository path
FILE_NAME = "current_datetime.txt"

def update_file_with_datetime():
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_path = os.path.join(REPO_DIR, FILE_NAME)
    
    with open(file_path, 'w') as f:
        f.write(f"Last updated: {current_datetime}")
    print(f"Updated {file_path} with current datetime: {current_datetime}")

def git_operations():
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Verify we're in a git repository
    if not os.path.exists(os.path.join(REPO_DIR, ".git")):
        print(f"Error: {REPO_DIR} is not a Git repository")
        return False
    
    # Change to repository directory first
    os.chdir(REPO_DIR)
    
    commands = [
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
    script_path = os.path.abspath(__file__)
    cron_entry = f"*/5 * * * * /usr/bin/python3 {script_path}"
    os.system(f'(crontab -l 2>/dev/null; echo "{cron_entry}") | crontab -')
    print(f"Added cron job to run every 5 minutes: {cron_entry}")

def main():
    if len(os.sys.argv) > 1 and os.sys.argv[1] == "--setup-cron":
        setup_cron_job()
        return
    
    # Ensure repository directory exists
    if not os.path.exists(REPO_DIR):
        print(f"Error: Repository directory {REPO_DIR} does not exist")
        return
    
    update_file_with_datetime()
    if git_operations():
        print(f"Operations completed at {datetime.now().strftime('%H:%M:%S')}")
    else:
        print("There was an error during Git operations")

if __name__ == "__main__":
    main()

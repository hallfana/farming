import os
from datetime import datetime

def update_file_with_date():
    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # File name to create/modify
    file_name = "current_date.txt"
    
    # Write current date to file
    with open(file_name, 'w') as f:
        f.write(f"Last updated: {current_date}")
    
    print(f"Updated {file_name} with current date: {current_date}")

def git_operations():
    # Get current date for commit message
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Git commands to execute
    commands = [
        'git add .',
        f'git commit -m "auto update {current_date}"',
        'git push --force'
    ]
    
    # Execute each command
    for cmd in commands:
        print(f"Executing: {cmd}")
        exit_code = os.system(cmd)
        if exit_code != 0:
            print(f"Command failed with exit code {exit_code}: {cmd}")
            return False
    return True

def main():
    update_file_with_date()
    if git_operations():
        print("All operations completed successfully!")
    else:
        print("There was an error during Git operations")

if __name__ == "__main__":
    main()

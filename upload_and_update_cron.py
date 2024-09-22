import paramiko
from scp import SCPClient
from config import hostname, username, password
import datetime
import os

# Configuration variables
local_file_path = 'raspitimelapse.sh'
remote_file_path = f'/home/{username}/raspitimelapse.sh'
cron_job = f'*/15 6-20 * * * /home/{username}/raspitimelapse.sh 2>&1'

# Read and modify the raspitimelapse.sh file
with open(local_file_path, 'r') as file:
    content = file.read()

# Replace <username> with the actual username
content = content.replace('<username>', username)

# Save the modified content to a temporary file
temp_file_path = 'temp_raspitimelapse.sh'
with open(temp_file_path, 'w', newline='\n') as file:
    file.write(content)

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, username=username, password=password)

    # Install imagemagick without prompting for confirmation
    ssh.exec_command('sudo apt-get update')
    ssh.exec_command('sudo apt-get install -y imagemagick')
     
    # Create an SCP client
    with SCPClient(ssh.get_transport()) as scp:
        # Upload the modified file
        scp.put(temp_file_path, remote_file_path)
    
    print("File uploaded successfully.")
    
    # Make the script executable
    ssh.exec_command(f'chmod +x {remote_file_path}')
    print("File made executable.")

    # Update the crontab
    stdin, stdout, stderr = ssh.exec_command('crontab -l')
    current_crontab = stdout.read().decode()
    
    if cron_job not in current_crontab:
        new_crontab = current_crontab + '\n' + cron_job + '\n'
        stdin, stdout, stderr = ssh.exec_command('crontab -')
        stdin.write(new_crontab)
        stdin.flush()
        print("Crontab updated successfully.")
    else:
        print("Crontab already contains the job.")
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the SSH connection
    ssh.close()
    # Remove the temporary file
    os.remove(temp_file_path)
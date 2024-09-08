import paramiko
from scp import SCPClient
from config import hostname, username, password

# Configuration variables
local_file_path = 'raspitimelapse.sh'
remote_file_path = f'/home/{username}/raspitimelapse.sh'
cron_job = f'*/5 6-20 * * * /home/{username}/raspitimelapse.sh 2>&1'

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, username=username, password=password)
    
    # Create an SCP client
    with SCPClient(ssh.get_transport()) as scp:
        # Upload the file
        scp.put(local_file_path, remote_file_path)
    
    print("File uploaded successfully.")
    
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
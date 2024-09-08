import paramiko
from scp import SCPClient
import datetime
import os
from moviepy.editor import ImageSequenceClip
from config import remote_path, local_path, hostname, username, password

# Get today's date in the required format
today_date = datetime.datetime.now().strftime('%Y%m%d')

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, username=username, password=password)
    
    # List files in the remote directory
    stdin, stdout, stderr = ssh.exec_command(f'ls {remote_path}')
    files = stdout.read().decode().split()
    
    # Filter files based on today's date
    today_files = [f for f in files if today_date in f]
    
    # Define the list file name based on today's date
    list_file_name = f'{today_date}.txt'
    
    # Create an SCP client
    with SCPClient(ssh.get_transport()) as scp:
        # Copy the filtered files from the remote directory to the local directory
        for file in today_files:
            scp.get(remote_path + file, local_path)
    
    print("Files copied successfully.")
    
    # Create a timelapse video using moviepy
    image_files = [os.path.join(local_path, file) for file in today_files]
    clip = ImageSequenceClip(image_files, fps=3)
    clip.write_videofile(f"{local_path}{today_date}.mp4", codec="libx264")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the SSH connection
    ssh.close()
# Timelapse Script Repository

This repository contains scripts and configuration files to automate the process of capturing images from a Raspberry Pi camera, transferring them to a local machine, and creating a timelapse video.

## Repository Structure

- [`config.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fconfig.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\config.py"): Contains configuration variables such as remote and local paths, server hostname, username, and password.
- [`raspitimelapse.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fraspitimelapse.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\raspitimelapse.sh"): A shell script to capture images from the Raspberry Pi camera at regular intervals and annotate them with a timestamp.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\requirements.txt"): Lists the Python dependencies required for the scripts.
- [`scp_copy_today.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fscp_copy_today.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\scp_copy_today.py"): A Python script to copy today's images from the Raspberry Pi to the local machine and create a timelapse video.
- [`upload_and_update_cron.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fupload_and_update_cron.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\upload_and_update_cron.py"): A Python script to upload the [`raspitimelapse.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fraspitimelapse.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\raspitimelapse.sh") script to the Raspberry Pi and update the crontab to schedule the image capture.

## Setup

1. **Install Dependencies**:
   Ensure you have Python and pip installed. Then, install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure the Scripts**:
   Update the [`config.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fconfig.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\config.py") file with your specific paths and server details:
   ```py
   remote_path = '/home/anand/raspitimelapse/'
   local_path = 'c:\\users\\anand\\timelapse\\'
   hostname = 'pizero.local'
   username = 'anand'
   password = 'Just4Zero!'
   ```

## Usage

### 1. Upload and Schedule the Capture Script

Run the [`upload_and_update_cron.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fupload_and_update_cron.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\upload_and_update_cron.py") script to upload the [`raspitimelapse.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fraspitimelapse.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\raspitimelapse.sh") script to the Raspberry Pi and update the crontab:
```sh
python upload_and_update_cron.py
```
This script will:
- Upload [`raspitimelapse.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fraspitimelapse.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\raspitimelapse.sh") to the Raspberry Pi.
- Add a cron job to run the script every 5 minutes between 6 AM and 8 PM.

### 2. Capture Images

The [`raspitimelapse.sh`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fraspitimelapse.sh%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\raspitimelapse.sh") script will be executed by the cron job and will:
- Capture an image from the Raspberry Pi camera.
- Annotate the image with a timestamp.
- Save the image in the specified directory.

### 3. Copy Images and Create Timelapse

Run the [`scp_copy_today.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fanand%2Ftimelapsescript%2Fscp_copy_today.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\anand\timelapsescript\scp_copy_today.py") script to copy today's images from the Raspberry Pi to the local machine and create a timelapse video:
```sh
python scp_copy_today.py
```
This script will:
- Connect to the Raspberry Pi via SSH.
- Copy images from the remote directory to the local directory.
- Create a timelapse video using the copied images.

## Significant Commands

- **Install Dependencies**:
  ```sh
  pip install -r requirements.txt
  ```

- **Upload and Schedule the Capture Script**:
  ```sh
  python upload_and_update_cron.py
  ```

- **Copy Images and Create Timelapse**:
  ```sh
  python scp_copy_today.py
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [paramiko](https://www.paramiko.org/) for SSH connections.
- [scp](https://github.com/jbardin/scp.py) for SCP file transfers.
- [moviepy](https://zulko.github.io/moviepy/) for creating timelapse videos.

Feel free to contribute to this project by submitting issues or pull requests.
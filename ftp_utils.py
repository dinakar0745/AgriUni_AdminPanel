import ftplib
import os


def download_file_from_ftp(ftp_server, ftp_username, ftp_password, remote_file_path, local_dir):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_username, ftp_password)

        # Ensure local directory exists
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        # Extract the filename from the remote file path
        filename = os.path.basename(remote_file_path)
        local_file_path = os.path.join(local_dir, filename)

        # Check if file already exists
        if os.path.exists(local_file_path):
            print(f"File {filename} already exists locally.")
            ftp.quit()
            return local_file_path

        with open(local_file_path, 'wb') as local_file:
            # Download the file
            ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)
            print(f"Downloaded {filename} to {local_file_path}")

        ftp.quit()
        return local_file_path
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

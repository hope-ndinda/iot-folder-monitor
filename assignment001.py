import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


MONITOR_FOLDER = "camera_images"  # Folder to monitor
UPLOADED_FOLDER = "uploaded"      # Folder to store uploaded images
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/0/j/e/c/t/s/4e8d42b606F70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

os.makedirs(UPLOADED_FOLDER, exist_ok=True)

class UploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.jpg', '.jpeg', '.png')):
            time.sleep(30) 
            file_path = event.src_path
            print(f"Uploading {file_path}...")
            
            try:
                result = subprocess.run(
                    ["curl", "-X", "POST", "-F", f"imageFile=@{file_path}", UPLOAD_URL],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    print(f"Upload successful: {file_path}")
                    os.rename(file_path, os.path.join(UPLOADED_FOLDER, os.path.basename(file_path)))
                else:
                    print(f"Upload failed for {file_path}: {result.stderr}")
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")


event_handler = UploadHandler()
observer = Observer()
observer.schedule(event_handler, MONITOR_FOLDER, recursive=False)
observer.start()

print(f"Monitoring folder: {MONITOR_FOLDER}")
try:
    while True:
        time.sleep(1) 
except KeyboardInterrupt:
    observer.stop()

observer.join()

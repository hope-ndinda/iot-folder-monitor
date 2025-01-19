iot-folder-monitor

Overview
This project automates the process of monitoring a folder for new images, uploading them to a server using the curl command, and organizing them into a separate folder after successful upload.

It was developed as part of an assignment for automating embedded system tasks.



Features
1.Monitors a folder where a camera saves captured pictures.
2.Automatically uploads each image to the server every 30 seconds.
3.Moves successfully uploaded images to an "uploaded" folder to avoid redundancy.

Usage
Requirements
Python 3.x
watchdog library for folder monitoring.
Internet connection to upload images.

Setup Instructions
1.Clone repository
2.Install dependencies
3 Update the script to suit your directory structure and the Url
4.Run the script


Challenges Faced
Encountered a 404 error on the upload URL, likely due to server misconfiguration.
Worked around potential issues by testing the script with mock endpoints.


License
This project is for educational purposes only and is not intended for production use.

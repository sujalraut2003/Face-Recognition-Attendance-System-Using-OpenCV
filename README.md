# Face-Recognition-Attendance-System-Using-OpenCV
A Face Recognition-based Attendance System built using Flask, Python, OpenCV, and face_recognition. It captures faces through a webcam, logs attendance in a CSV file, and provides a web interface to view and filter attendance records by date.

Step-by-Step Guide: Setting Up and Running the Face Recognition Attendance System
1. Clone or Download the Project
If you haven't already, clone or download the project to your local machine:

Clone from GitHub (If available)
bash
Copy code
 download the ZIP file of the project from GitHub and extract it.

2. Install Python and Dependencies
Ensure you have Python 3.x installed on your system. You can check this by running the following command:

bash
Copy code
python --version
If Python is not installed, download and install it from Python’s official website.

Install Required Libraries
Navigate to your project directory using the terminal or command prompt:

bash
Copy code
cd your_project
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

For Windows:
bash
Copy code
.\venv\Scripts\activate
For macOS/Linux:
bash
Copy code
source venv/bin/activate
Next, install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file, manually install the libraries:

bash
Copy code
pip install flask opencv-python face_recognition numpy
3. Prepare the images Folder for Face Recognition
Create an images Folder:

In the root directory of your project, create a folder named images. This folder will store the images of individuals whose attendance will be recorded.

Add Images with Names:

Add the images of people you want to recognize. Each image should be named according to the person’s name (e.g., john_doe.jpg).

Example:

images/john_doe.jpg
images/jane_smith.jpg
images/alice_johnson.jpg
Make sure the image files are clear, and the faces are visible.

Ensure the Folder Structure Looks Like This:

bash
Copy code
your_project/
├── app.py                # Flask web application script
├── attendance.py         # Face recognition script
├── images/               # Folder containing images of individuals
│   ├── john_doe.jpg      # Image of John Doe
│   ├── jane_smith.jpg    # Image of Jane Smith
│   └── alice_johnson.jpg # Image of Alice Johnson
├── attendance.csv        # CSV file for recording attendance
├── requirements.txt      # File listing dependencies
└── templates/
    └── index.html        # HTML template for the web page
4. Understand the Code Structure
app.py: This is the Flask web server that displays the attendance page and allows you to filter attendance by date.
attendance.py: This is the face recognition script that detects faces using a webcam and records attendance in attendance.csv.
index.html: This is the HTML file for displaying the attendance records on the web page.
attendance.csv: This file stores the attendance data, including the name, time, and date.
5. Configure the Paths in the Code
Ensure that the images folder path is correct in both attendance.py and app.py. The code already assumes that images are located in a folder called images.
python
Copy code
# In attendance.py
path = 'images'  # Ensure this points to the correct location of the images folder
6. Run the Face Recognition Script
Now, let's start the face recognition system:

Run the attendance script (this will start the webcam feed and begin detecting faces):

bash
Copy code
python attendance.py
The script will capture faces through the webcam, match them with images in the images folder, and record the attendance (name, time, and date) in the attendance.csv file.

7. Run the Flask Web Application
Once the face recognition script is running and recording attendance data, start the Flask web application to display the attendance:

Run the Flask app:

bash
Copy code
python app.py
This will start a local web server on http://127.0.0.1:5000.

Access the Web Application:

Open your browser and go to http://127.0.0.1:5000. You should see the attendance records displayed.

8. Filter Attendance by Date
On the web page, you can filter the attendance records by selecting a date from the date input field and clicking the Filter button. This will update the displayed records to only show the attendance for the selected date.

9. Check the Attendance Data
The attendance will be stored in the attendance.csv file, which will contain the following columns:

Name
Time
Date
For example:

makefile
Copy code
Name,Time,Date
john_doe,10:15:30,13/11/24
jane_smith,10:17:45,13/11/24
alice_johnson,10:19:10,13/11/24
10. Stop the Process
To stop the processes:

Press CTRL + C in the terminal to stop the Flask server.
Close the webcam feed by pressing Enter when the webcam window is active.
Conclusion
You have now successfully set up and run a face recognition-based attendance system! Make sure to:

Add clear images of individuals with proper names.
Use a properly lit environment for face detection.
Check the attendance records in attendance.csv and on the Flask web app.

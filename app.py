from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)

# Function to read attendance data from CSV
def loadAttendance(selected_date=None):
    attendance_data = []
    try:
        with open('attendance.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header if it exists
            for row in reader:
                if len(row) >= 3:  # Ensure row has at least 3 elements to avoid index errors
                    if selected_date:
                        # Filter attendance by selected date
                        if row[2] == selected_date:
                            attendance_data.append({'name': row[0], 'time': row[1], 'date': row[2]})
                    else:
                        attendance_data.append({'name': row[0], 'time': row[1], 'date': row[2]})
                else:
                    print(f"Skipping malformed or empty row: {row}")
    except FileNotFoundError:
        print("attendance.csv not found. Creating a new one.")
        with open('attendance.csv', 'w') as f:
            f.write('Name,Time,Date\n')  # Write a header for the CSV

    return attendance_data

# Route for displaying attendance
@app.route('/')
def index():
    # Get the selected date from the query parameters (if any)
    selected_date = request.args.get('date')
    
    # Print the selected date for debugging
    print(f"Selected Date: {selected_date}")
    
    # Load attendance data (either filtered by selected date or all data)
    attendance_data = loadAttendance(selected_date)
    
    return render_template('index.html', attendance=attendance_data)

if __name__ == '__main__':
    app.run(debug=True)

# Destination Explorer — Travel Website Using AWS EC2

## Project Overview

Destination Explorer is a travel website developed to help users explore travel destinations, view travel packages, and make bookings through a web interface.

The project is deployed on an AWS EC2 Ubuntu instance. Apache serves the frontend, while a Flask backend handles booking requests and stores booking information in an SQLite database.

## Live Website

- **Website:** http://34.228.57.123/
- **Images Gallery:** http://34.228.57.123/ec2-images.html



## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask, Gunicorn
- **Database:** SQLite
- **Cloud Hosting:** AWS EC2 (Ubuntu)
- **Web Server:** Apache
- **Version Control:** Git and GitHub

## Project Structure

```text
Destination-explorer-website-using-AWS-EC2/
├── index.html
├── booking.html
├── hotel.html
├── package.html
├── script.js
├── style.css
├── media.css
├── Images
├── backend/
│   ├── app.py
│   └── requirements.txt
├── README.md
└── Destination explorer website integration with EC2 Instance.docx
```

*Note: The structure above describes the intended organization. Update it if your actual GitHub filenames or folder locations differ.*

## Frontend

The frontend provides the website interface and pages for exploring destinations, hotels, and packages, along with booking functionality.

Apache serves the website files from the EC2 instance.

## Backend

The backend is developed using Python and Flask. Gunicorn runs the Flask application, and the backend processes booking requests received from the frontend.

The booking endpoint is:

```text
POST /api/bookings
```

## Image Storage

The website images are stored as files on the EC2 Ubuntu server.

**Server directory:**

```text
/var/www/html/Images
```

The image files are served to website visitors by Apache. They are stored separately from the booking database.

## Database and Booking Storage

The project uses SQLite to store booking records.

**Database file:**

```text
/opt/destination-explorer/data/bookings.db
```

**Table:** `bookings`

The table stores booking information such as booking ID, booking type, origin, destination, travel date, package name, price, and creation timestamp, depending on the booking record.

The Flask backend processes booking submissions and saves the records to the database.

## Application Architecture

1. A user opens the website in a browser.
2. Apache serves the frontend pages and image files.
3. The user submits a booking through the website.
4. The frontend sends the booking request to the Flask backend.
5. Flask processes the request and stores the booking information in SQLite.
6. The saved booking records can be inspected in the database.

## Deployment on AWS EC2

The application is hosted on an AWS EC2 Ubuntu instance.

- Apache serves the frontend.
- Gunicorn runs the Flask backend.
- SQLite stores booking records locally on the EC2 instance.
- Website images are stored in the server's image directory.

## Running the Backend Locally

1. Install Python 3 and pip.
2. Open a terminal in the backend directory.
3. Create and activate a virtual environment.
4. Install the required packages.
5. Configure the database path and run the Flask application using the project's configuration.

Example commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Follow the configuration in `app.py` for the appropriate database setup and application startup.

## Documentation

The repository also includes the project implementation document, which contains supporting implementation screenshots and details.

## Author

Developed as an academic project demonstrating frontend development, backend integration, database storage, and cloud deployment using AWS EC2.


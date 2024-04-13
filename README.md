# Doctor Management System

## Overview
Doctor Management System is a full-stack web application designed to facilitate the management of doctors, appointments, and patient records in a medical facility. The system is built using Django for the backend, PostgreSQL as the database, React.js for the frontend with Material-UI components, and implements JWT authentication for secure access. Additionally, it includes a Progressive Web App (PWA) feature for offline access and patient email notifications for appointment reminders.

## Features
- **Doctor Management**: Add, edit, and remove doctor profiles, including their specialties and contact information.
- **Appointment Scheduling**: Schedule appointments for patients with available doctors and manage appointment times.
- **Patient Records**: Maintain detailed records of patients, including personal information, medical history, and visit summaries.
- **Search and Filter**: Easily search for doctors, patients, or appointments using filters and keywords.
- **JWT Authentication**: Secure login system for administrators and doctors to access the system.
- **Progressive Web App (PWA)**: Allows users to install the application on their devices and provides offline access.
- **Email Notifications**: Sends email notifications to patients for appointment reminders.

## Technologies Used
### Backend
- Django: Web framework for building the backend server.
- PostgreSQL: Relational database management system for storing data.
- Django REST Framework: Toolkit for building Web APIs.
- JWT (JSON Web Tokens): Authentication mechanism for secure access.

### Frontend
- React.js: JavaScript library for building user interfaces.
- Material-UI: React components library for implementing a Material Design UI.
- Progressive Web App (PWA): Enhances the web application to behave like a native app.
- Axios: Promise-based HTTP client for making API requests.

## Installation
1. **Backend Setup**:
   - Clone the repository:
     ```
     git clone https://github.com/yourusername/doctor-management-system.git
     cd doctor-management-system/backend
     ```
   - Install Python dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Set up PostgreSQL database and update the database settings in `settings.py`.
   - Run Django migrations:
     ```
     python manage.py migrate
     ```
   - Start the Django development server:
     ```
     python manage.py runserver
     ```

2. **Frontend Setup**:
   - Navigate to the frontend directory:
     ```
     cd ../frontend
     ```
   - Install Node.js dependencies:
     ```
     npm install
     ```
   - Start the React development server:
     ```
     npm start
     ```

## Usage
1. Access the application in your web browser.
2. Register as an administrator or doctor and log in using your credentials.
3. Use the dashboard to manage doctors,admin, appointments, and patient records.
4. Schedule appointments for patients and send email notifications for appointment reminders.
5. Explore the PWA features for offline access and installation on supported devices.

## Contributing
Contributions are welcome! Please follow the contribution guidelines in the CONTRIBUTING.md file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Special thanks to [Logesh V] for their contributions and support.

## Contact
For inquiries or support, please contact [kunaliyyapan25@gmail.com].

OUTPUT
i)user login 
![User login](https://github.com/Kunali25/Kunali25-Doctor-Management-Systems/assets/128252521/f773a4a5-695b-4bba-b486-18d823d2030d)
2)doctor login
![doctor login](https://github.com/Kunali25/Kunali25-Doctor-Management-Systems/assets/128252521/37a565e0-8d5c-4cc6-9f3d-c3bf86439104)
















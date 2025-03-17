# OTP-Verification-System
The OTP Verification System is a simple yet effective Python application designed to enhance security by implementing a OTP mechanism for user authentication. The application generates a unique, 6-digit OTP and sends it directly to the user's registered email address, ensuring secure and reliable verification.

# Features
* OTP Generation: Generates a secure 6-digit One-Time Password for each session.
* Email Sending: Utilizes SMTP protocols to send the generated OTP to the user’s email address.
* User Input Verification: Provides an interface for the user to input the received OTP for validation.
* Access Control: Grants access to the system upon successful OTP verification or denies access if the input does not match the generated OTP.

# Flow of the Application
1. User Request: The user initiates the OTP request process by entering their email address.
2. OTP Generation: The system generates a 6-digit OTP and stores it temporarily for validation.
3. Sending OTP: The system sends the generated OTP to the provided email address.
4. User Input: The user receives the email, retrieves the OTP, and enters it into the system.
5. Validation: The system compares the entered OTP against the generated OTP.
   *  Success: If it matches, access is granted, and the user is notified.
   *  Failure: If it does not match, access is denied, and the user is informed.

# Technologies Used
* Python: The primary programming language for implementing the OTP generation and validation logic.
* smtplib: A Python library to send emails using the SMTP protocol.
* Random: A Python library for generating random numbers for OTP.

# Getting Started
1. Clone the Repository.
2. Install Required Packages: Make sure Python is installed. You might need to install the smtplib. Generally, smtplib is included with Python’s standard library.
3. Configure Email Settings: Modify the email configuration settings to include your SMTP server details and credentials.
4. Run the Application: Execute the main Python script to start the OTP verification process.

# Customization
You can customize various aspects of the OTP Verification System by modifying the otp_verification.py file. Here are key settings you can adjust:
1. OTP Length: Change the otp_length value to specify the length of the OTP you want to generate (default is 6 digits).
2. Email Subject: Modify the email_subject to customize the subject line of the verification email sent to users.
3. Email Body: Update the email_body to change the content of the verification email, allowing you to personalize the message.
4. Expiration Time for OTP: Set the otp_expiration_time (in seconds) to determine how long the OTP remains valid for user verification.
5. Number of Resend Attempts: Adjust the max_resend_attempts to define how many times a user can request a new OTP if needed.

# Conclusion
The OTP Verification System is a secure and customizable solution to user authentication. By adjusting these settings, you can tailor the system to better suit your specific needs while ensuring a smooth user experience. Feel free to expand and customize as necessary!

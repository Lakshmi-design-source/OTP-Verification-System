import random                   # Import the random module for generating random numbers
import smtplib                  # Import the smtplib module for sending emails
import tkinter as tk           # Import tkinter for creating the GUI
from tkinter import messagebox   # Import messagebox for pop-up messages

# Class to handle OTP generation and verification
class OTPVerifier:
    def __init__(self, email):  # Initialize with user's email
        self.email = email       # Store the email
        self.generated_otp = self.generate_otp()  # Generate an OTP

    def generate_otp(self):      # Function to generate a six-digit OTP
        return str(random.randint(100000, 999999))

    def send_otp_email(self):    # Function to send the OTP via email
        smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
        smtp_port = 587              # Port for TLS
        sender_email = 'Sender's email address'   # replace with your email
        password = 'Sender's email password'    # replace with your password

        subject = 'OTP Verification'  # Email subject
        body = f'Your OTP is: {self.generated_otp}'  # Email body containing the OTP
        message = f'Subject: {subject}\n\n{body}'  # Compose the email message format

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()                     # Start TLS for security
            server.login(sender_email, password)  # Log in to the email account
            server.sendmail(sender_email, self.email, message)  # Send the email
            server.quit()                         # Close the connection
            return True                          # Return True on successful email sending
        except Exception as e:                  # Catch any exceptions that occur
            print(f'Error occurred while sending OTP: {e}')  # Print error message
            return False                         # Return False on failure

    def verify_otp(self, input_otp):          # Function to verify the entered OTP
        return input_otp == self.generated_otp  # Check if the input matches the generated OTP

# Class for the OTP Application GUI
class OTPApplication:
    def __init__(self, root):      # Initialize with the main window 
        self.root = root            # Store the root window
        self.root.title("OTP Verification System")  # Set window title
        self.root.geometry("500x400")  # Set window size

        # Create input fields and buttons in the GUI
        self.email_label = tk.Label(root, text="Enter your Email:")  # Label for email entry
        self.email_label.pack(pady=5)  # Add the label to the window

        self.email_entry = tk.Entry(root)  # Entry field for email
        self.email_entry.pack(pady=5)      # Add the entry field to the window

        self.send_button = tk.Button(root, text="Send OTP", command=self.send_otp)  # Button to send OTP
        self.send_button.pack(pady=10)     # Add the button to the window

        self.otp_label = tk.Label(root, text="Enter OTP:")  # Label for OTP entry
        self.otp_label.pack(pady=5)  # Add the label to the window

        self.otp_entry = tk.Entry(root)  # Entry field for the OTP
        self.otp_entry.pack(pady=5)      # Add the entry field to the window

        self.verify_button = tk.Button(root, text="Verify OTP", command=self.verify_otp)  # Button to verify OTP
        self.verify_button.pack(pady=10)     # Add the button to the window

        self.otp_verifier = None  # Initialize the OTPVerifier instance

    def send_otp(self):      # Function triggered when sending OTP
        email = self.email_entry.get()  # Get email from the entry field
        if not email:                    # Check if email is provided
            messagebox.showerror("Error", "Please enter an email address.")  # Show error message
            return

        self.otp_verifier = OTPVerifier(email)  # Create an OTPVerifier instance with the provided email
        if self.otp_verifier.send_otp_email():  # Send the OTP
            messagebox.showinfo("OTP Sent", "OTP has been sent to your email.")  # Show success message
        else:
            messagebox.showerror("Error", "Failed to send OTP. Check your email configurations.")  # Show error

    def verify_otp(self):    # Function triggered when verifying the OTP
        if self.otp_verifier is None:  # Check if the OTP has been sent
            messagebox.showerror("Error", "Please send an OTP first.")  # Show error message
            return

        input_otp = self.otp_entry.get()  # Get entered OTP
        if self.otp_verifier.verify_otp(input_otp):  # Verify the OTP
            messagebox.showinfo("Success", "Access Granted! OTP verified successfully!")  # Success message
        else:
            messagebox.showerror("Error", "Access Denied! Incorrect OTP. Please try again.")  # Failure message

def main():        # Main function to run the application
    root = tk.Tk()  # Create the main application window
    app = OTPApplication(root)  # Initialize the OTP Application
    root.mainloop()  # Start the GUI loop to wait for user interaction

if __name__ == "__main__":
    main()

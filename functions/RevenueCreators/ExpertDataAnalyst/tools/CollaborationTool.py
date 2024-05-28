from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class CollaborationTool(BaseTool):
    """
    Facilitates document sharing, report generation, and communication between the ExpertDataAnalyst agent and the SalesManagerCEO. This tool leverages document manipulation for report generation and email for real-time communication.
    """

    email_recipient: str = Field(
        ..., description="The email address of the recipient for communication.")
    document_content: str = Field(
        ..., description="The content of the document/report to be shared.")

    def run(self):
        # Setup email client
        sender_email = os.getenv("AGENCY_EMAIL")
        password = os.getenv("AGENCY_EMAIL_PASSWORD")

        # Create MIME message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = self.email_recipient
        message['Subject'] = "Collaboration Tool Report Sharing"

        # Attach the document content
        message.attach(MIMEText(self.document_content, 'plain'))

        # Sending the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, self.email_recipient, message.as_string())

        # Return a confirmation message
        return f"Email successfully sent to {self.email_recipient} with the report."

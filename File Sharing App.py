# FILE SHARING APPLICATION USING PYTHON
import http.server
import socketserver
import pyqrcode
import os
import socket
import time
import subprocess

PORT = 8000
USERNAME = os.getenv('USERNAME')
SHARE_DIR = f"C:\\Users\\{USERNAME}\\Desktop\\Python_Notes" # you can use any file to share at the place of "Python_Notes"
# i shared python notes u can use any file or folder which exist on desktop
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address: {ip_address}")
        return ip_address
    except Exception as e:
        print(f"Error obtaining IP address: {e}")
        return "127.0.0.1" 

ip_address = get_ip_address()
url = f"http://{ip_address}:{PORT}/"
print(f"Generated URL: {url}")

qr_code_path = os.path.join(os.getcwd(), "qr_code.png")

try:
    qr_code = pyqrcode.create(url) # it open the QR code image file 
    qr_code.png(qr_code_path, scale=8) # it save the QR code as a PNG file
    print(f"QR code for URL '{url}' generated and saved as '{qr_code_path}'.")
except Exception as e:
    print(f"Error generating QR code: {e}")

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        if self.path == '/':
            self.path = '/'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def display_qr_code():
    time.sleep(1)  
    if not os.path.exists(qr_code_path):
        print(f"QR code file not found: {qr_code_path}")
        return
    
    try:
         # it open the QR code image file 
        if os.name == 'nt':  # it is for Windows
            os.startfile(qr_code_path)
        elif os.name == 'posix':  # it is for Linux, macOS
            subprocess.call(["xdg-open", qr_code_path])
        print("QR code displayed successfully.")
    except Exception as e:
        print(f"Error opening QR code: {e}")

def start_server():
    try:
        if not os.path.exists(SHARE_DIR):
            raise FileNotFoundError(f"Directory not found: {SHARE_DIR}")

        os.chdir(SHARE_DIR)
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"Serving files at: {url}")
            print("Press Ctrl+C to stop the server.")
            display_qr_code() # it displays the QR code
            httpd.serve_forever() # it starts the server
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_server()

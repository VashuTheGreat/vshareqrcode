# import http.server # for serving files over HTTP
# import socketserver # for serving files over HTTP
# import socket # for getting system ip address
# import qrcode # for serving QR codes
# import os # for selecting file path and dir
# from tkinter import Tk, filedialog # file picker dialog




# class sendFile():
#     file_path = ""
#     def __init__(self,file_path):
#         self.file_path = file_path
    
    
#     def send(self): 
#         file_path = self.file_path   
        
#         # # Step 1: File picker dialog
#         # root = Tk()
#         # root.withdraw()  # Hide root window
#         # file_path = filedialog.askopenfilename(title="Select a file to share")

#         if not file_path:
#             print("❌ No file selected. Exiting.")
#             exit()

#         file_name = os.path.basename(file_path)
#         file_dir = os.path.dirname(file_path)

#         # Step 2: Get local IP
#         hostname = socket.gethostname()
#         local_ip = socket.gethostbyname(hostname)

#         # Step 3: Setup server
#         PORT = 8000
#         url = f"http://{local_ip}:{PORT}/{file_name}"
#         print(f"📡 Sharing file at: {url}")

#         # Step 4: Generate QR code
#         qr = qrcode.QRCode()
#         qr.add_data(url)
#         qr.make()
#         qr.print_ascii(invert=True)  # Terminal QR

#         # Step 5: Serve file via HTTP
#         class FileRequestHandler(http.server.SimpleHTTPRequestHandler):
#             def __init__(self, *args, **kwargs):
#                 super().__init__(*args, directory=file_dir, **kwargs)

#         with socketserver.TCPServer(("", PORT), FileRequestHandler) as httpd:
#             print("🚀 Scan QR code above to download the file.")
#             print("🔁 Press Ctrl+C to stop the server.")
#             try:
#                 httpd.serve_forever()
#             except KeyboardInterrupt:
#                 print("\n🛑 Server stopped.")
#                 httpd.shutdown()




# if __name__ == "__main__":
#     sendFile(r"C:\Users\Asus\Downloads\racing.png").send()
    
    
    
    
import vshareqrcode

if __name__ == "__main__":
    # File path dena, jise share karna hai
    sender = vshareqrcode.sendFile(r"C:\Users\Asus\Downloads\racing.png")
    sender.send()


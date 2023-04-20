import socket
import tkinter as tk

class PortScanner:
    def __init__(self, master):
        self.master = master
        self.master.title("Port Scanner")

        
        self.host_label = tk.Label(self.master, text="Enter Host:")
        self.host_entry = tk.Entry(self.master, width=30)
        self.port_label = tk.Label(self.master, text="Enter Port:")
        self.port_entry = tk.Entry(self.master, width=30)
        self.result_label = tk.Label(self.master, text="")
        self.scan_button = tk.Button(self.master, text="Scan", command=self.scan_ports)

        
        self.host_label.pack()
        self.host_entry.pack()
        self.port_label.pack()
        self.port_entry.pack()
        self.scan_button.pack()
        self.result_label.pack()

    def scan_ports(self):
        
        host = self.host_entry.get()
        port = int(self.port_entry.get())

        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()

        
        if result == 0:
            self.result_label.config(text=f"Port {port} is open")
        else:
            self.result_label.config(text=f"Port {port} is closed")


root = tk.Tk()
app = PortScanner(root)
root.mainloop()

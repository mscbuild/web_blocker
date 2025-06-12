import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime

# Path to your hosts file
hosts_path = "/etc/hosts"  # Use "C:\\Windows\\System32\\drivers\\etc\\hosts" for Windows
redirect = "127.0.0.1"

# Working hours (optional)
start_hour = 9
end_hour = 17

# Shared state
websites = []
running = False

# Blocking function
def block_websites():
    global running
    while running:
        now = datetime.now()
        if start_hour <= now.hour < end_hour:
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for site in websites:
                    if site not in content:
                        file.write(f"{redirect} {site}\n")
        else:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in websites):
                        file.write(line)
                file.truncate()
        time.sleep(10)

# GUI functions
def add_website():
    site = entry.get().strip()
    if site and site not in websites:
        websites.append(site)
        listbox.insert(tk.END, site)
        entry.delete(0, tk.END)

def remove_selected():
    selected = listbox.curselection()
    for index in reversed(selected):
        site = listbox.get(index)
        websites.remove(site)
        listbox.delete(index)

def start_blocking():
    global running
    if not websites:
        messagebox.showwarning("No Websites", "Please add websites to block.")
        return
    if not running:
        running = True
        thread = threading.Thread(target=block_websites, daemon=True)
        thread.start()
        messagebox.showinfo("Started", "Website blocking started.")

def stop_blocking():
    global running
    running = False
    messagebox.showinfo("Stopped", "Website blocking stopped.")

# GUI setup
root = tk.Tk()
root.title("Website Blocker")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Add Website", command=add_website).pack(pady=2)
tk.Button(root, text="Remove Selected", command=remove_selected).pack(pady=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

tk.Button(root, text="Start Blocking", command=start_blocking).pack(pady=5)
tk.Button(root, text="Stop Blocking", command=stop_blocking).pack(pady=5)

root.mainloop()


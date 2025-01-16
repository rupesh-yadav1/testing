import tkinter as tk
from tkinter import messagebox
import speedtest

# Function to check internet speed (download and upload)
def check_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        # Get download and upload speeds in Mbps
        download_speed = st.download() / 10**6  # Convert from bits to Mbps
        upload_speed = st.upload() / 10**6  # Convert from bits to Mbps
        
        # Update labels with the speeds
        download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve speed. Error: {str(e)}")
        download_label.config(text="Download Speed: -- Mbps")
        upload_label.config(text="Upload Speed: -- Mbps")

# Create the main window
root = tk.Tk()
root.title("Internet Speed Checker")
root.geometry("400x300")

# Create a label for instructions
instructions_label = tk.Label(root, text="Click 'Check Speed' to measure your internet speed", font=("Arial", 12))
instructions_label.pack(pady=10)

# Create a button to check speed
check_button = tk.Button(root, text="Check Speed", command=check_speed, font=("Arial", 14))
check_button.pack(pady=20)

# Create labels to display download and upload speeds
download_label = tk.Label(root, text="Download Speed: -- Mbps", font=("Arial", 12))
download_label.pack()

upload_label = tk.Label(root, text="Upload Speed: -- Mbps", font=("Arial", 12))
upload_label.pack()

# Run the GUI loop
root.mainloop()

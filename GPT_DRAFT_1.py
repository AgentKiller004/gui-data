import tkinter as tk
from PIL import Image, ImageTk
import os

def create_homepage():
    # Create the main window
    root = tk.Tk()
    root.title("Fantasy League")
    root.geometry("1920x1080")  # Full HD window size
    root.configure(bg="#1c1c1c")  # Dark theme background
    root.resizable(True, True)  # Allow resizing the window

    # Heading frame
    header_frame = tk.Frame(root, bg="#1c1c1c")
    header_frame.pack(pady=20)

    # Football logo
    logo_path = "football_logo.jpg"
    if os.path.exists(logo_path):
        football_image = Image.open(logo_path)
        football_image = football_image.resize((80, 80), Image.Resampling.LANCZOS)  # Larger size for 1080p
        football_photo = ImageTk.PhotoImage(football_image)
        football_label = tk.Label(header_frame, image=football_photo, bg="#1c1c1c")
        football_label.image = football_photo  # Keep a reference to avoid garbage collection
        football_label.pack(side=tk.LEFT, padx=10)
    else:
        # Display a placeholder or handle the error if image is not found
        print(f"Error: {logo_path} not found.")
        placeholder_label = tk.Label(header_frame, text="Football Logo Not Found", font=("Arial", 14), fg="red", bg="#1c1c1c")
        placeholder_label.pack(side=tk.LEFT, padx=10)

    # Heading
    heading_label = tk.Label(
        header_frame,
        text="Fantasy League",
        font=("Arial", 36, "bold"),  # Larger font for a bigger window
        fg="#ffffff",
        bg="#1c1c1c",
    )
    heading_label.pack(side=tk.LEFT)

    # Run the application
    root.mainloop()

create_homepage()

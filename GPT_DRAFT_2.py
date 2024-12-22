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
    root.title("Fantasy Football League")  # Change title here
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
        # Display a placeholder if the image is not found
        print(f"Error: {logo_path} not found.")
        placeholder_label = tk.Label(header_frame, text="Football Logo Not Found", font=("Arial", 14), fg="red", bg="#1c1c1c")
        placeholder_label.pack(side=tk.LEFT, padx=10)

    # Heading label
    heading_label = tk.Label(
        header_frame,
        text="Fantasy League",
        font=("Arial", 36, "bold"),  # Larger font for a bigger window
        fg="#ffffff",
        bg="#1c1c1c",
    )
    heading_label.pack(side=tk.LEFT)

    # Button frame for the leagues
    button_frame = tk.Frame(root, bg="#1c1c1c")
    button_frame.pack(pady=50)

    # List of league names
    leagues = ["League 1", "League 2", "League 3", "League 4", "League 5"]

    # Create buttons for each league
    for league in leagues:
        button = tk.Button(
            button_frame,
            text=league,
            font=("Arial", 18),
            fg="#ffffff",
            bg="#FF5F00",  # Green button color
            activebackground="#45a049",  # Darker green when active
            relief="raised",  # Raised effect
            bd=4,
            width=20,  # Button width
            height=2  # Button height
        )
        button.pack(pady=10)

    # Run the application
    root.mainloop()

create_homepage()

import tkinter as tk
from PIL import Image, ImageTk
import os

# Function to open a new screen based on the league clicked
def open_new_screen(league_name):
    # Create a new top-level window (a new screen)
    new_window = tk.Toplevel()
    new_window.title(f"{league_name} Screen")  # Title for the new window
    new_window.geometry("1920x1080")  # Full HD window size
    
    # Customize the background color and content based on the league
    if league_name == "League 1":
        new_window.configure(bg="blue")
    elif league_name == "League 2":
        new_window.configure(bg="green")
    elif league_name == "League 3":
        new_window.configure(bg="red")
    elif league_name == "League 4":
        new_window.configure(bg="purple")
    elif league_name == "League 5":
        new_window.configure(bg="orange")
    
    # Add a label in the new window (optional)
    label = tk.Label(new_window, text=f"Welcome to {league_name}", font=("Arial", 36, "bold"), fg="#ffffff", bg=new_window.cget("bg"))
    label.pack(pady=20)

# Function to simulate hover effect (optional)
def on_enter(event):
    event.widget.config(bg="#FF7F32")  # Lighter neon orange on hover

def on_leave(event):
    event.widget.config(bg="#FF5F00")  # Neon orange when not hovered

def create_homepage():
    # Create the main window
    root = tk.Tk()
    root.title("Fantasy Football League")  # Change title here
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
            bg="#FF5F00",  # Neon orange button color
            activebackground="#FF7F32",  # Lighter neon orange when active
            relief="raised",  # Raised effect
            bd=4,
            width=20,  # Button width
            height=2,  # Button height
            command=lambda league=league: open_new_screen(league)  # Pass the league name to the function
        )
        
        # Bind hover effects to the button (simulate neon glow)
        button.bind("<Enter>", on_enter)  # On hover
        button.bind("<Leave>", on_leave)  # When not hovered
        
        button.pack(pady=10)

    # Run the application
    root.mainloop()

create_homepage()

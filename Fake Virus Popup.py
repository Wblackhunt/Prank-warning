while True:
    import tkinter as tk
    from tkinter import messagebox
        # Function to show the warning popup
    def show_warning():
        # Create the main application window (root)
        root = tk.Tk()
        # Hide the main application window
        root.withdraw()
            
        # Show the warning message box with a title and message
        messagebox.showwarning("Warning", "Your PC is infected with a virus!")
            
        # Destroy the main application window after the message box is closed
        root.destroy()
    
    # Call the function to show the warning popup
    show_warning()


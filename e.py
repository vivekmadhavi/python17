import tkinter as tk

def on_entry_change(event):
    # Get the content of the entry widget
    user_input = entry.get()

    # Update the content of the second entry widget
    display_entry.delete(0, tk.END)
    display_entry.insert(0, user_input)

# Create the main window
root = tk.Tk()
root.title("Number Display")

# Create and place the entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<KeyRelease>", on_entry_change)

# Create and place the entry widget to display the entered number
display_entry = tk.Entry(root)
display_entry.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

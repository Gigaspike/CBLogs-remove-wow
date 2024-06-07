import os
import tkinter as tk
from tkinter import messagebox

def delete_files_with_patterns(folder_path, patterns):
    """
    Delete files in the specified folder that match any of the given patterns.
    
    :param folder_path: The path of the folder to check.
    :param patterns: A list of patterns or substrings to match filenames against.
    """
    # List all files in the specified folder
    files = os.listdir(folder_path)
    
    # Find files that match the patterns
    files_to_delete = [file_name for file_name in files if any(pattern in file_name for pattern in patterns)]

    if not files_to_delete:
        print("No files found matching the given patterns.")
        return

    # Create a simple Tkinter GUI to ask for confirmation
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_list = "\n".join(files_to_delete)
    message = f"Are you sure you want to delete the following files?\n\n{file_list}"

    if messagebox.askokcancel("Confirm Delete", message):
        for file_name in files_to_delete:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    else:
        print("File deletion canceled.")

# Example usage:
folder_to_check = 'K:\World of Warcraft\_retail_\Logs'  # Replace with the path to your folder
patterns_to_delete = ['WoWCombatLog', 'CombatLog', 'WoWCombatLog-053024_131130']  # Replace with your patterns or substrings

delete_files_with_patterns(folder_to_check, patterns_to_delete)


#I created this script with ai assistance in learning the python code requirement to simplify a solution to removing combatlogs from my wow folder to cut down on clutter.
# gigaspike
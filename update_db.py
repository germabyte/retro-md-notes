#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox as mb
import os
import json

NOTES_FOLDER = 'notes'      # Path to your notes folder
DB_FILENAME = 'db.json'     # Output file

def build_db():
    """
    Scans NOTES_FOLDER for .md files, reads their full text content,
    and writes a JSON array to DB_FILENAME.
    """
    data = []
    
    # List all files in "notes" folder
    for filename in os.listdir(NOTES_FOLDER):
        # Only process .md files
        if filename.lower().endswith('.md'):
            filepath = os.path.join(NOTES_FOLDER, filename)
            
            # Read the entire file (full text)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add an entry for each note
            data.append({
                "filename": filename,
                "content": content
            })
    
    # Write JSON
    with open(DB_FILENAME, 'w', encoding='utf-8') as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
    
    return len(data)  # number of notes processed

def on_update_db():
    """
    Called when the user clicks the "Build/Update DB" button.
    """
    try:
        count = build_db()
        mb.showinfo("Success", f"Successfully updated {DB_FILENAME} with {count} notes!")
    except Exception as e:
        mb.showerror("Error", f"Error building DB:\n{e}")

def main():
    """
    Sets up the Tkinter window and runs the app loop.
    """
    root = tk.Tk()
    root.title("DB Updater")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label_title = tk.Label(frame, text="Update DB Script", font=('Helvetica', 14, 'bold'))
    label_title.pack(pady=(0, 10))

    label_notes_folder = tk.Label(frame, text=f"Notes Folder: {NOTES_FOLDER}", font=('Helvetica', 10))
    label_notes_folder.pack()

    label_db_file = tk.Label(frame, text=f"DB Output File: {DB_FILENAME}", font=('Helvetica', 10))
    label_db_file.pack()

    btn_update = tk.Button(frame, text="Build/Update DB", command=on_update_db)
    btn_update.pack(pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    main()

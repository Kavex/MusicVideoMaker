import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def select_file(filetypes, title):
    return filedialog.askopenfilename(filetypes=filetypes, title=title)

def create_video():
    image_path = select_file([("Image Files", "*.jpg;*.jpeg;*.png")], "Select an Image")
    if not image_path:
        return
    
    audio_path = select_file([("Audio Files", "*.mp3;*.wav")], "Select an Audio File (MP3/WAV)")
    if not audio_path:
        return
    
    output_folder = os.path.dirname(audio_path)
    output_name = os.path.splitext(os.path.basename(audio_path))[0] + ".mp4"
    output_path = os.path.join(output_folder, output_name)
    
    command = [
        "ffmpeg", "-loop", "1", "-i", image_path, "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k", 
        "-shortest", "-movflags", "+faststart", output_path
    ]
    
    console_output.insert(tk.END, "Starting conversion...\n")
    console_output.update_idletasks()
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            console_output.insert(tk.END, line)
            console_output.see(tk.END)
            console_output.update_idletasks()
        process.wait()
        
        if process.returncode == 0:
            messagebox.showinfo("Success", f"MP4 created successfully: {output_path}")
        else:
            messagebox.showerror("Error", "Failed to create MP4. Ensure FFmpeg is installed and working.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
root = tk.Tk()
root.title("Music Video Maker")
root.geometry("500x300")

tk.Label(root, text="Convert an image and audio file (MP3/WAV) into an MP4 video.").pack(pady=5)
tk.Label(root, text="Supported file types: JPG, PNG, MP3, WAV").pack(pady=5)
convert_button = tk.Button(root, text="Select Files & Convert", command=create_video)
convert_button.pack(pady=10)

console_output = scrolledtext.ScrolledText(root, height=10, width=60, state=tk.NORMAL)
console_output.pack(pady=10)

root.mainloop()

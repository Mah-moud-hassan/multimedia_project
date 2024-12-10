import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(resolution):
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please paste a YouTube link.")
        return

    try:
        yt = YouTube(link)

        if resolution == "high":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        elif resolution == "low":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
        elif resolution == "audio":
            stream = yt.streams.filter(only_audio=True).first()

        save_path = "./"  # Downloads will be saved in the current directory
        stream.download(output_path=save_path)

        messagebox.showinfo("Success", f"Download completed! Saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("YouTube Downloader By LearnCodeEasily")
root.geometry("400x200")

# Add widgets
title_label = tk.Label(root, text="Youtube Downloader", font=("Arial", 16))
title_label.pack(pady=10)

url_label = tk.Label(root, text="Paste Link Here:", font=("Arial", 12))
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Buttons for different download options
high_res_button = tk.Button(root, text="High Resolution", bg="blue", fg="white", font=("Arial", 12), command=lambda: download_video("high"))
high_res_button.pack(pady=5)

low_res_button = tk.Button(root, text="Low Resolution", bg="red", fg="white", font=("Arial", 12), command=lambda: download_video("low"))
low_res_button.pack(pady=5)

audio_button = tk.Button(root, text="Audio Only", bg="yellow", font=("Arial", 12), command=lambda: download_video("audio"))
audio_button.pack(pady=5)

# Run the application
root.mainloop()

import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("720x360")
        self.root.configure(bg="#6A50A7")

        mixer.init() #pygame mixer initialization

        self.playlist = []
        self.current_index = 0

        #creat Ui
        self.create_widgets()

    def create_widgets(self):
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg="#8067B7")
        buttons_frame.pack(pady=10)

        play_button = tk.Button(buttons_frame, text="Play", bg="#2C2C2C", fg="#FFFFFF", command=self.play_music)
        play_button.grid(row=0, column=0, padx=5)

        pause_button = tk.Button(buttons_frame, text="Pause", bg="#2C2C2C", fg="#FFFFFF", command=self.pause_music)
        pause_button.grid(row=0, column=1, padx=5)

        stop_button = tk.Button(buttons_frame, text="Stop", bg="#2C2C2C", fg="#FFFFFF", command=self.stop_music)
        stop_button.grid(row=0, column=2, padx=5)

        next_button = tk.Button(buttons_frame, text="Next", bg="#2C2C2C", fg="#FFFFFF", command=self.next_track)
        next_button.grid(row=0, column=3, padx=5)

        # Album image
        album_image = tk.PhotoImage(file="imagess.png")  # use only gif and png image
        album_image_label = tk.Label(self.root, image=album_image, bg="#8067B7",width=300)
        album_image_label.image = album_image
        album_image_label.pack(side=tk.LEFT,fill=tk.BOTH,padx=10,pady=10)

        # Playlist frame
        playlist_frame = tk.Frame(self.root, bg="#252525")
        playlist_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        playlist_label = tk.Label(playlist_frame, text="Playlist", bg="#252525", fg="#D4D4D4")
        playlist_label.pack()

        self.playlistbox = tk.Listbox(playlist_frame, bg="#252525", fg="#D4D4D4", selectbackground="#1E1E1E", selectforeground="#FFFFFF", activestyle="none")
        self.playlistbox.pack(fill=tk.BOTH, expand=True)

        # Track title
        self.title_label = tk.Label(self.root, text="Now Playing: ", bg="#8067B7", fg="#D4D4D4")
        self.title_label.pack(pady=5)

        # Add folder button
        add_folder_button = tk.Button(self.root, text="Add Folder", bg="#2C2C2C", fg="#FFFFFF", command=self.add_folder)
        add_folder_button.pack(pady=10)

    def play_music(self):
        if self.playlist:
            mixer.music.load(self.playlist[self.current_index]) #load the music
            mixer.music.play()
            self.update_title()

    def pause_music(self):
        mixer.music.pause()

    def stop_music(self):
        mixer.music.stop()
        self.title_label.config(text="Now Playing: ")

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()

    def add_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist.extend([os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav'))])
            self.update_playlist()

    def update_playlist(self):
        self.playlistbox.delete(0, tk.END)
        for song in self.playlist:
            self.playlistbox.insert(tk.END, os.path.basename(song))

    def update_title(self):
        current_track = os.path.basename(self.playlist[self.current_index])
        self.title_label.config(text=f"Now Playing: {current_track}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerUI(root)
    root.mainloop()

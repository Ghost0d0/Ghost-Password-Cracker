from customtkinter import *
from tkinter import filedialog, messagebox
import threading
import os
from cracker import crack_password, detect_hash_type

class PasswordCrackerApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("GhostCracker - Password Cracker")
        self.geometry("650x500")
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Hash input section
        self.hash_label = CTkLabel(self.main_frame, text="Target Hash:", font=("Arial", 12, "bold"))
        self.hash_label.pack(pady=(10, 5))
        
        self.hash_entry = CTkEntry(self.main_frame, width=450, placeholder_text="Enter your hash here...")
        self.hash_entry.pack()
        self.hash_entry.bind("<KeyRelease>", self.update_hash_detection)

        self.detected_hash_type = CTkLabel(self.main_frame, text="Detected Hash Type: Unknown", font=("Arial", 11))
        self.detected_hash_type.pack(pady=5)

        # Wordlist section
        self.wordlist_label = CTkLabel(self.main_frame, text="Wordlist File:", font=("Arial", 12, "bold"))
        self.wordlist_label.pack(pady=(15, 5))
        
        self.wordlist_frame = CTkFrame(self.main_frame, fg_color="transparent")
        self.wordlist_frame.pack()
        
        self.wordlist_path = CTkEntry(self.wordlist_frame, width=350)
        self.wordlist_path.pack(side="left", padx=(0, 10))
        
        self.browse_button = CTkButton(self.wordlist_frame, text="Browse", command=self.browse_wordlist, width=90)
        self.browse_button.pack(side="left")

        # Progress bar with better visibility
        self.progress = CTkProgressBar(self.main_frame, width=450, mode='determinate')
        self.progress.set(0)
        self.progress.pack(pady=(20, 10))

        # Start button
        self.start_button = CTkButton(self.main_frame, text="Start Cracking", command=self.start_cracking, font=("Arial", 12, "bold"))
        self.start_button.pack(pady=10)

        # Results box
        self.result_box = CTkTextbox(self.main_frame, height=150, width=500, font=("Consolas", 11))
        self.result_box.pack(pady=10)
        self.result_box.insert("1.0", "Results will appear here...\n")

    def update_hash_detection(self, event=None):
        current_hash = self.hash_entry.get().strip()
        if current_hash:
            hash_type = detect_hash_type(current_hash)
            self.detected_hash_type.configure(text=f"Detected Hash Type: {hash_type}")

    def browse_wordlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.wordlist_path.delete(0, END)
            self.wordlist_path.insert(0, file_path)

    def update_progress(self, value):
        self.progress.set(value / 100)
        self.update()  # Force immediate GUI update

    def start_cracking(self):
        target_hash = self.hash_entry.get().strip()
        wordlist = self.wordlist_path.get().strip()

        if not target_hash:
            messagebox.showerror("Error", "Please provide the target hash.")
            return

        hash_type = detect_hash_type(target_hash)
        if hash_type == 'Unknown':
            messagebox.showerror("Error", "Could not detect hash type. Please provide a valid MD5, SHA1, SHA256, etc. hash.")
            return

        if not wordlist or not os.path.isfile(wordlist):
            messagebox.showerror("Error", "Please select a valid wordlist file.")
            return

        self.result_box.delete("1.0", END)
        self.result_box.insert("1.0", f"Starting cracking attempt for {hash_type} hash...\n")
        self.progress.set(0)
        self.start_button.configure(state="disabled")

        threading.Thread(
            target=self.run_cracker,
            args=(target_hash, hash_type, wordlist),
            daemon=True
        ).start()

    def run_cracker(self, target_hash, hash_type, wordlist):
        result = crack_password(target_hash, hash_type, wordlist, self.update_progress)
        
        self.after(0, lambda: self.start_button.configure(state="normal"))
        
        if 'error' in result:
            self.after(0, lambda: self.result_box.insert(END, f"\nError: {result['error']}\n"))
        elif result['found']:
            self.after(0, lambda: self.result_box.insert(END, "\n=== PASSWORD FOUND ===\n"))
            self.after(0, lambda: self.result_box.insert(END, f"Password: {result['password']}\n"))
            self.after(0, lambda: self.result_box.insert(END, f"Hash Type: {result['hash_type']}\n"))
            self.after(0, lambda: self.result_box.insert(END, f"Time Taken: {result['time']} seconds\n"))
        else:
            self.after(0, lambda: self.result_box.insert(END, "\n=== CRACKING FAILED ===\n"))
            self.after(0, lambda: self.result_box.insert(END, "Password not found in the wordlist.\n"))
            self.after(0, lambda: self.result_box.insert(END, f"Time Taken: {result['time']} seconds\n"))
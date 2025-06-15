import tkinter as tk
from tkinter import messagebox
import pyshorteners
import pyperclip
import webbrowser

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("600x400")
        self.root.configure(bg="#1e1e2e")
        
        # Initialize URL shortener
        self.shortener = pyshorteners.Shortener()
        
        # Create GUI elements
        self.create_banner()
        self.create_widgets()
        
    def create_banner(self):
        # Stylish banner
        banner_frame = tk.Frame(self.root, bg="#0a0a23", pady=10)
        banner_frame.pack(fill="x")
        
        banner_label = tk.Label(
            banner_frame,
            text="URL Shortener\nCoded by Pakistani Ethical Hacker Mr Sabaz Ali Khan",
            font=("Arial", 16, "bold"),
            fg="#00ff88",
            bg="#0a0a23",
            pady=10
        )
        banner_label.pack()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#1e1e2e", pady=20)
        main_frame.pack(expand=True)
        
        # URL input
        tk.Label(
            main_frame,
            text="Enter URL:",
            font=("Arial", 12),
            fg="#ffffff",
            bg="#1e1e2e"
        ).pack(pady=5)
        
        self.url_entry = tk.Entry(
            main_frame,
            width=50,
            font=("Arial", 10),
            bg="#2e2e3e",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.url_entry.pack(pady=5)
        
        # Shorten button
        tk.Button(
            main_frame,
            text="Shorten URL",
            command=self.shorten_url,
            font=("Arial", 12, "bold"),
            bg="#00ff88",
            fg="#0a0a23",
            activebackground="#00cc70",
            relief="flat",
            padx=20,
            pady=5
        ).pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(
            main_frame,
            text="Shortened URL will appear here",
            font=("Arial", 10),
            fg="#cccccc",
            bg="#1e1e2e",
            wraplength=500
        )
        self.result_label.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg="#1e1e2e")
        button_frame.pack(pady=10)
        
        # Copy button
        tk.Button(
            button_frame,
            text="Copy URL",
            command=self.copy_url,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="#ffffff",
            relief="flat",
            padx=10
        ).pack(side="left", padx=5)
        
        # Open button
        tk.Button(
            button_frame,
            text="Open URL",
            command=self.open_url,
            font=("Arial", 10),
            bg="#2196F3",
            fg="#ffffff",
            relief="flat",
            padx=10
        ).pack(side="left", padx=5)
        
    def shorten_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
            
        try:
            short_url = self.shortener.tinyurl.short(url)
            self.result_label.config(text=f"Shortened URL: {short_url}")
            self.short_url = short_url
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")
            
    def copy_url(self):
        try:
            pyperclip.copy(self.short_url)
            messagebox.showinfo("Success", "URL copied to clipboard!")
        except AttributeError:
            messagebox.showerror("Error", "No URL to copy")
            
    def open_url(self):
        try:
            webbrowser.open(self.short_url)
        except AttributeError:
            messagebox.showerror("Error", "No URL to open")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
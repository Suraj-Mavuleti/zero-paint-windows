import customtkinter as ctk
import threading
import time
import math
import socket
import urllib.request
import json
import sqlite3
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zero Paint - Digital Canvas")
        self.geometry("800x600")
        self.configure(fg_color="#1a1a24")
        
        # Header
        self.header = ctk.CTkLabel(self, text="Zero Paint - Digital Canvas", font=("Helvetica", 24, "bold"), text_color="#00C7FF")
        self.header.pack(pady=20)
        
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)
        
        self.setup_ui()
        
    
    def setup_ui(self):
        import tkinter as tk
        
        toolbar = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        toolbar.pack(fill=ctk.X, pady=5)
        
        self.color = "white"
        colors = ["white", "red", "green", "blue", "yellow", "black"]
        for c in colors:
            btn = ctk.CTkButton(toolbar, text=c.capitalize(), fg_color=c if c!="white" else "gray", text_color="black" if c in ["white", "yellow"] else "white", width=50, command=lambda c=c: self.set_color(c))
            btn.pack(side=ctk.LEFT, padx=5)
            
        ctk.CTkButton(toolbar, text="Clear", command=self.clear).pack(side=ctk.RIGHT, padx=5)
        
        self.canvas = tk.Canvas(self.main_frame, bg="black", highlightthickness=0)
        self.canvas.pack(fill=ctk.BOTH, expand=True, pady=10)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
    def set_color(self, c):
        self.color = c
        
    def paint(self, event):
        x, y = event.x, event.y
        r = 5
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.color, outline=self.color)
        
    def clear(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    app = App()
    app.mainloop()

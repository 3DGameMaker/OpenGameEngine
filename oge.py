import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from enum import Enum, auto
import random

class GUIScriptRunner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.current_window = None
        self.widgets = {}
        self.command_handlers = {
            # Window commands
            "create window": self._handle_create_window,
            "set title to": self._handle_set_title,
            "set size to": self._handle_set_size,
            "set background to": self._handle_set_background,
            
            # Widget commands
            "add text": self._handle_add_text,
            "add button": self._handle_add_button,
            "add input": self._handle_add_input,
            "add checkbox": self._handle_add_checkbox,
            
            # Action commands
            "show message": self._handle_show_message,
            "on close": self._handle_on_close
        }
    
    def execute_script(self, script_path):
        try:
            with open(script_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    self._process_command(line)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Script file not found: {script_path}")
            sys.exit(1)
    
    def _process_command(self, command):
        for pattern in self.command_handlers:
            if command.lower().startswith(pattern.lower()):
                arg = command[len(pattern):].strip()
                self.command_handlers[pattern](arg)
                return
        messagebox.showerror("Error", f"Unknown command: {command.split()[0]}")
    
    # Command handlers
    def _handle_create_window(self, arg):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Toplevel()
        self.current_window.protocol("WM_DELETE_WINDOW", self._on_window_close)
        if arg:
            self._handle_set_title(arg)
    
    def _handle_set_title(self, title):
        self._require_window()
        title = title.strip('"\'')
        self.current_window.title(title)
    
    def _handle_set_size(self, size):
        self._require_window()
        width, height = map(int, size.lower().replace('x', ' ').split())
        self.current_window.geometry(f"{width}x{height}")
    
    def _handle_set_background(self, color):
        self._require_window()
        self.current_window.configure(bg=color.strip('"\''))
    
    def _handle_add_text(self, text):
        self._require_window()
        text = text.strip('"\'')
        label = ttk.Label(self.current_window, text=text)
        label.pack(padx=10, pady=5)
    
    def _handle_add_button(self, text):
        self._require_window()
        text = text.strip('"\'')
        button = ttk.Button(self.current_window, text=text)
        button.pack(padx=10, pady=5)
    
    def _handle_add_input(self, name):
        self._require_window()
        name = name.strip('"\'') or f"input_{random.randint(1000,9999)}"
        entry = ttk.Entry(self.current_window)
        entry.pack(padx=10, pady=5)
        self.widgets[name] = entry
    
    def _handle_add_checkbox(self, text):
        self._require_window()
        text = text.strip('"\'')
        var = tk.IntVar()
        cb = ttk.Checkbutton(self.current_window, text=text, variable=var)
        cb.pack(padx=10, pady=5)
    
    def _handle_show_message(self, message):
        message = message.strip('"\'')
        messagebox.showinfo("Message", message)
    
    def _handle_on_close(self, message):
        message = message.strip('"\'')
        self.on_close_message = message
    
    def _on_window_close(self):
        if hasattr(self, 'on_close_message'):
            messagebox.showinfo("Message", self.on_close_message)
        self.current_window.destroy()
        self.current_window = None
        if not any(tk.Toplevel.winfo_children(self.root)):
            self.root.quit()
    
    def _require_window(self):
        if not self.current_window:
            self._handle_create_window("")

    def run(self):
        self.root.mainloop()

def main():
    if len(sys.argv) != 2:
        print("Open Source Game Engine")
        print("Usage: oge <script_file_directory>")
        print("\nExample script:")
        print('  create window')
        print('  set title to "My App"')
        print('  set size to 400x300')
        print('  add text "Welcome!"')
        print('  on close "Thank you for using the app!"')
        sys.exit(1)

    script_path = sys.argv[1]
    
    if os.path.isfile(script_path):
        runner = GUIScriptRunner()
        runner.execute_script(script_path)
        runner.run()
    else:
        messagebox.showerror("Error", f"File not found: {script_path}")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk


class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom Window")
        self.custom_frame = CustomFrame(self)
        self.custom_frame.pack(padx=20, pady=20)

        # Bind the frame's custom event to the window's handler
        self.bind("<<CustomFrameEvent>>", self.handle_frame_event)

    def handle_frame_event(self, event):
        """Handle events from the custom frame"""
        # Access the event data that was passed
        data = event.widget.event_data
        print(f"Window handling frame event with data: {data}")

        # You can perform window-level actions here
        self.title(f"Event Received: {data}")


class CustomFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.event_data = None  # Store data to pass with the event

        # Create some example widgets
        self.button = ttk.Button(self, text="Trigger Event",
                                 command=self.trigger_event)
        self.button.pack(pady=5)

        # Example of binding mouse events
        self.bind("<Button-1>", self.on_click)

    def trigger_event(self):
        """Trigger a custom event that will be handled by the window"""
        self.event_data = "按鈕被按了"
        # Generate custom event that will be caught by the window
        self.event_generate("<<CustomFrameEvent>>")

    def on_click(self, event):
        """Handle mouse click within the frame"""
        self.event_data = f"Clicked at coordinates: ({event.x}, {event.y})"
        self.event_generate("<<CustomFrameEvent>>")


# Example usage
if __name__ == "__main__":
    window = CustomWindow()
    window.mainloop()

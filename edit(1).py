import tkinter as tk
import requests

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor and Optimizer")
        self.root.geometry("500x300")

        self.initial_text = self.fetch_initial_text()  # Get initial text from the API

        self.create_widgets()

    def create_widgets(self):
        self.text_frame = tk.Text(self.root, wrap=tk.WORD, width=60, height=10, font=("Arial", 12))
        self.text_frame.insert(tk.END, self.initial_text)  # Insert initial text into the text box
        self.text_frame.pack(pady=10)

        self.optimize_button = tk.Button(self.root, text="Optimize Text", command=self.optimize_text)
        self.optimize_button.pack(pady=5)

    def fetch_initial_text(self):
        # Function to fetch initial text from the API
        api_url = "https://link.zhihu.com/?target=http%3A//jsonplaceholder.typicode.com/post" #it is a example url
        response = requests.get(api_url)
        if response.status_code == 200:
            initial_text = response.text
        else:
            initial_text = "Failed to fetch initial text from the API."
        return initial_text

    def optimize_text(self):
        optimized_text = self.text_frame.get("1.0", tk.END)  # Get user-edited text
        # Function to send optimized text to the API
        self.send_text_to_api(optimized_text)

    def send_text_to_api(self, text):
        # Function to send text to the API
        api_url = "YOUR_API_URL"  # Replace "YOUR_API_URL" with the actual URL for sending optimized text
        payload = {"text": text}
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print("Optimized text has been successfully sent to the API.")
        else:
            print("Failed to send text to the API. Please check your API settings.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

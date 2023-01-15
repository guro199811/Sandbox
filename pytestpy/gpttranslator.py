import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.geometry("800x600")
root.configure(bg="gray")

# Create a text input field
input_field = ttk.Entry(root, width=100)
input_field.pack(pady=10)

# Create a button to submit the user's input
submit_button = ttk.Button(root, text="Translate", command=translate)
submit_button.pack()

# Create a text output field to display my response
output_field = tk.Text(root, width=100, height=20, bg="white")
output_field.pack()

# Define the translate function
def translate():
    # Get the user's input
    user_input = input_field.get()
    
    # Use the OpenAI API to generate a response
    response = generate_response(user_input)
    
    # Display the response in the output field
    output_field.insert("1.0", response)

# Import the OpenAI API client
from openai import api_key, Client

# Create an OpenAI client
client = Client(api_key=api_key)

# Define the generate_response function
def generate_response(input_text):
    # Use the OpenAI API to generate a response
    response = client.completions(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1024,
        temperature=0.5
    )
    
    # Return the generated response
    return response["choices"][0]["text"]

# Run the main loop
root.mainloop()

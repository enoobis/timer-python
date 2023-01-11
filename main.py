import tkinter as tk

def start_timer():
    # Get the time entered by the user
    count = int(time_var.get())

    # Disable the start button so the timer can't be started again
    start_button['state'] = 'disable'
    
    # Enable the stop button so the user can stop the timer
    stop_button['state'] = 'normal'

    # Start the countdown
    countdown(count)

def stop_timer():
    # Stop the countdown
    label.after_cancel(countdown)
    label['text'] = "Stopped"
    stop_button['state'] = 'disable'
    

def countdown(count):
    # Display the time remaining in the label
    label['text'] = count

    # Check if the timer has reached zero
    if count > 0:
        # If not, decrement the count and call countdown again after 1000ms (1 second)
        label.after(1000, countdown, count-1)
    else:
        label['text'] = "Time's Up!"
        stop_button['state'] = 'disable'

# Create a Tkinter window
root = tk.Tk()
root.geometry("350x150") # set the size of the window
root.title("Countdown Timer") # set the title of the window

# Create a label to display the time remaining
label = tk.Label(root, font=("Courier", 44))
label.pack(pady=20)

# Entry widget to take input from user
time_var = tk.StringVar(value="60") # set the default time
time_entry = tk.Entry(root, textvariable=time_var)
time_entry.pack()

# Create start and stop button
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(root, text="Stop", command=stop_timer)
stop_button.pack(side="right", padx=10)
stop_button['state'] = 'disable'

root.mainloop()


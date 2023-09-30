import subprocess
import time
import os
import threading
import signal
import platform
import keyboard  # Install using 'pip install keyboard'

# Replace 'tur.py' with the name of your Python script
python_script = 'tur.py'

def run_script():
    print("Running the script...")
    try:
        process = subprocess.Popen(["python3", python_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)

        # Make a thread to monitor user input for closing with Escape key
        def monitor_user_input():
            keyboard.wait("esc")
            print("Terminating the script...")
            process.stdin.write("exit\n")
            process.stdin.flush()
            process.terminate()
        
        user_input_thread = threading.Thread(target=monitor_user_input)
        user_input_thread.start()

        # Make a thread to monitor the script's execution
        def monitor_script():
            try:
                process.wait(timeout=20)  # Wait for 5 seconds
            except subprocess.TimeoutExpired:
                print("Terminating the script...")
                process.terminate()
        
        monitor_thread = threading.Thread(target=monitor_script)
        monitor_thread.start()

        # Wait for the script to finish or be terminated by the user
        monitor_thread.join()
        user_input_thread.join()
    except subprocess.CalledProcessError as e:
        print(f"Error running the script: {e}")

if __name__ == "__main__":
    print("Monitoring for changes in 'tur.py'...")

    while True:
        # Wait for the file to be modified (saved)
        modification_time = os.path.getmtime(python_script)
        while modification_time == os.path.getmtime(python_script):
            time.sleep(1)
        
        # Run the script in a separate thread
        script_thread = threading.Thread(target=run_script)
        script_thread.start()
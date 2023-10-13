from flask import Flask
import json
import os
app = Flask(__name__)

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'event_demo_files.json')

with open(file_path) as f:
    events_file = json.loads(f.read())

counter = 0

@app.route('/')
def get():
    global counter  # Use the global counter variable
    try:
        # Get the next event
        msg = events_file[counter]
        counter += 1

    except IndexError as e:
        print("IndexError:", e)
        return 'no events found'

    return msg

f.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
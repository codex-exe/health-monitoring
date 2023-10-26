import os

def save_kb(kb, filename):
    # Create the directory if it doesn't exist
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the knowledge base to a file
    with open(filename, 'w') as f:
        f.write(kb)

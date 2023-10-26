def save_kb(kb, filename):
    # Save the knowledge base to a file
    with open(filename, 'w') as f:
        f.write(kb)
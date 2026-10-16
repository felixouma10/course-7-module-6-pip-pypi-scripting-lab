from datetime import datetime


def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # Generate today's timestamped filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to the file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation
    print(f"Log written to {filename}")

    return filename

import glob

# Get all .txt files in the directory

files = glob.glob("server_dump/*.txt") 

print(files)

import glob
import os

def process_files(directory_path="."):
    """
    Reads all .txt files in the specified directory, counts statuses,
    and provides an option to print filenames.
    """
    # Create the full path for the glob pattern
    search_pattern = os.path.join(directory_path, '*.txt')
    files = glob.glob(search_pattern) #
    
    if not files:
        print(f"No .txt files found in the directory: {os.path.abspath(directory_path)}")
        return

    # Data structure to store counts and associated filenames
    status_counts = {"OK": 0, "WARN": 0, "ERROR": 0}
    status_files = {"OK": [], "WARN": [], "ERROR": []}

    print(f"Found {len(files)} .txt files to process.")

    for filename in files:
        try:
            with open(filename, 'r') as f: #
                content = f.read()
                # Check for the *presence* of status strings in the file content
                # This logic assumes a file generally has one primary status,
                # or we just count if the status string appears at all.
                # A more complex requirement (e.g., count *lines* with status,
                # or assume *one* status per file) would need different logic.
                if "ERROR" in content:
                    status_counts["ERROR"] += 1
                    status_files["ERROR"].append(filename)
                elif "WARN" in content:
                    status_counts["WARN"] += 1
                    status_files["WARN"].append(filename)
                elif "OK" in content:
                    status_counts["OK"] += 1
                    status_files["OK"].append(filename)
        except IOError as e:
            print(f"Error reading file {filename}: {e}") #

    # Print the counts
    print("\n--- Status Summary ---")
    for status, count in status_counts.items():
        print(f"{status}: {count} files")

    # Ask the user if they want to see the filenames
    print("\nDo you want to print all filenames for each status type? (yes/no)")
    user_choice = input().strip().lower()

    if user_choice == "yes" or user_choice == "y":
        print("\n--- Files by Status ---")
        for status in ["OK", "WARN", "ERROR"]:
            print(f"\nFiles with status '{status}':")
            if status_files[status]:
                # Use bullet points for the list of files
                for file_name in status_files[status]:
                    print(f"* {file_name}")
            else:
                print("  None")
    else:
        print("Filenames will not be printed.")

if __name__ == "__main__":
    # You can change the directory here, or leave it as "." for the current directory
    process_files(directory_path=".") wss
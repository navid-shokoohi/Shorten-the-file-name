import os

def shorten_file_names(directory):
    try:
        # Validate the path
        if not os.path.exists(directory):
            print("Invalid path. Please enter a valid absolute path.")
            return

        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            # Create the full file path
            file_path = os.path.join(directory, filename)

            # Check if it is a file
            if os.path.isfile(file_path):
                # Split the filename and extension
                name, extension = os.path.splitext(filename)

                # Shorten the name to 120 characters
                shortened_name = name[:200]

                # Create the new filename
                new_filename = shortened_name + extension

                # Create the new file path
                new_file_path = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(file_path, new_file_path)

        print("File names have been shortened successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get absolute path from user
directory = input("Enter the absolute path of the directory: ").strip()

# Call the function with the provided directory
shorten_file_names(directory)

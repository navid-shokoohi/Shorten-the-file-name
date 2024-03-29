Shorten File Names Utility

This Python script is designed to shorten file names within a specified directory to avoid potential issues caused by long file names, particularly on Windows systems where long paths can sometimes lead to problems opening files.
Purpose

Long file names and paths can sometimes cause compatibility issues with certain software applications, especially on Windows platforms. This script aims to mitigate such issues by shortening file names within a given directory to a specified length.
Usage

    Clone the Repository: Begin by cloning this repository to your local machine using the following command:

    bash

git clone <repository-url>

Navigate to the Repository Directory: Use the cd command to navigate into the cloned repository directory:

bash

cd <repository-directory>

Run the Script: Execute the Python script by providing the absolute path of the directory containing the files you wish to shorten:

    python shorten_file_names.py

    You will be prompted to enter the absolute path of the directory. Provide the path and press Enter.

    Review Output: Once the script completes execution, it will display a message indicating whether the file names were successfully shortened or if any errors occurred.

Important Notes

    Ensure that you have Python installed on your system to run this script.
    It's recommended to make a backup of your files before running the script, as renaming files can be irreversible and may lead to unintended consequences.
    The script shortens file names to a maximum of 210 characters, adjusting both the file name and extension. You can modify this limit within the script if necessary.
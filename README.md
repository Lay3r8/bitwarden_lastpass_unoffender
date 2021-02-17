# Bitwarden Lastpass unoffender

Used to fix the csv generated on the Lastpass website for import in Bitwarden

It will create a second file named "bitwarden_output.csv" where the "password" and "extra" columns containing more than 512 chars have been replaced by a custom message.

Tested on Windows with Python 3.8

Usage: python main.py -f original_csv_file [-v]
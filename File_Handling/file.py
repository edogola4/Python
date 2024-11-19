# File Handling and Exception Handling


'''
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
'''

# File Handling and Exception Handling

def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the input file
            content = infile.read()
            # Modify the content (for demonstration, converting to uppercase)
            modified_content = content.upper()

        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An issue occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for a filename to read
    input_filename = input("Enter the input file name to read from: ")
    output_filename = input("Enter the output file name to write to: ")

    # Call the function to read from and write to the file
    read_and_write_file(input_filename, output_filename)


# Run the program
if __name__ == "__main__":
    main()

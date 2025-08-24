def process_file():
    # Ask file name
    filename = input("Enter filename: ")
    
    try:
        # Read file
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Successfully read {len(content)} characters from {filename}")
        
        lines = content.split('\n')
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        modified_content = '\n'.join(modified_lines)
        
        # Write thew content
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
print(f"Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_file()

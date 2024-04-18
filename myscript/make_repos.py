import os
import csv

class MakeRepos:
    def __init__(self):
        pass

    def merge_csv_files(self, input_dir, output_file='tmp.txt', encoding='latin-1', remove_duplicates=False):
        # Initialize a flag to check if header has been written
        header_written = False

        # input_dir = os.path.normpath(input_dir)

        # Initialize a set to keep track of lines already written if removing duplicates
        lines_written = set()
        
        # Open the output file in write mode with the specified encoding
        with open(output_file, 'w', newline='', encoding=encoding) as outfile:
            writer = csv.writer(outfile)
            
            # List all files in the input directory
            input_files = os.listdir(input_dir)
            
            # Loop through each file in the input directory
            for file_name in input_files:
                if file_name.endswith('.csv'):
                    file_path = os.path.join(input_dir, file_name)
                    
                    # Open each csv file and read its contents with the specified encoding
                    with open(file_path, 'r', newline='', encoding=encoding) as infile:
                        reader = csv.reader(infile)
                        
                        # Skip header if it's not the first file
                        if header_written:
                            next(reader)
                        else:
                            header_written = True
                        
                        # Write the contents to the output file
                        for row in reader:
                            if not remove_duplicates or ','.join(row) not in lines_written:
                                writer.writerow(row)
                                if remove_duplicates:
                                    lines_written.add(','.join(row))


    def split_file(self, input_file, prefix_text='', add_first_line=True, encoding='latin-1'):

        input_file = os.path.normpath(input_file)
        # Read the contents of the input file
        with open(input_file, 'r', encoding=encoding) as infile:
            content = infile.readlines()
        
        # Get the first line of the input file
        first_line = content[0] if content else ''
        
        # Append the first line to the prefix text if requested
        if add_first_line:
            prefix_text += first_line
        
        # Initialize a list to store parts
        parts = []
        
        # Initialize the part content with the prefix text
        part_content = prefix_text
        
        # Split the content into parts with max size of 4000 characters without splitting lines
        for line in content[1:]:
            if len(part_content) + len(line) <= 4000:
                part_content += line
            else:
                parts.append(part_content)
                part_content = prefix_text + line
        if part_content:
            parts.append(part_content)
        
        # Get the file name and extension
        base_name, extension = os.path.splitext(input_file)
        
        # Write each part to a separate file
        for i, part_content in enumerate(parts):
            # Determine the filename for the current part
            part_file_name = f"{base_name}_4000char_part{str(i+1).zfill(4)}{extension}"
            
            # Write the current part content to the file
            with open(part_file_name, 'w', encoding=encoding) as outfile:
                outfile.write(part_content)
        
        # Return the total number of parts created
        return len(parts)

    def merge_csv_files2(self, output_file, encoding='latin-1', remove_duplicates=False):
        # Initialize a flag to check if header has been written
        header_written = False
        
        # Initialize a set to keep track of lines already written if removing duplicates
        lines_written = set()
        
        # Open the output file in write mode with the specified encoding
        with open(output_file, 'w', newline='', encoding=encoding) as outfile:
            writer = csv.writer(outfile)
            
            # List all files in the input directory
            input_files = os.listdir(self.input_directory)
            
            # Loop through each file in the input directory
            for file_name in input_files:
                if file_name.endswith('.csv'):
                    file_path = os.path.join(self.input_directory, file_name)
                    
                    # Open each csv file and read its contents with the specified encoding
                    with open(file_path, 'r', newline='', encoding=encoding) as infile:
                        reader = csv.reader(infile)
                        
                        # Skip header if it's not the first file
                        if header_written:
                            next(reader)
                        else:
                            header_written = True
                        
                        # Write the contents to the output file
                        for row in reader:
                            if not remove_duplicates or ','.join(row) not in lines_written:
                                writer.writerow(row)
                                if remove_duplicates:
                                    lines_written.add(','.join(row))

    def split_file3(self, input_file, prefix_text='', add_first_line=True, encoding='latin-1'):
        # Read the contents of the input file
        with open(input_file, 'r', encoding=encoding) as infile:
            content = infile.readlines()
        
        # Get the first line of the input file
        first_line = content[0] if content else ''
        
        # Append the first line to the prefix text if requested
        if add_first_line:
            prefix_text += first_line
        
        # Initialize a list to store parts
        parts = []
        
        # Initialize the part content with the prefix text
        part_content = prefix_text
        
        # Split the content into parts with max size of 4000 characters without splitting lines
        for line in content[1:]:
            if len(part_content) + len(line) <= 4000:
                part_content += line
            else:
                parts.append(part_content)
                part_content = prefix_text + line
        if part_content:
            parts.append(part_content)
        
        # Get the file name and extension
        base_name, extension = os.path.splitext(input_file)
        
        # Write each part to a separate file
        for i, part_content in enumerate(parts):
            # Determine the filename for the current part
            part_file_name = f"{base_name}_4000char_part{str(i+1).zfill(4)}{extension}"
            
            # Write the current part content to the file
            with open(part_file_name, 'w', encoding=encoding) as outfile:
                outfile.write(part_content)
        
        # Return the total number of parts created
        return len(parts)

    
    @staticmethod
    def convert_directory_to_tmpfile(input_directory: str) -> str:
        """
        Convert the input directory path to a merge file path.

        Args:
            input_directory (str): The input directory path.

        Returns:
            str: The merge file path.
        """
        # Sanitize the input directory
        sanitized_input_directory = os.path.normpath(input_directory)

        # Extract the directory names and concatenate them with underscores
        directory_parts = sanitized_input_directory.split(os.sep)
        directory_name = '_'.join(directory_parts)

        # Create the merge file path
        merge_file_path = os.path.join('tmp', f"test_merge_{directory_name}.csv")

        return merge_file_path

#### Examples:
# These examples send output to tmp directory !!
def example0():
    """
    This function demonstrates how to use the MakeRepos class to convert
    an input directory path to a merge file path.
    """
    # Instantiate the MakeRepos class
    make_repos = MakeRepos()

    # Define the input directory path
    input_directory = r'subject\frequentiedatabase\strict_csv'

    # Convert the input directory path to a merge file path
    merge_file = make_repos.convert_directory_to_tmpfile(input_directory)

    # Output the merge file path
    print(merge_file)


def example1():
    """
    Merging *.csv from a directory to a fixec filename
    """
    make_repos = MakeRepos()

    input_dir = r'subject\frequentiedatabase\strict_csv'
    merge_file = r'tmp/merged_output.csv'
    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    

def example2():
    """
    Merging *.csv from a directory to tmp/<From_dir_created_filename>.csv 
    """
    make_repos = MakeRepos()

    input_dir = r'subject\frequentiedatabase\strict_csv'
    merge_file = make_repos.convert_directory_to_tmpfile(input_dir)
    # os.path.join('tmp', f"test_merge_{input_dir.replace('/', '-')}.csv")

    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    


def example3():
    """
    Merging *.csv from a directory.
    """
    make_repos = MakeRepos()

    input_dir = r'subject\frequentiedatabase\strict_csv'
    merge_file = r'tmp/example3_merged_data.csv'

    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    


def example4():
    """
    Splitting up a file.
    """
    make_repos = MakeRepos()
    input_file = r'tmp/example3_merged_data.csv'

    total_parts = make_repos.split_file(input_file, prefix_text='# Start of part:\n', add_first_line=True)
    print(f"Total {total_parts} parts created.")


def example5():
    """
    Merging *.csv from a directory and then splitting it up.
    """
    make_repos = MakeRepos()

    input_dir = r'subject\frequentiedatabase\strict_csv'
    merge_file = r'tmp/merged_data.csv'

    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    

    total_parts = make_repos.split_file(merge_file, prefix_text='# Radio information (in parts):\n', add_first_line=True)
    print(f"Total {total_parts} parts created.")


def main():
    # example0()        # Not testing a function - testing conversion of ...
    # example1()        # Merging *.csv from a directory.
    # example2()        # Merging *.csv from a directory.
    # example3()        # Merging *.csv from a directory.
    # example4()        # Splitting up a file.
    # example5()        # Merging *.csv from a directory and then splitting it up.
    # example5()
    pass

if __name__ == "__main__":
    main()

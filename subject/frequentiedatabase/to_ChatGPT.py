import os
import sys
import csv

sys.path.insert(0, 'myscript')

from make_repos import MakeRepos # type: ignore



def program():
    """
    Merging *.csv from a directory and then splitting it up.
    """
    make_repos = MakeRepos()

    input_dir = r'subject\frequentiedatabase\strict_csv'
    merge_file = r'to_ChatGPT\freqdb.csv'

    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    

    total_parts = make_repos.split_file(merge_file, prefix_text='# Radio information (in parts):\n', add_first_line=True)
    print(f"Total {total_parts} parts created.")



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
    program()
    pass

if __name__ == "__main__":
    main()

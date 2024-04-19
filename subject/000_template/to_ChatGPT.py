### 000_template\to_ChatGPT.py
## Copy and adapt this to your needs
import os
import sys
import shutil

## My imports
sys.path.insert(0, 'myscript')
from make_repos import MakeRepos # type: ignore

def main():
    """
    <yoursubject> info creator
        REMARK First empty the to-ChatGPT directory !!
        Make a copy of the intro.txt file in the to_ChatGPT directory
        Merge the files in subject/<yoursubject>/strict_csv/  
          after that splitup the merge_file and place the output in the to_ChatGPT directory. 
        The merge_file can be found in the tmp directory
    """
    make_repos = MakeRepos()

    ## Source file path
    source_file = r'subject\<yoursubject>\intro.txt'
    ## Destination file path
    destination_file = r"to_ChatGPT\<yoursubject>_0_intro.txt"


    ### Copy the intro.txt file
    shutil.copy(source_file, destination_file)

    input_dir = r'subject\<yoursubject>\strict_csv'
    merge_file = r'to_ChatGPT\<yoursubject>.csv'

    make_repos.merge_csv_files(input_dir, merge_file, remove_duplicates=True)    

    total_parts = make_repos.split_file(merge_file, prefix_text='!! # <yoursubject> information (in parts):\n', add_first_line=True)
    print(f"Total {total_parts} parts created.")

    ### Move merge_file to directory tmp
    destination_directory = "tmp/"
    
    ## Get the filename without the extension
    filename, extension = os.path.splitext(os.path.basename(merge_file))

    ## Counter to add to the filename
    counter = 1

    ## Keep trying until we find a unique filename
    while os.path.exists(os.path.join(destination_directory, filename + "_" + str(counter) + extension)):
        counter += 1

    new_filename = filename + "_" + str(counter) + extension

    ## Move the file with the new filename
    shutil.move(merge_file, os.path.join(destination_directory, new_filename))

    ## Ready Now you can copy and paste the content of the to_ChatGPT files to ChatGPT to give ifo about <yoursubject>

if __name__ == "__main__":
    main()

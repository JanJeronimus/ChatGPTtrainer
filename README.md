# ChatGPT trainer
Create files to feed new data to ChatGPT using copy and paste

This GitHub contains tools to convert data in a digestible format for ChatGTP ( The fee 3.5 web based version).
Requirements : Python,  Free ChatGTP account

Use case:
I asked ChatGPT (GPT-3.5 model chat.openai.com on 17apr2024): 
"What is the length of text i can type in here?"
The responce was:
"You can type up to 4096 characters in a single message. If you need to convey more information, you can break it up into multiple messages."


This is created to break up information into multiple messages.

The tool splits information in digestable parts of around 4000 characters in separate files in the 4ChatGTP directory.
To feed this information you need to:
1) Copy this from GitHub to your computer. 
2) Empty the 4ChatGTP/ directory  (files with info for ChatGTP will be placed in this directory).
		(Optional delete items in the tmp directory )
3) Copy the data in a subdirectory of subject/{yoursubject}/    -  Create this directory for your own subject. 
																	In this github are available
																			subject/000_template/	Empty template for <yoursunject>
																			subject/quansheng/  Quansheng codeplug 

4) Run the  script subject/{yoursubject}/to_chatgpt.py            -  Example subject/{yoursubject}/to_chatgpt.py  
	To do several common things Python scripts ( Class Functions contants ) are available in the script directory that can be called from your to_chatgpt.py  

5) Copy and paste the content of the to_ChatGTP/ files in ChatGTP

Important information regarding the demo  subject/quansheng : 
You need to provide your own codeplug data by copying the Quansheng Chirp csv file in the subject/quansheng/strict_csv/
The subject/quansheng/4chatgpy.py program will 
Make a copy of the intro.txt file in the to_ChatGPT directory
merge the files in subject/quansheng/strict_csv/ and after that splitup the merge_file and place the output in the to_ChatGPT directory. 


Possible improvements to do are in ToDo.md

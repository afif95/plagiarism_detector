# Among the sample data, I have considered 1.txt as the source file and 2.txt as the file being checked.

# run the detector.py using the Makefile in the terminal; for example: make FILE1=<path>/plagiarism06/1.txt FILE2=<path>/plagiarism06/2.txt run

# It will generate output 1 for plagiarised text and 0 for non-plagiarised text.

# In the code, f1 and f2 are receiving the file path as arguments and the files are being opened in read mode.

# Both of the files are being preprocessed where particular words and punctuations are being removed and full text is being converted to lowercase letters.

# preprocess_common() returns the remaining words as Lists.

# hold_length1 and hold_length2 contain the length of the Lists.

# conv_dictionary() converts the Lists into Dictionary where the key is a word and value is the frequency of that word.

# dic1 and dic2 contain the Dictionaries returned by conv_dictionary().

# conv_list() converts the keys of the previous Dictionaries into Lists so that no duplicates are present and newfile1 and newfile2 store the Lists.

# In the output_generator(), if a non-empty word of newfile2 is present in newfile1 then the minimum value of that word from dic1 and dic2 is being added to the counter.

# If the calculated percentage of counter based on the length of the file being checked (hold_length2) is above 50, then 2.txt is plagiarised from 1.txt and output is set to 1; otherwise 0.

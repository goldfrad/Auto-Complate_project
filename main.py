import trie
import time
import input_processing
import os
import sys
import ID_sentence

ID = 0
ID_sentences = list()

def insert_data(root, file_name):
    global ID
    
    with open(file_name, encoding="utf8") as fp:
        line = fp.readline()
        cnt = 1
        
        while line:
            print(cnt)
            ID_sentences.append(ID_sentence.ID_sentence(file_name, cnt))
            sentence =  line.strip()
            for i in range(len(sentence)):
                root.insert(input_processing.clearing_the_sentence(sentence), i, ID)
                
            ID += 1
            line = fp.readline()
            cnt += 1
            
            
def main():
    
    t = trie.Trie()
    
    insert_data(t, "abstract.txt")
    insert_data(t, "allocation.txt")
    insert_data(t, "apiabiversion.txt")
    insert_data(t, "arg.txt")
    insert_data(t, "bool.txt")
    insert_data(t, "buffer.txt")
    insert_data(t, "bytearray.txt")
    insert_data(t, "bytes.txt")
    
#   URL = t.search(input_processing.clearing_the_sentence("go"))
#   for url in URL:
#       if url:
#           print(url)
# 
if __name__ == '__main__': 
    main() 
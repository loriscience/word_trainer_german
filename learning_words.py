import pandas as pd 
import numpy as np


def start_game(words): 
    
    score = 0 
    number_of_question = len(words)
    
    fail_list = []
    
    for row in words.itertuples() : 
        
        
        if row.Artikel == "-": 

            val = input(f"What is the meaning of {row.Word} = ")
            
            if val.lower() == row.Meaning.lower() : 
                print("Correct !")
                
                score += 1
            
            else : 
                print("False !")
                fail_list.append(row.Word)
            
        
        else : 
            val = input(f"What is the meaning of {row.Word} = ")
            artikel = input(f"What is the artikel of {row.Word} = ")
            
            
            if val.lower() == row.Meaning.lower() and artikel.lower() == row.Artikel.lower(): 
                print("Correct ! ")
                score += 1
            
            else : 
                print("False ! ")
                fail_list.append(row.Word)
            
    
        
    print(f"Your answered {(score / number_of_question) * 100} % of the questions correctly ")
    print("Work on these words")
    print(fail_list)
    

def main() : 


    df = pd.read_csv("words.csv")

    words = df[["Artikel", "Word","Meaning"]]
    start_game(words)




if __name__ == "__main__": 
    main()



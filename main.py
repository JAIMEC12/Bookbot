from stats import count_words, count_characters
import sys

# OPEN THE FILE IN WHICH THERE IS THE TEXT OF THE BOOK
# BOOK VARIABLE MEANS THE PATH WHERE THE FILE IS LOCATED
def get_book_text(book):
    book_content = ""
    #OPEN THE FILE WITH R MEANING ONLY FOR READING AND ENCODE = UTF-8 IS TO TRANSFORM THE STRINGS INTO A SEQUENCE OF BYTES USING UTF-8 FORMAT IN ORDER TO HANDLE TEXT FILES WITH SPECIAL CHARACTERS EASILY
    with open(book, "r", encoding="utf-8") as file:
        book_content = file.read() #RETURN ALL THE TEXT AS A STRING
    return book_content 

def main():
    #IF IN THE COMMAND LINE THERE IS NO TWO ENTRIES 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") # IT WILL EXPLAIN THE CORRECT USAGE OF THE PROGRAM
        sys.exit(1) #ALLOW TO EXIT THE PROGRAM WITH A STATUS CODE 1

    #GET THE CONTENT OF THE BOOK WHICH IS SPECIFIED AS ARGUMENT IN THE FUNCTION
    file = get_book_text(sys.argv[1]) # WE USE THE SECOND ARGUMENT WRITTEN IN THE COMMAND LINE WHICH HAS TO BE THE PATH WHERE THE BOOK IS LOCATED

   #REPORT 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}") #NAME OF THE BOOK OR FILE
    print("----------- Word Count ----------")
    print(f"Found {count_words(file)} total words") #FUNCTION TO GET THE TOTAL OF WORDS IN THE TEXT
    print("--------- Character Count -------")
    
    result = count_characters(file) # VARIABLE WHOSE CONTENT IS A LIST OF CHARACTERS USED IN THE TEXT AND THE NUMBER OF TIMES WHICH HAVE BEEN USED
    
    for data in result:
        if data["char"].isalpha(): #IF THE CHARACTER IS ALPHABETICAL
            print(f"{data["char"]} : {data["num"]}")  #THEY WILL BE PRINTED WITH THEIR TOTAL OF TIMES

if __name__ == "__main__":
    main()
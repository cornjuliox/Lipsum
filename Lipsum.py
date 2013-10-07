import random
import string
import os
from timeit import Timer

# It's been about a few monthss since I first wrote this function. I realize now that
# it was a mistake to try and turn that thing into a class.
def GenerateLipsum(f_path, max_words=250, clean=False):
        """ Generates a "Lipsum" - a block of dummy text used for testing page layouts in Web Design.
        takes 3 arguments:
                f_path    - Path to the file that is to be used as the Lipsum source.
                max_words - The length of the desired lipsum, defaults to 250.
                clean     - Determines whether or not to clean the Lipsum, meaning strip out all the
                            punctuation.
        
        Returns a string.
        """
        f_obj = open(f_path, "rb")
        draft = f_obj.read()
        newseq = []
        if clean == True:
                table = string.maketrans(string.lowercase, string.lowercase)
                draft_2 = draft.translate(table, string.punctuation)
                draft_3 = draft_2.split()
                for x in range(0, max_words):
                        newseq.append(random.choice(draft_3))
                return " ".join(newseq)
        else:
                draft = draft.split()
                for x in range(0, max_words):
                        newseq.append(random.choice(draft))
                f_obj.close()
                return " ".join(newseq)

        
if __name__ == "__main__":
    # There is be a better way to write these tests, but this should do for now. I SPOTTED THE SECRET LETTER
    test_books = ["The Art of War by Sun Tzu.txt" ,"The Practice and Science of Drawing.txt",
                "Manners Custom and Dress of the Middle Ages.txt"]
    results = []
    for x in test_books:
        if not os.path.exists(x):
            print "%s was not found. The built-in test will not work without it."
        else:
            # I <3 Python.
            results.append(GenerateLipsum(x))

    print "Standard lipsums, generated from test files."
    for x in results:
        print "--------------------------------"
        print "Standard lipsum, len(result) = %s words" % (len(x.split()))
        print "--------------------------------"
        print x
        print "--------------------------------"
        print "--------------------------------"
        print
        
    print
    print "TEST COMPLETE"
    


    

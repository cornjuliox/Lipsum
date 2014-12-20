import random

# debating on whether or not I should put this in a separate file, or
# just keep it as is.
block_of_text = """But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was
born and I will give you a complete account of the system and expound the actual teachings of the great explorer
of the truth the master-builder of human happiness No one rejects dislikes, or avoids pleasure itself because it
is pleasure but because those who do not know how to pursue pleasure rationally encounter consequences that are
extremely painful Nor again is there anyone who loves or pursues or desires to obtain pain of itself because it is
pain but because occasionally circumstances occur in which toil and pain can procure him some great pleasure To take
a trivial example which of us ever undertakes laborious physical exercise except to obtain some advantage from it
But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences or
one who avoids a pain that produces no resultant pleasure """

def GenerateLipsum(length=1):
    """
    Generates a block of text, randomly selecting from the block_of_text in Lipsum.py, up
    to 'length'. 'length' defaults to 1 if not provided.
    """
    # single line unreadability!
    return " ".join([
        block_of_text.split()[random.randint(1,len(block_of_text.split())-1)] for x in xrange(0,length)
    ])

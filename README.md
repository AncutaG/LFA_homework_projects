# LFA_homework_projects- Project 1 (DFA)

A simple function (a DFA check) in Python was implemented and it takes as input the word that should be checked, returning a tuple containing:
- the path (of nodes)
- the result (*True*- for recognized words or *False*- for unrecognized words)
----------------------------------------------------------------------------------
* I've used a dictionary for the adjacency list having as key, the node and as values, for that key, a list of tuples (in the case of more different transitions from that node). 
* I've used the pythonic unpacking in order to take the output that I've actually needed. 

The result component from the tuple mentioned above (*returned by the function*) is triggered by the fact that the word was/ was not checked fully, so once a letter is not recognized it doesn't move further to the next node with the checking and the boolean value for the result is False. Otherwise, it moves further with the checking and the word gets accepted as language by the little  DFA.

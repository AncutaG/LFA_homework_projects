# the output for check function is thought to be in the form of a tuple:
# (path-> a list of nodes, result->True or False)

def check(word):
# we always have a starting node on our DFA path of letters
    node = start
# the path will be a list of travelled nodes to be filled in as we move to the next state  
    path = [node] 
    counter = 0 # we count the letters that we check one by one
    

    for letter in word:  # we check letter by letter
# relation is a tuple containing 2 things: 
# the next node within the path 
# and the string needed in order to go to that next node e.g: (2, 'a') <-> 'a' takes us to node 2

        for relation in neighbours[node]: 
# we check for next transition, for what comes from node 1 as further relation in terms of correct letter=relation[1]
            if relation[1] == letter:
                
# if the letter is correct then the transition happens and we move to the next node
                node = relation[0] # relation[0] is the node
# we add the node to the path in order to have the full path at the end
                path.append(node)
                counter += 1
                break
            
    # if counter < len(word):
    #     return (path, False)
    return (path, node in final_states) #  node in final_states cand take either False or True value 

input = open("Input_DFA")
# n ->number of nodes
# m ->number of transitions
n, m = tuple(int(elem) for elem in input.readline().split())

# a dictionary where the key is the node (we check pairs of nodes) and the value of key is a list of tuples 
# each tuple has the node (destination) and the string (condition for the destination)

# the list of nodes with an empty list associated
neighbours = {int(state):[] for state in range(1,n+1)}
# input.readline().split()

# unpacking the read line (we always have to check between 2 nodes in essence)
for i in range(m):
    node1, node2, string = input.readline().split()
    neighbours[int(node1)].append((int(node2), string))


start = int(input.readline())
number_finals, *final_states = tuple(int(final_state) for final_state in input.readline().split())
# print(number_finals, final_states)

# final_states = set(int(final_state) for final_state in input.readline().split())
number_words = int(input.readline())
words = [input.readline().strip() for elem in range(number_words)]
input.close()


output = open("Output_DFA", "w")
for word in words:
    path, result = check(word)
    output.write(f"Cuvantul {word} este ACCEPTAT cu traseul: {' '.join(str(node) for node in path)}\n" 
                if result else f"Cuvantul {word} este RESPINS.\n")
output.close()


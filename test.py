class Alphabet:
    def __init__(self, word):
        self.word = word 
    def __repr__(self):
        return f"Word({self.word})"
        
class State:
    def __init__(self, name):
        self.name = name 
    def __repr__(self):
        return f"State({self.name})"
        
class Transition:
    def __init__(self, state1, state2, word):
        self.state1 = state1
        self.state2 = state2
        self.word = word
    def __repr__(self): 
        return f"Transition(\n   state={self.state1},\n   to state={self.state2})"

        

class FiniteAutomate:
    def __init__(self,name):
        self.name = name 
        self.words = []
        self.states = []
        self.transitions = []
        self.initial_states = []
        self.final_states = []
        
    def add_state(self, state):
        self.states.append(state)
    
    def get_state_from(self, state_name):
        for state in self.states:
            if state.name == state_name:
                return state
        return None

    
    def add_word(self, word):
        self.words.append(word)
        
    def read_from_file(self,filename):
        with open(filename, 'r') as file:

            # Read and generate words
            num_words = int(file.readline().strip())
            for i in range (num_words):
                new_word = Alphabet(chr(i + 97))
                self.add_word(new_word)

            # Read and generate the states                            
            num_states = int(file.readline().strip())
            for i in range (num_states):
                new_state = State(f'{i}')
                self.add_state(new_state)
            
            # Read initial states
            initial_states_info = file.readline().strip().split()
            num_initial_states = int(initial_states_info[0])
            initial_states = set(initial_states_info[1:num_initial_states + 1])
            for state_name in initial_states :
                self.initial_states.append(self.get_state_from(state_name))    
            print(initial_states)
                
            
       
    
    def __repr__(self):
        return f"FA(\n   name={self.name},\n   words={self.words},\n   states={self.states},\n   initial_states={self.initial_states})"


def display_finite_automate(fa):
    print("Finite Automate name:", fa.name)
    print("Alphabet:", fa.words)
    print("States:", fa.states)
    


def display_finite_automate_amandine(fa):
    print("Finite Automate name:", fa.name)
    print("Alphabet:", fa.words)
    print("States:", fa.states)



fa = FiniteAutomate("Test")
#fa.read_from_file("Inputs/Int3-2-3.txt")
#display_finite_automate(fa)

fa.words = ['a' , 'b']

def display_table(FA):
    """
    Display a table of elements in the list.

    Parameters:
    elements (list): The list of elements to display.
    """
    for index, word in enumerate(FA.words):
        if index > 0:  # Skip printing the separator for the first element
            print(' / ', end='')
        print(word, end='')


    #print("Index\tElement")
    #print("----------------")
    #for index, element in enumerate(elements):
        #print(f"{index}\t{element}")

# Example usage
my_list = ['apple', 'banana', 'orange', 'kiwi']
display_table(fa)

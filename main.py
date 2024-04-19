import re

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
        self.from_state = state1
        self.to_state = state2
        self.word = word
    def __repr__(self): 
        return f"Transition({self.from_state}->{self.word}->{self.to_state})"

        

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
    
    def get_word_from(self, word_name):
        for word in self.words:
            if word.word == word_name:
                return word
        return None
    
    def is_standard(self) -> bool:
        #TODO to complete/modify
        if len(self.initial_states) == 1:
            # Check if no transition is going to initial state
            initial_state = self.initial_states[0]
            status = True
            for transition in self.transitions:
                if transition.to_state is initial_state : # Warning use is function to compare same object in memory
                    return False
            return True
        else:
            return False
        
    # TODO : à implémenter
    def is_deterministic(self) -> bool:
        return True

    # TODO : à implémenter
    def is_complete(self) -> bool:
        return True
    
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
            #print(initial_states)
            
            # Read final states
            final_states_info = file.readline().strip().split()
            num_final_states = int(final_states_info[0])
            final_states = set(final_states_info[1:num_final_states + 1])
            for state_name in final_states :
                self.final_states.append(self.get_state_from(state_name))    
            #print(final_states)

            # Read transitions
            num_transitions = int(file.readline().strip())
            #print(num_transitions)
            
            for _ in range(num_transitions):
                text = file.readline().strip()
                parts = re.split(r'(\d+)([a-zA-Z])(\d+)', text) # use regex to separate items
                # Remove any empty strings from the list which can occur due to how re.split() includes results
                parts = [part for part in parts if part]
                source_state = parts[0]
                word = parts[1]
                ending_state = parts[2]
                self.transitions.append(Transition(self.get_state_from(source_state),self.get_state_from(ending_state),self.get_word_from(word)))
                #print(f"Transistion {source_state}-{word}-{ending_state}")
            
    
    def __repr__(self):
        return f"FA(\n   name={self.name},\n   words={self.words},\n   states={self.states},\n   initial_states={self.initial_states}),\n   final_states={self.final_states}),\n   transition={self.transitions})"


"""def display_finite_automate(fa):
    print("Finite Automate name:", fa.name)
    print("Alphabet:", fa.words)
    print("States:", fa.states)
    print("Initial states:", fa.initial_states)
    print("Final states:", fa.final_states)
    print("Transitions:", fa.transitions)
        


def display_finite_automate_amandine(fa):
    print("Finite Automate name:", fa.name)
    print("Alphabet:", fa.words)
    print("States:", fa.states)"""

def diplay_FA(FA):
    #TODO print the automaton

def standardization(FA) :
    #TODO return the standardize automaton

def completion(FA):
    #TODO the completion of the automaton
    return

def determinization_and_completion_automaton (FA) :
    #TODO return the determinize and complete automaton

def display_complete_dererministic_automaton(CDFA) :
    #TODO print the CDFA

def minimization(CDFA) :
    #TODO return the minimized automaton

def display_minimal_automaton(MCDFA) : 
    #TODO print the MCDFA

fa = FiniteAutomate("Test")
#fa.read_from_file("Inputs/Int3-2-20.txt")
fa.read_from_file("Inputs/Int3-2-4.txt")
display_finite_automate(fa)
fa.is_standard()


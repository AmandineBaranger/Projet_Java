import re
import os
from enum import Enum
import tabulate
from tabulate import tabulate

# from pydantic import BaseModel

# Define classes for Alphabet, State, and Transition


####################################################
# Alphabet Class
####################################################
class Alphabet:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"Word({self.word})"


####################################################
# State Class
####################################################
class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"State({self.name})"

class TransitionType(Enum):
    STANDARD = 1
    LOOP = 2
    EPSILON = 3

####################################################
# Transision Class
####################################################
class Transition:
    def __init__(self, from_state, to_state, word):
        self.from_state = from_state
        self.to_state = to_state
        if word=='ε':
            #@print("Epsilon")
            self.type = TransitionType.EPSILON
            self.word = None
        elif from_state is to_state:
            #print("Loop")
            self.type = TransitionType.LOOP
            self.word = word
        else:
            #print("Standard")
            self.type = TransitionType.STANDARD
            self.word = word
            
    def is_loop(self) -> bool:
        if self.type == TransitionType.LOOP:
            return True
        return False
    
    def is_standard(self) -> bool:
        if self.type == TransitionType.STANDARD:
            return True
        return False
    
    def is_epsilon(self) -> bool:
        if self.type == TransitionType.EPSILON:
            return True
        return False

    def __repr__(self):
        return f"Transition({self.type} : {self.from_state}->{self.word}->{self.to_state})"
    



####################################################
# Define class for FiniteAutomaton
####################################################
class FiniteAutomate:
    def __init__(self, name):
        self.name = name
        self.alphabet = []
        self.states = []
        self.transitions = []
        self.initial_states = []
        self.final_states = []

    def add_state(self, state):
        """Add a state to the automaton."""
        self.states.append(state)

    def get_state_from_name(self, state_name):
        """Get a state from its name."""
        for state in self.states:
            if state.name == state_name:
                return state
        raise Exception("Sorry, no state with this name")
        return None

    def is_in_inital_states(self, initial_state) -> bool:
        """Check if a state is an initial state."""
        if not isinstance(initial_state, State):
            raise TypeError("Error: must be a State")
        for state in self.initial_states:
            if state is initial_state:
                return True
        return False

    def is_in_final_states(self, final_state) -> bool:
        """Check if a state is a final state."""
        if not isinstance(final_state, State):
            raise TypeError("Error: must be a State")
        for state in self.final_states:
            if state is final_state:
                return True
        return False

    def get_word_from(self, word_name):
        """Get a word from its name."""
        if not isinstance(word_name, str):
            raise TypeError("Error: must be a string")
        for word in self.alphabet:
            if word.word == word_name:
                return word
        return None

    def is_standard(self) -> bool:
        """Check if the automaton is in standard form."""
        if len(self.initial_states) == 1:
            # Check if no transition is going to initial state
            initial_state = self.initial_states[0]
            status = True
            for transition in self.transitions:
                if (
                    transition.to_state is initial_state
                ):  # Warning use is function to compare same object in memory
                    return False
            return True
        else:
            return False

    def is_deterministic(self) -> bool:
        """Check if the automaton is deterministic."""
        # Verifies for each state and each symbols of the alphabet
        for state in self.states:
            for word in self.alphabet:
                # Count the number of transitions for the current state and the current alphabet
                transitions_count = sum(
                    1
                    for transition in self.transitions
                    if transition.from_state == state and transition.word == word
                )
                # If the number of transitions is greater than 1, then this automaton is not deterministic
                if transitions_count > 1:
                    return False
        return True

    def is_complete(self) -> bool:
        """Check if the automaton is complete."""
        # Verifies for each states and each symbols of the alphabet
        for state in self.states:
            for word in self.alphabet:
                # Search a corresponding transition
                transition_found = any(
                    transition.from_state == state and transition.word == word
                    for transition in self.transitions
                )
                # If no transition is found, then the automata is not complete
                if not transition_found:
                    return False
        return True
    
    def has_epsilon_transitions(self) -> bool:
        for transition in self.transitions:
            if transition.type == TransitionType.EPSILON:
                return True
        return False

    def add_word(self, word):
        """Add a word to the alphabet."""
        self.alphabet.append(word)

    def read_from_file(self, filename):
        """Read data from a file and initialize the automaton."""
        with open(filename, "r") as file:

            # Read and generate words
            num_words = int(file.readline().strip())
            for i in range(num_words):
                new_word = Alphabet(chr(i + 97))
                self.add_word(new_word)

            # Read and generate the states
            num_states = int(file.readline().strip())
            for i in range(num_states):
                new_state = State(f"{i}")
                self.add_state(new_state)

            # Read initial states
            initial_states_info = file.readline().strip().split()
            num_initial_states = int(initial_states_info[0])
            initial_states = set(initial_states_info[1 : num_initial_states + 1])
            for state_name in initial_states:
                self.initial_states.append(self.get_state_from_name(state_name))
            # print(initial_states)

            # Read final states
            final_states_info = file.readline().strip().split()
            num_final_states = int(final_states_info[0])
            final_states = set(final_states_info[1 : num_final_states + 1])
            for state_name in final_states:
                self.final_states.append(self.get_state_from_name(state_name))
            # print(final_states)

            # Read transitions
            num_transitions = int(file.readline().strip())
            # print(num_transitions)

            for _ in range(num_transitions):
                text = file.readline().strip()
                parts = re.split(
                    r"(\d+)([a-zε])(\d+)", text
                )  # use regex to separate items 
                # Remove any empty strings from the list which can occur due to how re.split() includes results
                # ε for empty word
                parts = [part for part in parts if part]
                source_state = parts[0]
                word = parts[1] #
                print(word)
                ending_state = parts[2]
                if word != "ε":
                    self.transitions.append(
                        Transition(
                            self.get_state_from_name(source_state),
                            self.get_state_from_name(ending_state),
                            self.get_word_from(word),
                        ))
                        
                else: # mange the epsilon transaction
                    self.transitions.append(
                        Transition(
                            self.get_state_from_name(source_state),
                            self.get_state_from_name(ending_state),
                            "ε",
                        ))
                # print(f"Transistion {source_state}-{word}-{ending_state}")

    # Display the automaton
    def __repr__(self):
        return f"FA(\n   name={self.name},\n   alphabet={self.alphabet},\n   states={self.states},\n   initial_states={self.initial_states}),\n   final_states={self.final_states}),\n   transition={self.transitions})"


####################################################
# Functions definitions
####################################################

####################################################
# Function to list files in a directory
####################################################

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


####################################################
# Function to display the automaton
####################################################
def display_FA(fa):
    """Display the automaton."""
    header = []
    header.append(" ")
    header.append(" ")
    for word in fa.alphabet:
        header.append(word.word)
        
    if fa.has_epsilon_transitions():
        header.append("ε")

    table = [header]

    for state in fa.states:
        row = []
        if fa.is_in_inital_states(state):
            row.append("->")
        elif fa.is_in_final_states(state):
            row.append("<-")
        else:
            row.append(" ")

        row.append(state.name)

        for _ in range(len(fa.alphabet)):
            row.append("--")
        if fa.has_epsilon_transitions():
            row.append("--")
        table.append(row)

    last_column_index = len(fa.alphabet) + 2
    
    for transition in fa.transitions:
        if transition.is_standard() or transition.is_loop() :
            #print(transition)
            source = int(transition.from_state.name) + 1
            dest = int(transition.to_state.name)
            word = ord(transition.word.word) - 95
            if table[source][word] == "--":
                table[source][word] = dest
            else:
                table[source][word] = f"{table[source][word]},{dest}"
        else: # Case for Epsilon
            source = int(transition.from_state.name) + 1
            dest = int(transition.to_state.name)
            if table[source][last_column_index] == "--":
                table[source][last_column_index] = dest
            else:
                table[source][last_column_index] = f"{table[source][last_column_index]},{dest}"
        
    print(tabulate(table, tablefmt="simple_grid"))


####################################################
# Testing
####################################################


"""directory = 'Inputs/'
files = list_files(directory)
#print(files)

automata = []

for file in files:
    automaton = FiniteAutomate(file)
    path = f"{directory}{file}"
    print("-->"+path)
    automaton.read_from_file(f"{directory}{file}")
    display_FA(automaton)
    automata.append(automaton)"""

#print(automata)

# Create the FiniteAutomate object and read data from file
fa = FiniteAutomate("Test")
fa.read_from_file("Inputs/Int3-2-33.txt")

# Display the automaton
test = display_FA(fa)

if fa.is_standard():
    print("The automaton is standard")
else:
    print("The automaton is not standard")

if fa.is_complete():
    print("The automaton is complete")
else:
    print("The automaton is not complete")

if fa.is_deterministic():
    print("The automaton is not deterministic")
else:
    print("The automaton is deterministic")

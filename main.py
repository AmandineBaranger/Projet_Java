

class State:
    def __init__(self, name):
        self.name = name 
    def __repr__(self):
        return f"State({self.name})"
        
class Transition:
    def __init__(self, state1, state2):
        self.state1 = state1
        self.state2 = state2
        
    def __repr__(self):
        return f"Transition(\n   state={self.state1},\n   to state={self.state2})"

        

class FiniteAutomate:
    def __init__(self,name):
        self.name = name 
        self.states = []
        self.transition = []
        self.initial_states = []
        
    def add_state(self, state):
        self.states.append(state)
        
        
    def __repr__(self):
        return f"FA(\n   name={self.name},\n   states={self.states},\n   initial_states={self.initial_states})"

state1 = State("q0")
state2 = State("q1")
trans1 = Transition(state1,state2)
trans2 = Transition(state2,state1)

FA = FiniteAutomate("test")
FA.add_state(state1)


print(test)
print(trans1)
print(trans2)
print(FA)


import StateMachine

"""
 Do we begin with simple cases or complex cases?  
 Are each of the test cases meant to be self contained?  Yes

 Do we throw an exception if the operation was largely successful
 e.g. adding multiple states (one state was empty string)

"""

if __name__ == "__main__":

    def test_create_state_machine():
        """ Test if state machine is being created """
        #sm1 = StateMachine.StateMachine()
        pass

    def test_add_state():
        """ Test if  """
        pass

    def test_add_duplicate_state():
        """ DuplicateStateException should occur if state has already been added  """
        pass

    def test_add_invalid_state():
        """ InvalidStateException should occur if state is blank or whitespace """
        pass

    def test_add_states():
        """ Valid states should be added.  First invalid state should cause
         InvalidStateException """
        pass

    def test_remove_existing_state():
        """ Remove if already existing. """
        pass

    def test_remove_non_existent_state():
        """ NonExistentStateException should occur (don't check for validity) """
        pass

    def test_remove_states():
        """ Remove all existing states until a NonExistentStateException is raised. """
        pass

    def test_remove_non_existent_states():
        """ NonExistentStateException should occur if any of the states is blank or
         whitespace.  None"""
        pass

    def test_set_initial_state():
        """ Should allow setting initial state """
        pass

    def test_set_invalid_initial_state():
        """ Should allow setting initial state """
        pass

    def test_set_duplicate_initial_state():
        """ Should raise exception if initial state already set """
        pass

    def test_add_one_final_state():
        """ Should allow setting a final state """
        pass

    def test_add_invalid_final_state():
        """ Should raise an InvalidStateException if state is blank or whitespace """
        pass

    def test_add_multiple_final_states():
        """ Should allow setting multiple final states """
        pass

    def test_add_multiple_invalid_final_states():
        """ Should add all valid states passed in the parameter before 
        raising an if InvalidStateException state is blank or whitespace """
        pass

    def test_valid_alphabet():
        pass

    def test_invalid_alphabet():
        pass



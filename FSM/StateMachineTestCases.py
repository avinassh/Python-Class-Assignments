from StateMachine import *
import StateMachine

"""
 Do we begin with simple cases or complex cases?  
 Are each of the test cases meant to be self contained?  Yes

 Do we throw an exception if the operation was largely successful
 e.g. adding multiple states (one state was empty string)

 Should all the test cases pass?  Ain't some test cases low priority?

"""

if __name__ == "__main__":

    def test_create_state_machine():
        """ Test if state machine is being created? """
        sm1 = StateMachine.StateMachine()

        # This is probably a bad way to do things.
        if hasattr(sm1, "initial_state") and hasattr(sm1, "final_states") and \
           hasattr(sm1, "transitions") and hasattr(sm1, "alphabet") and \
           hasattr(sm1, "states"):
            print "Passed: test_create_state_machine()"
        else:
            print "Failed: test_create_state_machine()"

    def test_add_state_1():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("  S1 ")
        if "S1" in sm1.states:
            print "Passed: test_add_state_1()"
        else:
            print "Failed: test_add_state_1()"

    def test_add_state_2():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        sm1.add_state(1)    # Passing a number instead of a string
        if "1" in sm1.states:
            print "Passed: test_add_state_2()"
        else:
            print "Failed: test_add_state_2()"

    def test_add_invalid_state_1():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state("   ")
            print "Failed: test_add_invalid_state_1()"
        except InvalidStateException:
            print "Passed: test_add_invalid_state_1()"
        
    def test_add_invalid_state_2():
        """ Test if a state can be added """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state(" !@#$  ")
            print "Failed: test_add_invalid_state_2()"
        except InvalidStateException:
            print "Passed: test_add_invalid_state_2()"

    def test_add_duplicate_state():
        """ DuplicateStateException should occur if state has already been added  """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_state("S2")
            sm1.add_state("S2")
            print "Failed: test_add_duplicate_state()"
        except DuplicateStateException:
            print "Passed: test_add_duplicate_state()"

    def test_add_states():
        """ Valid states should be added.  First invalid state should cause
         InvalidStateException """
        sm1 = StateMachine.StateMachine()
        sm1.add_states("S1", "S2", "S3")
        if "S1" in sm1.states and "S2" in sm1.states and "S3" in sm1.states:
            print "Passed: test_add_states()"
        else:
            print "Failed: test_add_states()"

    def test_add_invalid_states():
        """ InvalidStateException should occur if state is blank or whitespace """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.add_states("S1", "", "S3")
            print "Failed: test_add_invalid_states()"
        except InvalidStateException:
            if "S1" in sm1.states:
                print "Passed: test_add_invalid_states()"
            else:
                print "Failed: test_add_invalid_states()"

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

    def test_set_initial_state_0():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("0")
        sm1.set_initial_state("0")
        if sm1.initial_state == "0":
            print "Passed: test_set_initial_state_0()"
        else:
            print "Failed: test_set_initial_state_0()"

    def test_set_initial_state_1():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("State1")
        sm1.set_initial_state("State1")
        if sm1.initial_state == "State1":
            print "Passed: test_set_initial_state_1()"
        else:
            print "Failed: test_set_initial_state_1()"

    def test_set_initial_state_2():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("2")
        sm1.set_initial_state(" 2   ")
        if sm1.initial_state == "2":
            print "Passed: test_set_initial_state_2()"
        else:
            print "Failed: test_set_initial_state_2()"

    def test_set_initial_state_3():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        sm1.add_state("State1")
        sm1.set_initial_state(" State1   ")
        if sm1.initial_state == "State1":
            print "Passed: test_set_initial_state_3()"
        else:
            print "Failed: test_set_initial_state_3()"

    def test_set_invalid_initial_state_1():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.set_initial_state("   ")
            print "Failed: test_set_invalid_initial_state_1()"
        except InvalidStateException, e:
            print "Passed: test_set_invalid_initial_state_1()"

    def test_set_invalid_initial_state_2():
        """ Should allow setting initial state """
        sm1 = StateMachine.StateMachine()
        try:
            sm1.set_initial_state(" 1 2  ")
            print "Failed: test_set_invalid_initial_state_2()"
        except InvalidStateException, e:
            print "Passed: test_set_invalid_initial_state_2()"

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

    try:
        test_create_state_machine()
        test_add_state_1()
        test_add_state_2()
        test_add_invalid_state_1()
        test_add_invalid_state_2()
        test_add_duplicate_state()
        test_add_states()
        test_add_invalid_states()
        test_set_initial_state_0()
        test_set_initial_state_1()
        test_set_initial_state_2()
        #test_set_initial_state_2()
        test_set_invalid_initial_state_1()
        test_set_invalid_initial_state_2()

    except Exception as e:
        print e.message



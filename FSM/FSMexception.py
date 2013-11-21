from exceptions import Exception

class DuplicateStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class InvalidStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class NonExistentStateException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

#class (Exception):
#    def __init__(self, msg):
#        Exception.__init__(self, msg)
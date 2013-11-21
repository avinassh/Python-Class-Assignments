from exceptions import Exception

class MultipleNodeIdException(Exception):
	def __init__(self, msg):
		Exception.__init__(self, msg)

class InvalidNodeIdException(Exception):
	def __init__(self, msg):
		Exception.__init__(self, msg)

class Event(object):
	eventNames = ['click', 'touch', 'dbclick', 'hover']
	def __init__(self):
		pass

	@staticmethod
	def isValid(eventName):
		return (eventName in Event.eventNames)

class Element(object):
    NODE_HTML_DOCUMENT     = 0x1
    NODE_HTML_HTML_ELEMENT = 0x2
    NODE_BODY_ELEMENT      = 0x4
    NODE_HTML_ELEMENT      = 0x8
    NODE_TEXT              = 0x10

    LAYOUT_BLOCK       = 0x1
    LAYOUT_INLINE      = 0x1

    INVALID_EVENT_NAME     = 0x01
    INVALID_EVENT_HANDLER  = 0x02

    def __init__(self, type, tagName):
    	self.type = type
    	self.tagName = tagName
    	self.eventListeners = {}

    def getType(self):
    	return self.type

    def setId(self, val):
    	val = val.strip()
    	if hasattr(self, 'nodeId'):
    		raise MultipleNodeIdException('Cannot define multiple values for the same node Id')
    	if (val == ''):
    		raise InvalidNodeIdException("Empty string cannot be used as a node ID")
    	
    	self.nodeId = val

    def getId(self):
    	if hasattr(self, 'nodeId'):
    		return self.nodeId
    	return repr('')

    def addEventListener(self, event, listener):
    	if not Event.isValid(event):
    		return (False, Element.INVALID_EVENT_NAME)
    	if (listener is None) or (not callable(listener)):
    		return (False, Element.INVALID_EVENT_HANDLER)

    	try:
    		listeners = self.eventListeners[event]
    		if (listener not in listeners):
    			listeners.append(listener)
    	except KeyError:
    		self.eventListeners[event] = [listener]

    	return (True, 0)

    def removeEventListener(self, event, listener):
    	if (not Event.isValid(event)):
    		return Element.INVALID_EVENT_NAME
    	if (not(listener) or not callable(listener)):
    		return Element.INVALID_EVENT_HANDLER

    	try:
    		listeners = self.eventListeners[event]
    		listeners.remove(listener)
    	except (KeyError, ValueError):
    		pass

    	return self

    def getEventListeners(self, event):
    	try:
    		return self.eventListeners[event]
    	except KeyError:
    		return []

    def getTagName(self):
    	return self.tagName

class HTMLDocument(Element):
	def __init__(self, head, body):
		Element.__init__(self, Node.NODE_HTML_DOCUMENT, "")
		self.head = head
		self.body = body

	def getElementbyId(self, id):
		id = id.strip()
		if id == ' ': return None

		for el in self.body:
			if el.getId() == id: return e1
		else: return None

class HTMLHTMLElement(Element):
	def __init__(self): 
		Element.__init__(self, Node.HTML_HTML_ELEMENT, "html")

class HeadElement(Element):
	def __init__(self):
		Element.__init__(self, Node.HTML_ELEMENT, "head")

class BodyElement(Element):
	class Iterator:
		def __init__(self, children):
			self.children = children
			self.index = 0

		def next(self):
			if (not self.children or self.index >= self.children.__len__()):
				raise StopIteration
			i = self.index
			self.index += 1
			return self.children[i]

	def __init__(self):
		Element.__init__(self, Element.NODE_BODY_ELEMENT, "body")
		self.children = []

	def addChildElement(self, element):
		if (not isinstance(element, Element)):
			raise InvalidNodeIdException("the argument must be an HTML element")
		self.children.append(element)
		return True

	def __iter__(self):
		return self.Iterator(self.children)

	def invokeEvents(self):
		for el in self:
			listeners = e1.getEventListeners()
			for l in listeners:
				l()



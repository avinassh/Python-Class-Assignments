from node import *

if __name__ =='__main__':
	def testEmptyNodeId():
		try:
			el = Element(Element.NODE_HTML_ELEMENT, "div")
			assert (el.getId() == repr(''))
			print 'pass: testEmptyNodeId()'
		except AssertionError:
			print 'fail: testEmptyNodeId()'

	def testValidNodeId():
		try:
			el = Element(Element.NODE_HTML_ELEMENT, "div")
			el.setId(' idQuizCard  ' )
			assert (el.getId() == 'idQuizCard')
			print 'pass: testValidNodeId()'
		except AssertionError:
			print 'fail: testValidNodeId()'

	def testMultipleNodeIdPerNode():
		try:
			el = Element(Element.NODE_HTML_ELEMENT, "div")
			el.setId('idQuizCard')
			el.setId('idQuizCard')
			print 'fail: testMultipleNodeIdPerNode()'
		except MultipleNodeIdException:
			print 'pass: testMultipleNodeIdPerNode()'

	def	testInvalidNodeId():
		try:
			el = Element(Element.NODE_HTML_ELEMENT, "div")
			el.setId('   ')
			print 'fail: testInvalidNodeId()'
		except InvalidNodeIdException:
			print 'pass: testInvalidNodeId()'

	def testAddEventListener():
		def clickHandler():
			print 'click handler!'

		try:
			el = Element(Element.NODE_HTML_ELEMENT, "div")
			el.setId('quizCard')
			(result, reason) = el.addEventListener('click', clickHandler)
			if (result == True):
				print 'pass: testAddEventListener()'
			else:
				print 'fail: testAddEventListener()', reason
		except Exception as e:
			print 'fail: testAddEventListener()', e.message

	def testAddDuplicateEventListener():
		def sayHello():
			print 'click handler: Hello!'

		def greetGuido():
			print 'click handler: Hello Mr. Guido!'

		def ignoreClick():
			pass

		el = Element(Element.NODE_HTML_ELEMENT, "div")
		el.setId('quizCard')

		(result, reason) = el.addEventListener('click', sayHello)
	 	(result, reason) = el.addEventListener('click', greetGuido)
		(result, reason) = el.addEventListener('click', ignoreClick)
		(result, reason) = el.addEventListener('click', sayHello)

		if result is True:
			print 'pass: testAddDuplicateEventListener()'
		elif reason == Element.INVALID_EVENT_NAME:
			print 'fail: testAddDuplicateEventListener() -- invalid event name'
		elif reason == Element.INVALID_EVENT_HANDLER:
			print "fail: testAddDuplicateEventListener() -- invalid event handler"

	def testIterateBodyElements():
		body = BodyElement()
		divCardWrapper = Element(Element.NODE_HTML_ELEMENT, "div")
		divCardWrapper.setId("divCardWrapper")
		res = body.addChildElement(divCardWrapper)
		divCard = Element(Element.NODE_HTML_ELEMENT, "div")
		divCard.setId("divCard")
		res = body.addChildElement(divCard)
		for el in body:
			print el.getTagName(), ': ', el.getId()
		try:
			#res = body.addChildElement('str')
			if (res == True):
				print 'pass: testIterateBodyElements()'
		except InvalidNodeIdException as e:
			print 'fail: testIterateBodyElements() -- ', e.message

	try:
		testEmptyNodeId()
		testValidNodeId()
		testMultipleNodeIdPerNode()
		testInvalidNodeId()
		testAddEventListener()
		testAddDuplicateEventListener()

		testIterateBodyElements()
	except Exception as e:
		print e.message

import unittest
from main import do_stuff

class TestMain(unittest.TestCase):

	def setUp(self):
		print('about to test a function')

	def test_do_stuff(self):
		'''First test'''
		test_param = 10
		result = do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'asdff'
		result = do_stuff(test_param)
		self.assertTrue(isinstance(result,ValueError))

	def test_do_stuff3(self):
		test_param = None
		result = do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')
	
	def test_do_stuff4(self):
		test_param = ''
		result = do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')
	
	# Usually for database
	def tearDown(self):
		print('clean up')

# Run the test not the file itself
if __name__ == '__main__':
	unittest.main()


# python -m unittest -v(verbose)

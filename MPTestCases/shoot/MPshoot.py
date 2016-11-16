import unittest

class MPshoot(unittest.TestCase):
	def setUp(self):
		pass;

	def tearDown(self):
		pass;
	
	def test_shoot1(self):
		print "test_shoot1"

	def test_shoot2(self):
		print "test_shoot2"

	def test_shoot3(self):
		print "test_shoot3"

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPshoot('test_shoot1'))  
	suite.addTest(MPshoot('test_shoot2'))  
	suite.addTest(MPshoot('test_shoot3')) 

	runner = unittest.TextTestRunner()  
	runner.run(suite)


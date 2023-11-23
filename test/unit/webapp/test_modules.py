import unittest

from app import restore_thelines
# all entries within <> are placeholders

class TestClass(unittest.TestCase):
	def test_lines(self):
		self.assertTrue(restore_thelines("Hello this is neeha"))

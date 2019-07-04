import unittest
from app.models import Pitch, User

class PitchTest(unittest.TestCase):
    def setUp(self):
        '''
        Method that creates an instance of  the Pitch class
        '''
        self.new_pitch = Pitch('Example Title', 'This is a sample pitch', 'highlights')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

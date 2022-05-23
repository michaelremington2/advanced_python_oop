import unittest
import os
from make_diary import Diary

class Test_Make_Diary(unittest.TestCase):
    '''
    Welcome to the Journals testing suite! Pretty comfy huh? This script is what is known as unit testing and it is super important if you want to develope actual 
    software for people! There are a couple of things you should know.
    1. This is from the python package unittest. Always import the package or class you want to test!
    2. In the test object, make sure you include: unittest.TestCase, this is how python knows its a test suite.
    3. the setUp method is a special method automatically run by python. This is space for you to build the basic infustructure your tests will need to be able to run.
    4. Any function with the word 'test' in front of it will automatically be run. These are what will give you the output summary when you run this script.
    5. The tearDown method is a special method that is the oppisite of the setUp method. This is space where you can delete files you created to run tests or other things
    6. in the if__name__==main part, make sure you run unittest.main(). This allows python to know you are doing unit testing and which gives it all these extra functionalities.
    7. You're a good software developer for making unit tests your parents will be very proud of you!
    '''
    def setUp(self):
        '''This is a setup method! This is run outside of your tests to set up your tests'''
        self.test_journal = Diary(diary_name='test_journal')

    def test_data_population(self):
        '''This test checks if the journal csv file is made appropriately.'''
        current_fp = os.getcwd()
        my_test_journal = os.path.join(current_fp,"Data/test_journal.csv")
        if os.path.exists(my_test_journal):
            pass 
        else:
            assert False

    def test_array_shape(self):
        '''This function will check if the program is actually adding entries to the csv. I ran it twice here plue the header means the length of the data should be 3.'''
        self.test_journal.add_diary_entry(diary_text="robot dream")
        self.test_journal.add_diary_entry(diary_text="robot dream # 2")
        test_data = self.test_journal.open_diary()
        test_data_size = len(test_data)
        self.assertEqual( test_data_size, 3)

    def tearDown(self):
        '''Goodbye test diary csv.'''
        self.test_journal.delete_diary()



if __name__ == '__main__':
    unittest.main()
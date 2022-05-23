import time
import os
import csv
from datetime import datetime


class Diary(object):
    """  
    This is a small python app that allows the user to make their own dream journal. The purpose of this app is
    to teach intermediate python users how to do object oriented programming and other concepts such as pep 8 documentation,
    Args:
        diary_name -- the name of the diary you would like to use. Preferably just your name!
        set_file_directory -- this is optional, if none then it will use the current file directory the user is running this in.
    Attributes:
        _data_dir -- Directory for the data folder that contains journal csvs
        _diary_dir -- file path for the journal of interest.
        """
    def __init__(self,diary_name, set_file_directory=None):
        # This function initializes your whole class and gets it started with everything it will need for basic functionality.
        self.diary_name = diary_name
        if set_file_directory:
            self._current_directory = _set_file_directory
        else:
            self._current_directory = os.getcwd()
        self.initialize_diary()


    def initialize_diary(self):
        '''Set up appropriate directories for the data path and journal file and then make them if they do not exist.'''
        self._data_dir = os.path.join(self._current_directory,'data')
        self._diary_dir = os.path.join(self._data_dir,(self.diary_name + ".csv"))
        self.make_diary_db()
        self.make_diary()   

    def make_diary_db(self):
        '''Checks if there is already a diary database folder in this current file path. If there isn't then this function makes one.'''
        if os.path.exists(self._data_dir):
            pass
        else:
            os.mkdir(self._data_dir)

    def make_diary(self):
        '''Checks if there is already a diary file with this diary name. If there isn't then this function makes one.'''
        if os.path.exists(self._diary_dir):
            pass
        else:
            with open(self._diary_dir, "w", newline='\n') as my_dream_diary:
                self.append_to_diary(date='date', journal_entry='journal_entry')

    def append_to_diary(self, date, journal_entry):
        '''Adds rows (journal entries) to our csv.'''
        with open(self._diary_dir, 'a') as diary:
            writer = csv.writer(diary)
            row = [date, journal_entry]
            writer.writerow(row)

    def add_diary_entry(self, diary_text=None, date=None):
        '''Interacts with the user to obtain the appropriate journal entry.'''
        if diary_text is None:
            print(f'What would you like to insert into the journal {self.diary_name}?')
            diary_text = input()
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')
        self.append_to_diary(date=date, journal_entry=diary_text)

    def open_diary(self):
        """Opens the csv file that contains the diary information and reads entries into a list."""
        with open(self._diary_dir, "r") as my_dream_diary:
            diary_data = list(csv.reader(my_dream_diary))
        return diary_data

    def read_diary(self):
        ''' Makes a list of diary entries then prints them in a formated manner.'''
        diary_data = self.open_diary()
        for key, row in enumerate(diary_data):
            if key!=0:
                print(f"Date: {row[0]}")
                print(f"{row[1]} \n")

    def delete_diary(self):
        '''Deletes the journal csv.'''
        os.remove(self._diary_dir)



class Dream_Diary(Diary):
    '''
    Inheritance is a super (forshadowing a pun here) important concept in object oriented programing! Instead of object in parenthesis we
    call the object we are inheriating methods and attributes from which is the Diary class. We then call the super method to load these into our new class without manually
    having to do it.

    Args:
        diary_name -- the name of the diary you would like to use. Preferably just your name!
        set_file_directory -- this is optional, if none then it will use the current file directory the user is running this in.
    Attributes:
        _data_dir -- Directory for the data folder that contains journal csvs
        _diary_dir -- file path for the journal of interest.'''
    def __init__(self,diary_name, set_file_directory=None):
        super().__init__(diary_name,set_file_directory)
        self.initialize_diary()

    def make_diary(self):
        '''Checks if there is already a diary file with this diary name. If there isn't then this function makes one.'''
        if os.path.exists(self._diary_dir):
            pass
        else:
            with open(self._diary_dir, "w", newline='\n') as my_dream_diary:
                self.append_to_diary(date='date', journal_entry='journal_entry', sleep_quality='sleep_quality', nightmare='nightmare')

    def append_to_diary(self, date, journal_entry, sleep_quality, nightmare):
        '''Dream journals are like powerful day journals because they care about how you sleep and whether you not you had a nighmare'''
        with open(self._diary_dir, 'a') as diary:
            writer = csv.writer(diary)
            row = [date, journal_entry,sleep_quality,nightmare]
            writer.writerow(row)

    def add_diary_entry(self, diary_text=None, date=None,sleep_quality=None,nightmare=None):
        '''Interacts with the user to obtain the appropriate journal entry.'''
        if diary_text is None:
            print(f'What would you like to insert into the journal {self.diary_name}?')
            diary_text = input()
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')
        if sleep_quality is None:
            sleep_quality = self.sleep_quality_input(sleep_quality)
        if nightmare is None:
            nightmare=self.nightmare_input()
        self.append_to_diary(date=date, journal_entry=diary_text, sleep_quality=sleep_quality,nightmare=nightmare)

    def sleep_quality_input(self,sleep_quality):
        '''Here we check if the user is giving us an appropriate answer between 1-10. If not try again! Notice the try, and except method.'''
        while sleep_quality is None:
            print("How did you sleep on a scale from 1-10?: ")
            user_value = int(input())
            try:
                sleep_quality = int(self.sleep_quality_val_check(sleep_quality=user_value))
            except ValueError:
                print('Please enter an integer from 1-10')
                continue
            else:
                break
        return sleep_quality

    def sleep_quality_val_check(self,sleep_quality):
        '''Here we are literally checking if the value is between 1-10. If it is not its a value error :('''
        if 1 > sleep_quality > 10:
            raise ValueError
        return sleep_quality


    def nightmare_input(self):
        while True:
            try:
                nightmare = bool(input("Was your dream a nightmare? (True or False): "))
            except ValueError:
                print('Please enter True or False with a capital letter.')
                continue
            else:
                break
        return nightmare

    def open_diary(self):
        """Opens the csv file that contains the diary Information so entries can be added or read in."""
        diary_data = []
        with open(self._diary_dir, "r") as my_dream_diary:
            reader = csv.reader(my_dream_diary)
            for row in reader:
                diary_data.append(row)
        return diary_data        

    def read_diary(self):
        ''' Makes a list of diary entries then prints them in a formated manner.'''
        diary_data = self.open_diary()
        for key, row in enumerate(diary_data):
            if key!=0:
                print(f"Date: {row[0]}, sleep quality: {str(row[2])}, nightmare: {str(row[3])}")
                print(f"{row[1]} \n")


if __name__=='__main__':
    # michael_diary = Diary(diary_name='mikes_normal_journal')
    michael_diary = Dream_Diary(diary_name='mikes_dream_journal')
    #michael_diary.add_diary_entry()
    michael_diary.read_diary()


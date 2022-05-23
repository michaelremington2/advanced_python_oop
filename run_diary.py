from make_diary import Diary, Dream_Diary


# Hank Journal Entries
he1 = "Bark Bark Bark"
he2 = "squirrels are jerks"
he3 = "squirrels chased me for hours :("

def populate_hanks_dream_diary(*args):
    hank_diary = Dream_Diary(diary_name='hank_dream_journal')
    for dream in args:
        hank_diary.add_diary_entry(diary_text=dream, sleep_quality=7,nightmare=False)
    hank_diary.read_diary()





if __name__=='__main__':
    # michael_diary = Diary(diary_name='mikes_normal_journal')
    #michael_diary = Dream_Diary(diary_name='mikes_dream_journal')
    #michael_diary.add_diary_entry()
    #michael_diary.read_diary()
    #populate_hanks_dream_diary(he1, he2, he3)




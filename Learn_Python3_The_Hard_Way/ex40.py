class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(['生日快乐',
                   '换行了',
                   '又换行了'])

bulls_on_parade = Song(['你瞅啥','瞅你咋地',
                        '再瞅一个试试'])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

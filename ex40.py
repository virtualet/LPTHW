class Song(object):

    def __init__(self, lyrics):
        self.varlyrics = lyrics

    def sing_me_a_song(self):
        for line in self.varlyrics:
            print line




happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "so I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


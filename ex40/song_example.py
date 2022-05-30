class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print("")


popular_song = Song(lyrics=["La la",
                            "la la",
                            "You were the popular one, the popular chick",
                            "It is what it is, now I'm popular-ish"])


the_foundation_of_decay = Song(lyrics=[
    "See the man who stands upon the hill",
    "He dreams of all the battles won",
    "But fate had left its scars upon his face",
    "With all the damage they had done"])

popular_song.sing_me_a_song()
the_foundation_of_decay.sing_me_a_song()

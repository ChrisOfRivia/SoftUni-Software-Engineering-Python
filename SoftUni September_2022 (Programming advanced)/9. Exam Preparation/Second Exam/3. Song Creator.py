def add_songs(*args):
    dict_songs = {}
    for inputs in args:
        song_title, lyrics = inputs
        if song_title not in dict_songs:
            dict_songs[song_title] = []
        if lyrics:
            for every_lyric in lyrics:
                dict_songs[song_title].append(every_lyric)

    result = ''
    for titles, lyrics_song in dict_songs.items():
        result += f"- {titles}\n"
        for every_lyric in lyrics_song:
            result += f"{every_lyric}\n"

    return result

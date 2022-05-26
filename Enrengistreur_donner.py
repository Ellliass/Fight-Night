from user_data import scoredata


def save(game):

    dict1 = game.score
    file1 = open("user_data/scoredata.py", "w")
    file1.write("%s = %s\n" % ("dict1", dict1))
    file1.close()

    f = open('user_data/scoredata.py', 'r')
    if f.mode == 'r':
        contents = f.read()

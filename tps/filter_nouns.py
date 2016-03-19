"""
It is used for judge a word is some type of noun or not.
Now It can be some function:
is_time(word):

"""
from nltk.corpus import wordnet as wn


def is_time(word):
    """
    judge a word is about time or not
    :param word:
    :return:
    """
    time_syns_words = ["time_period.n.01", "series.n.03", "time.n.05", "clock_time.n.01", "time_unit.n.01"]
    return is_sub(word,time_syns_words)


def is_sub(word, lists):
    word = wn.morphy(word.lower(), wn.NOUN)
    p_syns = []
    for p_syn_item in lists:
        p_syns.append(wn.synset(p_syn_item))
    if not word:
        return False
    syns = wn.synsets(word,wn.NOUN)

    # print "word is ", word
    flag = False
    for syn in syns:
        for p_syn in p_syns:
            for syn_path in syn.hypernym_paths():
                if p_syn in syn_path:
                    flag = True
    return flag


def is_relation(word):
    """
    to judge a word is about relation or not
    :param word:
    :return:
    """
    relation_syns_words = ["relative.n.01","friend.n.01"]
    return is_sub(word,relation_syns_words)

if __name__ == "__main__":
    print "today is time ? " + str(is_time("today"))
    print "happy is time ? " + str(is_time("happy"))
    print "friend is relation? " + str(is_relation("friend"))
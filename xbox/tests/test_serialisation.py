import pickle


def test_pickle_clip(clip):
    pickled = pickle.dumps(clip)
    restored = pickle.loads(pickled)
    assert id(clip) != id(restored)
    for key, value in clip.__dict__.iteritems():
        assert restored.__dict__[key] == value


def test_pickle_gamer_profile(gamerprofile):
    pickled = pickle.dumps(gamerprofile)
    restored = pickle.loads(pickled)
    assert id(gamerprofile) != id(restored)
    for key, value in gamerprofile.__dict__.iteritems():
        assert restored.__dict__[key] == value
"""
-- Created by: Ashok Kumar Pant
-- Created on: 12/14/21
"""
from langdetect import DetectorFactory

PROFILES_DIRECTORY  = "./profiles"
_factory = None


def init_factory():
    global _factory
    if _factory is None:
        _factory = DetectorFactory()
        _factory.load_profile(PROFILES_DIRECTORY)
        print(_factory.get_lang_list())
        _factory.seed = 0


def detect(text):
    init_factory()
    detector = _factory.create()
    detector.append(text)
    return detector.detect()


def detect_langs(text):
    init_factory()
    detector = _factory.create()
    detector.append(text)
    return detector.get_probabilities()


if __name__ == '__main__':
    langs = detect_langs("this is nepali language")
    print(langs)
    langs = detect_langs("ptrkaar")
    print(langs)
    langs = detect_langs("k xa")
    print(langs)
    langs = detect_langs("नेपाली")
    print(langs)
    langs = detect_langs("पहिलो")
    print(langs)
    langs = detect_langs("dosro")
    print(langs)

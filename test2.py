from gensim import models

ko_model = models.fasttext.load_facebook_model("DATA/cc.ko.300.bin")


for w, sim in ko_model.similar_by_word("파이썬", 10):
    print(f"{w}: {sim}")

import pickle

with open("set.pick", "rb") as fic:
    s2=pickle.load(fic)

print(s2, type(s2))

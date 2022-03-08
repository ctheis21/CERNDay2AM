import pickle

s1={34,56,78}

print(s1)
with open("set.pick", "wb") as fic:
    pickle.dump(s1, fic)
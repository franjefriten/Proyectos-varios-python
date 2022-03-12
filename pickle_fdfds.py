try:
    import cPickle as pickle
except:
    import pickle

file = open("Seriaización\data.txt", "w")
animales = ["girafa", "camello", "primate"]

pickle.dump(animales, file)
pickle.dump()
file.close()
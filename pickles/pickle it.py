#pickle it
#preserving data structures
#Sabastian Taton

import pickle
import shelve
##
##print("Pickling lists.")
##variety = ["dill", "sweet","hot"]
##shape = ["whole","spear","chip"]
##brand = ["Vlassic","Kosher","Heinz","Claussen"]
##
##f = open("pickles1.dat", "wb")
##pickle.dump(variety, f)
##pickle.dump(shape, f)
##pickle.dump(brand, f)
##f.close()

##print("unpickling lists.")
##
##f = open("pickles1.dat", "rb")
##variety = pickle.load(f)
##shape = pickle.load(f)
##brand = pickle.load(f)
##print(variety)
##print(shape)
##print(brand)
##f.close()

print ("\nShelving lists")
s = shelve.open("pickles2.dat")
s["variety"] = ["dill", "sweet","hot"]
s['shape'] = ["whole","spear","chip"]
s['brand'] = ["Vlassic","Kosher","Heinz","Claussen"]
s.sync()

print("Retrieveing from shelf")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])

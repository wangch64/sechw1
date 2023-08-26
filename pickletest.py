# serialization
import pickle
my_dict = {
    'S': "Scissors",
    'P': "Paper",
    'T': "Stone",
}
with open('test.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
# Pickle Load
with open('test.pickle', 'rb') as f:
    rec_dict = pickle.load(f)
print(rec_dict)

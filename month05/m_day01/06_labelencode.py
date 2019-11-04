import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford',
    'audi'])

le = sp.LabelEncoder()
print(le)
result = le.fit_transform(raw_samples)
print(result)

test = [0,0,1,2,3]
print(le.inverse_transform(test))
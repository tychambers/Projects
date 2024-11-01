# splits data on the graph
# margin free space between lines
# Kernels add a third dimension to data
# soft margin

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

data = load_breast_cancer()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# rbf, polynomial, linear(fastest)
clf = SVC(kernel='linear', C=3)
clf.fit(x_train, y_train)

clf2 = KNeighborsClassifier(n_neighbors=3)
clf2.fit(x_train, y_train)

test = np.array(data.data)[19]

test2 = clf.predict([test])
print(test2)


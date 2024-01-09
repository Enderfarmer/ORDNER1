from sklearn import tree
from numpy import array
X = array([[9, 5, 6, 'Informatik']
           [1, 8, 1, 'Linguistik']
           [5, 7, 9, 'Kunst']])
Tree = tree.DecisionTreeClassifier().fit(X[:,:-1],X[:,-1])
print(Tree.predict([[5,9,2]]))
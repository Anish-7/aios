import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn import svm
from sklearn.metrics import f1_score,accuracy_score ,confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from imblearn.combine import SMOTETomek 
import joblib

state_dat=pd.read_csv("state.csv")
state_dat=state_dat.drop(columns=['cpuavg'])


x=state_dat.iloc[:,2:5]
y=state_dat.iloc[:,-1]



smk= SMOTETomek(random_state=42)
xres,yres=smk.fit_resample(x,y)

# print(yres.value_counts())
X_train, X_test, y_train, y_test =train_test_split(xres, yres,train_size=0.60, test_size=0.40, random_state=101)

#svm
# rbf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# rbf_pred = rbf.predict(X_test)

#naive bayes
# from sklearn.naive_bayes import GaussianNB
# gnb = GaussianNB().fit(X_train, y_train)
# gnb_predictions = gnb.predict(X_test)

# cm = confusion_matrix(y_test, gnb_predictions)
# accuracy = gnb.score(X_test, y_test)
# print(accuracy)

#descision tree
from sklearn.tree import DecisionTreeClassifier
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
accuracy = dtree_model.score(X_test, y_test)

# print(accuracy)
filename = "state.joblib"
joblib.dump(dtree_model, filename)

# rbf_accuracy = accuracy_score(y_test, rbf_pred)
# print(rbf_accuracy)

y_test=list(y_test)
for i in range(len(y_test)):
    print(f'{y_test[i]},{dtree_predictions[i]}')
    

# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12pbmOE2RYnfnLKpZnTK2OpzN82Vy339a
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Método normal

# Fazendo o import
dados = pd.read_csv("./pima_indians.csv")

# Dividindo a base de dados entre 'x' e 'y'
x = dados[['pregnant', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'diabetes', 'age']]
y = dados['test']

# Preparando as partes de treinamento e teste
xtreino, xteste, ytreino, yteste = train_test_split(x, y, random_state=1)

# Iniciando o modelo SVM
svm = SVC()
svm = svm.fit(xtreino, ytreino)
yprevisao = svm.predict(xteste)

svm.support_vectors_
svm.n_support_

# Avaliando a acurácia
metrics.accuracy_score(yteste, yprevisao)

X = dados.values[:100, 1:3]
y = dados.values[:100, 8].astype(np.integer)

# Treinando o modelo SVM
svm = SVC(kernel='rbf')
svm.fit(X, y)

plot_decision_regions(X, y, clf=svm)

# Testando outro modelo linear
svm = LinearSVC()
svm.fit(X, y)

# Mostrando o gráfico
plot_decision_regions(X, y, clf=svm)
plt.show()

# Método scaling

# Fazendo o import
dados = pd.read_csv("./pima_indians.csv")

# Dividindo a base de dados entre 'x' e 'y'
x = dados[['pregnant', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'diabetes', 'age']]
y = dados['test']

# Preparando as partes de treinamento e teste
xtreino, xteste, ytreino, yteste = train_test_split(x, y, random_state=1)

xtreino.min()

# Iniciando o range
xtreino_range = xtreino.max() - xtreino.min()

xtreino_padroniz = (xtreino - xtreino.min()) / xtreino_range

# Realizando o scaling
ytreino_range = ytreino.max() - ytreino.min()
ytreino_padroniz = (ytreino - ytreino.min()) / ytreino_range

xteste_range = xteste.max() - xteste.min()
xteste_padroniz = (xteste - xteste.min()) / xteste_range

# Gerando o modelo com dados padronizados
X = xtreino_padroniz.values[:, 1:3]
y = ytreino.values.astype(np.integer)

# Criando o modelo SVM
svm = SVC(kernel='linear')
svm.fit(X, y)

 # Preparando o gráfico
plot_decision_regions(X, y, clf=svm, legend=2)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.title('SVM com Kernel Linear - Tipos de Flores')

# Aplicando o modelo com dados padronizados
svm = SVC()
svm = svm.fit(xtreino_padroniz, ytreino)

yprevisao = svm.predict(xteste_padroniz)
yprevisao[0:5]

# Avaliando o modelo
cm = np.array(confusion_matrix(yteste,yprevisao, labels=[1,0]))
avaliacao = pd.DataFrame(cm,index=['tem diabetes', 'está saudável'], columns=['previsto com diabetes', 'previsto como saudável'])

# Avaliando a acurácia
metrics.accuracy_score(yteste, yprevisao)
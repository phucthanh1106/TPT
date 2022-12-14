# -*- coding: utf-8 -*-
"""text_to_speech-detectlanguage.ipynb 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Eo6oH9PRrh9vScdZ1bO1aN58fWJ0SZN
"""

from google.colab import drive
drive.mount('/content/drive', force_remount = True)
!cp drive/MyDrive/TFE/Language_Detection.csv .

pip install SpeechRecognition

import os

pip install playsound

pip install wikipedia

pip install selenium

pip install webdriver-manager

pip install gTTs

import time
import sys
import ctypes
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS

pip install langdetect

pip install textblob

pip install panda

import codecs

codecs.register_error('strict', codecs.lookup_error('surrogateescape'))

import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")
# Tải tập dữ liệu
data = pd.read_csv("Language_Detection.csv")
# Đếm số lượng giá trị cho mỗi ngôn ngữ
print(data['Language'].value_counts())
# Tách các biến độc lập và phụ thuộc
X = data["Text"]
y = data["Language"]
# Chuyển đổi các biến đã phân loại thành số
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
# Tạo danh sách để nối văn bản đã xử lý tách trước đó
data_list = []
# Vòng lặp xử lý tất cả các văn bản
for text in X:
    # Loại bỏ các ký hiệu và số
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', str(text))
    text = re.sub(r'[[]]', ' ', str(text))
    # Chuyển văn bản thành chữ thường, không in hoa
    text = text.lower()
    # Thêm văn bản đã xử lý vào data list đã tạo trước đó
    data_list.append(text)
# Tạo túi từ bằng cách sử dụng countvectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(data_list).toarray()
#Thử nghiệm training dữ liệu test, tập test là 1/5 dữ liệu đưa vào, còn lại là training
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
# Tạo mô hình và dự đoán
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train, y_train)
# Dự đoán tập test
y_pred = model.predict(x_test)
# Đánh giá mô hình đã tạo
from sklearn.metrics import accuracy_score, confusion_matrix
ac = accuracy_score(y_test, y_pred)
print(ac)
cm = confusion_matrix(y_test, y_pred)

# function dự đoán ngôn ngữ
def predict(text):
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    print("The language is in",lang[0])
# English
predict("Analytics Vidhya provides a community based knowledge portal for Analytics and Data Science professionals")
# French
predict("Analytics Vidhya fournit un portail de connaissances basé sur la communauté pour les professionnels de l'analyse et de la science des données")
# Arabic
predict("توفر Analytics Vidhya بوابة معرفية قائمة على المجتمع لمحترفي التحليلات وعلوم البيانات")
# Spanish
predict("Analytics Vidhya proporciona un portal de conocimiento basado en la comunidad para profesionales de Analytics y Data Science.")
# Malayalam
predict("അനലിറ്റിക്സ്, ഡാറ്റാ സയൻസ് പ്രൊഫഷണലുകൾക്കായി കമ്മ്യൂണിറ്റി അധിഷ്ഠിത വിജ്ഞാന പോർട്ടൽ അനലിറ്റിക്സ് വിദ്യ നൽകുന്നു")
# Russian
predict("Analytics Vidhya - это портал знаний на базе сообщества для профессионалов в области аналитики и данных.")
#Korea
predict("나는 오늘 너무 재미 있었어요!")
#Chinese
predict("这辈子总有美好的事情在等着我们，只是让您感到积极，一切都很棒")
#Japanese
predict("彼は人の話を聞かないきらいがある")

le.classes_

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import Model
from tensorflow import keras

# Tính confusion matrix
matrix = confusion_matrix(y_test, y_pred)
# print(matrix)

y_train

len(x_train)

print(np.mean(y_test==y_pred))

import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes, ax,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
   
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.xlabel('True label')
    plt.ylabel('Predicted label')

from sklearn import metrics
import itertools

score = metrics.accuracy_score(y_test, y_pred)
print("accuracy:   %0.3f" % score)
cm = metrics.confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(cm, classes =['Arabic', 'Chinese', 'Danish', 'Dutch', 'English', 'French',
       'German', 'Greek', 'Hindi', 'Italian', 'Japanese', 'Kannada',
       'Korean', 'Malayalam', 'Portugeese', 'Russian', 'Spanish',
       'Sweedish', 'Tamil', 'Turkish'], ax = ax)

y_pred1 = model.predict(x_train)

from sklearn import metrics
import itertools

score = metrics.accuracy_score(y_train, y_pred1)
print("accuracy:   %0.3f" % score)
cm = metrics.confusion_matrix(y_train, y_pred1)
fig, ax = plt.subplots(figsize=(10, 10))
plot_confusion_matrix(cm, classes =['Arabic', 'Chinese', 'Danish', 'Dutch', 'English', 'French',
       'German', 'Greek', 'Hindi', 'Italian', 'Japanese', 'Kannada',
       'Korean', 'Malayalam', 'Portugeese', 'Russian', 'Spanish',
       'Sweedish', 'Tamil', 'Turkish'], ax = ax)
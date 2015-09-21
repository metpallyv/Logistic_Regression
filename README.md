# Logistic_Regression
Goal of this project is to implement Logistic  Regression without using Machine Learning Libraries

In this project, I implemented logistic regression using gradient ascent algorithm.

I implemented on three datasets for binary classification:

• Spambase: the objective is to classify email messages as being spam or not. To this end the
dataset uses fifty seven text based features to represent each email message. There are about
4600 instances. Here are the definitions for the features:

The last column of 'spambase.data' denotes whether the e-mail was considered spam (1) or not (0), i.e. unsolicited commercial e-mail. Most of the attributes indicate whether a particular word or character was frequently occuring in the e-mail. The run-length attributes (55-57) measure the length of sequences of consecutive capital letters. For the statistical measures of each attribute, see the end of this file. Here are the definitions of the attributes: 

1. 48 continuous real [0,100] attributes of type word_freq_WORD 
= percentage of words in the e-mail that match WORD, i.e. 100 * (number of times the WORD appears in the e-mail) / total number of words in e-mail. A "word" in this case is any string of alphanumeric characters bounded by non-alphanumeric characters or end-of-string. 

2. 6 continuous real [0,100] attributes of type char_freq_CHAR] 
= percentage of characters in the e-mail that match CHAR, i.e. 100 * (number of CHAR occurences) / total characters in e-mail 
3. 1 continuous real [1,...] attribute of type capital_run_length_average 
= average length of uninterrupted sequences of capital letters 

4. 1 continuous integer [1,...] attribute of type capital_run_length_longest 
= length of longest uninterrupted sequence of capital letters 

5. 1 continuous integer [1,...] attribute of type capital_run_length_total 
= sum of length of uninterrupted sequences of capital letters 
= total number of capital letters in the e-mail 

6. 1 nominal {0,1} class attribute of type spam 
= denotes whether the e-mail was considered spam (1) or not (0), i.e. unsolicited commercial e-mail. 

• Breast Cancer: this dataset is aimed at developing classifiers that can distinguish between
malignant and benign tumors in breast cancer. There are thirty real valued features and 569
instances. Here are the definitons of the features: 

1. Class: no-recurrence-events, recurrence-events 
2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99. 
3. menopause: lt40, ge40, premeno. 
4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59. 
5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26, 27-29, 30-32, 33-35, 36-39. 
6. node-caps: yes, no. 
7. deg-malig: 1, 2, 3. 
8. breast: left, right. 
9. breast-quad: left-up, left-low, right-up,	right-low, central. 
10. irradiat:	yes, no.

• Pima Indian Diabetes: The task is to predict whether a person has diabetes or not based
on eight features. The data was recorded from females of pima indian heritage. It has a total
of 768 instances.

Here are the definitions of the features:

Diabetes files consist of four fields per record. Each field is separated by a tab and each record is separated by a newline. File Names and format: 
1.  Date in MM-DD-YYYY format 
2.  Time in XX:YY format 
3. Code 
4. Value

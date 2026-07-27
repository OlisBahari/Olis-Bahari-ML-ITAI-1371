Filename......: L08_OlisBahari_ITAI1371

Language......: Python

Tools.........: Visual Studio Code (VSC)
               : Google Colab
               
Class.........: ITAI 1371 Introduction to Machine Learning

Semester......: Summer 2026

Class Type....: Online

Instructor....: Sitaram Ayyagari

Student.......: Olis Bahari

Version.......: V1.0

Purpose.......: Demonstrate bias-variance tradeoff using polynomial regression
                 and learning curves

### **[Q1]** 
The degree 1 model is underfitting because it is too simple to capture the curved sine-wave pattern in the data.

The degree 4 model is a good fit because it follows the overall trend without fitting random noise. 

The degree 15 model is overfitting because it is highly complex and fits noisy data points rather than the true underlying pattern.


### **[Q2]**
For the underfitting model, both the training and cross-validation scores are relatively low and close together. 

This means the model is too simple to learn the relationship in the data. 

It has high bias and performs poorly on both the training and validation data.


### **[Q3]**
For the overfitting model, the training score is very high while the cross-validation score is noticeably lower, creating a large gap between the two curves. 

This means the model has high variance. It learns the training data very well, including the noise, but does not generalize as well to new, unseen data.


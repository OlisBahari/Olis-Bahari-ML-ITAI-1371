## Part 1: Project Definition

This project aims to build and compare machine learning models that classify movie reviews as either positive or negative. It uses the NLTK Movie Reviews dataset, looks at the text and class distribution, preprocesses the reviews, turns the text into TF-IDF features, trains several classifiers, and checks how well they perform.

Models Compared

* Logistic Regression
* Multinomial Naive Bayes
* Linear Support Vector Machine (LinearSVC)

The best model is chosen based on the weighted F1-score. The project also looks at accuracy, precision, recall, confusion matrices, training time, and examples of misclassified reviews.


## Part 2: EDA

This section loads the NLTK Movie Reviews dataset, checks its structure and data quality, examines class balance and review lengths, and explores frequently occurring words in positive and negative reviews.


## Part 3: Preprocessing & Feature Extraction

To prepare the reviews, the text is changed to lowercase and any URLs, HTML tags, mentions, digits, or extra characters are removed. After cleaning, the data is divided into training and testing sets.

TF-IDF is trained using only the training data, and then the same transformation is applied to the test data. This approach helps make sure that no information from the test set influences the model during training.


## Part 4: Modeling

We train three classification algorithms using the same TF-IDF training matrix to ensure a fair comparison of their performance.
1. Logistic Regression
2. Multinomial Naive Bayes
3. Linear SVM


##Part 5: Evaluation

We evaluate each model using accuracy, weighted precision, weighted recall, weighted F1-score, a classification report, and a confusion matrix. After that, we rank the models based on their weighted F1-score.


Error Analysis

This last section looks at examples that the best-performing model got wrong. By reviewing these misclassified cases, we can spot challenging language patterns like ambiguity, sarcasm, mixed opinions, or unusual wording.




## Part 6: Conclusion

This project shows a full supervised text-classification process. Movie reviews are cleaned, turned into TF-IDF features, and then three machine-learning classifiers are trained and tested using the same stratified train/test split.

The final comparison picks the best model using the weighted F1-score instead of just accuracy. Since the dataset has equal numbers of positive and negative reviews, accuracy is useful, but looking at precision, recall, F1-score, confusion matrices, and individual errors gives a fuller picture.

Key Strengths

* Uses a balanced public sentiment dataset.
* Checks missing values and duplicate rows.
* Preserves important negation words such as not, no, nor, and never.
* Uses unigram and bigram TF-IDF features.
* Fits TF-IDF on training data only, which avoids test-set leakage.
* Compares three different classification algorithms.
* Includes both quantitative metrics and qualitative error analysis.


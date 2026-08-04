Purpose: Compare manual data preprocessing with a Scikit-Learn
pipeline using a Random Forest classifier on the Titanic dataset.

Reflective Knowledge Check

1. Code Comparison

Using a Pipeline helps keep your code simple, consistent, and less likely to have errors.
Combining preprocessing and model training in one workflow makes everything easier to manage.
This way, you can be sure that preprocessing is done the same way for both your training and test data.
It also helps you avoid mistakes, such as fitting a scaler or encoder on your test data.



Reflective Knowledge Check

2. Data Leakage Explained

Use scaler.fit_transform() only on your training data so the scaler learns the mean and standard deviation from that set. After that, apply scaler.transform() to your test data. Fitting the scaler on the test data can cause data leakage and make your model evaluation less trustworthy.

The Pipeline helps automate these steps. When you run final_pipeline.fit(X_train, y_train), it fits the preprocessing steps using just the training data. Later, when you use final_pipeline.predict(X_test), it applies the same preprocessing to the test data without fitting again.

Reflective Knowledge Check

 3. Extending the Pipeline

I suggest placing PCA after the preprocessor and before the RandomForestClassifier in the final pipeline. The steps would look like this:

Preprocessing → PCA → Random Forest

This approach first cleans, scales, and encodes the data. PCA then reduces the number of features before the processed data is sent to the Random Forest classifier.

Reflective Knowledge Check

4. Real-World Value

A single final_pipeline object is safer and more reliable because it manages the whole machine-learning workflow in the right order. The deployment team can enter raw data and get predictions without having to apply each preprocessing step and the model by hand.

If you use separate objects, you might skip steps, do them in the wrong order, or use different preprocessing settings by mistake. A single pipeline makes sure new data is handled the same way as the training data, which keeps deployment consistent and helps prevent errors.

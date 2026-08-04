Purpose: Train a logistic regression model and audit its
fairness across male and female demographic groups.

Reflective Knowledge Check

1. Analyze Your Results

Accuracy for Males: 81.20%

Accuracy for Females: 91.81%

The model demonstrates a 10.61 percentage point difference in accuracy, performing at 81.20% for males and 91.81% for females. It is more accurate for females overall.

Reflective Knowledge Check

2. Interpret the Errors

The False Positive Rate (FPR) was 10.26% for males and 2.81% for females. This means the model is more likely to make false positive errors for males, so male applicants without high incomes are more often misclassified as having high incomes.

In loan applications, this error can lead lenders to approve loans or offer better terms to people whose real income does not support the loan. This raises financial risk for lenders and may put applicants at risk of debt they cannot manage.

The False Negative Rate (FNR) shows another fairness issue. The FNR was 37.80% for males and 47.84% for females, which means high-income females are more likely than males to be misclassified as having lower incomes.

Reflective Knowledge Check

3. Justify a Decision

I would not approve this model for screening candidates for high-paying jobs, as a false negative could result in a qualified individual being unfairly rejected and losing a valuable opportunity.

The model's false negative rate is 47.84% for females and 37.80% for males, a difference of nearly 10 percentage points. This indicates the model is more likely to overlook qualified high-income female candidates. Although overall accuracy is higher for females, the elevated false negative rate increases the risk of rejecting qualified female applicants. The false positive rates also differ, at 10.26% for males and 2.81% for females, indicating errors are not distributed evenly. I recommend conducting additional fairness assessments and applying bias reduction techniques before approving the model.

Reflective Knowledge Check

4. Propose a Mitigation

Removing the sex column does not ensure fairness, as other variables may still correlate with sex and convey similar information. For example, occupation, relationship status, marital status, education, and hours worked per week often differ between men and women.

The model may still detect patterns related to sex, even without the sex column. While removing a sensitive attribute can reduce bias, it is important to reassess fairness after retraining. Recalculate subgroup accuracy, false positive rate (FPR), and false negative rate (FNR) to determine whether differences between men and women have decreased.

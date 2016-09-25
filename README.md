# Image-Classification
This is the solution for a programming project from BerkeleyX: CS188.1x Artificial Intelligence class.</br>
three classifiers are designed: a naive Bayes classifier, a perceptron classifier and a large-margin (MIRA) classifier. </br>
You can test classifiers on two image data sets: a set of scanned handwritten digit images and a set of face images in which edges have already been detected. More descriptions are in the classification.html</br></br>
Discussion & Analysis:</br>
1) Many types of classifiers have a common training structure in practice: using training data for the main supervised training loop but tuning certain parameters with a small held-out validation set.</br>
2) For some classifiers (Naive Bayes, MIRA), you will need to return the parameters' values after training and tuning step. I also try different numbers of iterations in Perceptron and see how it influences the performance. More iterations is more likely to get precise weights.</br>
3) We can also find the training data set size increases, the test accuracy increases. However, the maximum test accuracy does not occur in the maximum training data set size. All three classifiers have the maximum test accuracy over 80%.</br>
4) Another fact is that as the the training data set size increases, the running time of Perceptron and MIRA classifiers have a linear increase. Naive bayes classifier remains the same. MIRA is an online learner which is closely related to the Perceptron classifiers.</br>
5) The main difference between a good classification system and a bad one is usually not the classifier itself (e.g. Perceptron vs. Naive Bayes), but rather the quality of the features used.


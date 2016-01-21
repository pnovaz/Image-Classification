# mira.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        self.features = trainingData[0].keys() # this could be useful for your code later...

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        """
        This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid,
        then store the weights that give the best accuracy on the validationData.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        representing a vector of values.
        """
	lab = util.Counter()
	cwts = util.Counter()
	a = 0	
	count = util.Counter()
	for c in Cgrid:
        	for iteration in range(self.max_iterations):
        	    	for i in range(len(trainingData)):
                        # Try to guess the label 
				for l in self.legalLabels:
					lab[l] = trainingData[i].__mul__(self.weights[l])
                    # Wrong guess, update weights
				if not(trainingLabels[i] == lab.argMax()):
					x = trainingLabels[i]
					y = trainingData[i]
					z = lab.argMax()
					tou = ((self.weights[z].__sub__(self.weights[x])).__mul__(y) +1.0)/2.0/(y.__mul__(y)) 
					d = min(tou,c)
					j = util.Counter()	
					for k in trainingData[i].keys():
						j[k] = trainingData[i][k]*d
					self.weights[trainingLabels[i]].__radd__(j)
					self.weights[lab.argMax()].__sub__(j)
		cwts[c] = self.weights
        # Check the accuracy associated with this c
		for i in range(len(validationData)):
			for l in validationLabels:
				lab[l] = validationData[i].__mul__(self.weights[l])
			if (validationLabels[i] == lab.argMax()):
				a += 1	
		count[c] = a
	self.weights = cwts[count.argMax()]

    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses

    def findHighOddsFeatures(self, label1, label2):
        """
        Returns a list of the 100 features with the greatest difference in feature values
                                         w_label1 - w_label2

        """
        featuresOdds = []

        "*** YOUR CODE HERE ***"

        return featuresOdds


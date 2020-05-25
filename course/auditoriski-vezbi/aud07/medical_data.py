import csv
import math
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    with open('medical_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]
        dataset = [[int(dataset[i][j]) for j in range(0, len(dataset[i]))] for i in range(0, len(dataset))]

        train_set = dataset[:math.ceil(len(dataset) *0.8)]
        test_set = dataset[math.ceil(len(dataset) *0.8):]

        train_x = [x[:-1] for x in train_set]
        train_y = [x[-1] for x in train_set]

        classifier = GaussianNB()
        classifier.fit(train_x, train_y)

        print(classifier.predict([test_set[0][:-1]]))
        print(classifier.predict_proba([test_set[0][:-1]]))

        podatoci = [int(element) for element in input().split(' ')]
        print(classifier.predict([podatoci]))
        print(classifier.predict_proba([podatoci]))

        accuracy = 0
        for row in test_set:
            predicted = classifier.predict([row[:-1]])
            if predicted == row[-1]:
                accuracy += 1
        print(f'Accuracy: {accuracy/len(test_set)}')

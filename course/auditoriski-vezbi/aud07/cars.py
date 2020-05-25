import csv
import math
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

def nacin1():
    """
    eden nacin na citanje od fajl
    """
    csv_file = open('cars.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_file.close()

if __name__ == '__main__':
    with open('cars.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        #kaj Naive bayes podatocite morat da bidat od numericki tip
        #zatoa mora da se enkodiraat (transformacija od tekstualni vo numericki vrednosti)
        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(0, len(dataset))])
        #fit() sluzi za treniranje na enkoderot


        train_set = dataset[0:math.ceil(len(dataset) * 0.7)]
        test_set = dataset[math.ceil(len(dataset) * 0.7):]

        #X = [train_set[i][:-1] for i in range(0, len(train_set))]
        #Y =[train_set[i][-1] for i in range(0, len(dataset))]
        train_x = [x[:-1] for x in train_set]
        train_x = encoder.transform(train_x)
        train_y = [x[-1] for x in train_set]

        classifier = CategoricalNB()
        classifier.fit(train_x, train_y)
        test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))])

        #Tochnost na klasifikatorot
        accuracy = 0
        for i in range(0, len(test_set)):
            predict = classifier.predict([test_set_x[i]])
            if predict == test_set[i][-1]:
                accuracy += 1
        print(f'Accuracy: {accuracy/len(test_set)}')


        podatoci =[element for element in input().split(' ')]
        print(classifier.predict(podatoci))





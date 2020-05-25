import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    with open('cars.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        encoder = OrdinalEncoder()
        encoder.fit([row[:-1] for row in dataset])

        train_set = dataset[:int(len(dataset) *0.7)]
        test_set = dataset[int(len(dataset) *0.7):]

        train_set_x = [x[:-1] for x in train_set]
        train_set_x = encoder.transform(train_set_x)
        train_set_y = [x[-1] for x in train_set]

        test_set_x = [x[:-1] for x in test_set]
        test_set_x = encoder.transform(test_set_x)
        test_set_y =[x[-1] for x in test_set]

        classifier = RandomForestClassifier(n_estimators=3, criterion='entropy')
        classifier.fit(train_set_x, train_set_y)

        acc = 0
        for x,y in zip(test_set_x, test_set_y):
            predicted = classifier.predict([x])[0]
            if y == predicted:
                acc += 1
        print(f'Accuracy: {acc/len(test_set)}')

        classifier2 = RandomForestClassifier(n_estimators=3, criterion='entropy')
        classifier3 = RandomForestClassifier(n_estimators=5, criterion='entropy')

        #Random forest e podobar od Decision tree vo slucaj koga imame pogolem broj na atributi

        feature_importances = list(classifier.feature_importances_)
        mif = feature_importances.index(max(feature_importances))
        lif = feature_importances.index(min(feature_importances))
        print(f'Most important feature: {mif}\nLeast important feature: {lif}')

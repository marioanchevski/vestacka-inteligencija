import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

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

        classifier = DecisionTreeClassifier(criterion='entropy')
        classifier.fit(train_set_x, train_set_y)

        print(f'Depth: {classifier.get_depth()}\nLeaves: {classifier.get_n_leaves()}')

        correct_samples = 0
        for x,y in zip(test_set_x, test_set_y):
            predicted = classifier.predict([x])[0]
            if y == predicted:
                correct_samples += 1
        print(f'Accuracy {correct_samples/len(test_set)}')

        #Vaznost na sekoja od karakteristikite od mnozestvoto
        feature_importances = list(classifier.feature_importances_)
        print(f'Feature importances: {feature_importances}')

        #Most important feature
        mif = feature_importances.index(max(feature_importances))
        print(f'Most important feature: {mif}')

        #Least_important feature
        lif = feature_importances.index(min(feature_importances))
        print(f'Least important feature: {lif}')

        train_x_2 = list()
        for x in train_set_x:
            data = [x[i] for i in range(len(x)) if i != mif]
            train_x_2.append(data)

        test_x_2 = list()
        for x in test_set_x:
            data = [x[i] for i in range(len(x)) if i != mif]
            test_x_2.append(data)

        train_x_3 = list()
        for x in train_set_x:
            data = [x[i] for i in range(len(x)) if i != lif]
            train_x_3.append(data)

        test_x_3 = list()
        for x in test_set_x:
            data = [x[i] for i in range(len(x)) if i != lif]
            test_x_3.append(data)


        classifier2 = DecisionTreeClassifier(criterion='entropy')
        classifier2.fit(train_x_2, train_set_y)
        print(f'Depth (removed most important feature): {classifier2.get_depth()}')
        print(f'Leaves (removed most important feature): {classifier2.get_n_leaves()}')

        classifier3 = DecisionTreeClassifier(criterion='entropy')
        classifier3.fit(train_x_3, train_set_y)
        print(f'Depth (removed least important feature): {classifier3.get_depth()}')
        print(f'Leaves (removed least important feature): {classifier3.get_n_leaves()}')

        acc2 = 0
        for x,y in zip(test_x_2, test_set_y):
            predicted = classifier2.predict([x])[0]
            if y == predicted:
                acc2 += 1
        print(f'Accuracy (removed most important feature): {acc2/len(test_set)}')

        acc3 = 0
        for x, y in zip(test_x_3, test_set_y):
            predicted = classifier3.predict([x])[0]
            if y == predicted:
                acc3 += 1
        print(f'Accuracy (removed least important feature): {acc3 / len(test_set)}')
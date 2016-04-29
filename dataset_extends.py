import pandas as pd
import numpy as np
import random
import scipy.ndimage as nd

IMAGE_WIDTH=28
IMAGE_WIDTH=28

def load_training_data():
    data = pd.DataFrame.as_matrix(pd.read_csv("/Users/dragonjohn/Documents/DevEnv/Python/digitUnpack/trainR1_azure.csv"))
    Y = data[:, 0]
    data = data[:, 1:] # trim first classification field
    X = normalize_data(data)
    return X, Y

def normalize_data(X):
    return X/255.0

def nudge_dataset(X, Y):
    nudge_size = 2
    direction_matricies = [
        [[0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [1, 0, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 1],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 1, 0]]]

    scaled_direction_matricies = [[[comp*nudge_size for comp in vect] for vect in matrix] for matrix in direction_matricies]
    shift = lambda x, w: np.convolve(x.reshape((IMAGE_WIDTH, IMAGE_WIDTH)), mode='constant',
                                  weights=w).ravel()
    X = np.concatenate([X] +
                       [np.apply_along_axis(shift, 1, X, vector)
                        for vector in scaled_direction_matricies])

    Y = np.concatenate([Y for _ in range(5)], axis=0)
    return X, Y

def rotate_dataset(X, Y):
    rot_X = np.zeros(X.shape)
    for index in range(X.shape[0]):
        sign = random.choice([-1, 1])
        angle = np.random.randint(8, 16)*sign
        rot_X[index, :] = threshold(nd.rotate(np.reshape(X[index, :],
            ((28, 28))), angle, reshape=False).ravel())
    XX = np.vstack((X,rot_X))
    YY = np.hstack((Y,Y))
    return XX, YY

def threshold(X):
    X[X < 0.15] = 0.0
    X[X >= 0.85] = 1.0
    return X

def run():
    X_train, Y_train = load_training_data()

    X_train, Y_train = rotate_dataset(X_train, Y_train)
    X_train, Y_train = nudge_dataset(X_train, Y_train)

    n_features = X_train.shape[1]
    n_classes = 10
    classifier = DBN([n_features, 8000, n_classes],
        learn_rates=0.3, learn_rate_decays=0.9, epochs=80, verbose=1)

    classifier.fit(X_train, Y_train)

    test_data = get_test_data_set()
    predictions = classifier.predict(test_data)
    write_to_csv(predictions)

if __name__ == "__main__":
    print "yes"
    run()

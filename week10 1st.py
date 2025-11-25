import matplotlib.pyplot as plt
import tensorflow as tf
from keras.utils import to_categorical
layers = tf.keras.layers
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
# one-hot encode the labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
plt.figure(figsize=(10,8))
for i in range(1, 15):
# image in ith position of grid
    plt.subplot(5, 5, i)
plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
plt.show()
model = tf.keras.Sequential()
model.add(layers.Flatten())
model.add(layers.Dense(5, activation='sigmoid'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy',
metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=32,
validation_data=(x_test, y_test))
loss, accuracy = model.evaluate(x_test, y_test)
print('\n\nTest loss', loss)
print('Test accuracy', accuracy)
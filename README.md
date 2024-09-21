# Digit-Recognition
__MNIST Digit Recognition__

An implementation of multilayer neural network using PyTorch with an accuracy over 99%.

__About MNIST dataset:__

The MNIST database (Modified National Institute of Standards and Technology database) of handwritten digits consists of a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. Additionally, the black and white images from NIST were size-normalized and centered to fit into a 28x28 pixel bounding box and anti-aliased, which introduced grayscale levels.

__Structure of Neural Network:__
A neural network is made up by stacking layers of neurons, and is defined by the weights of connections and biases of neurons. Activations are a result dependent on a certain input.

This structure is known as a feedforward architecture because the connections in the network flow forward from the input layer to the output layer without any feedback loops. In this figure:

- The input layer contains the predictors.

- The hidden layer contains unobservable nodes, or units. The value of each hidden unit is some function of the predictors; the exact form of the function depends in part upon the network type and in part upon user-controllable specifications.

- The output layer contains the responses. Since the history of default is a categorical variable with two categories, it is recoded as two indicator variables. Each output unit is some function of the hidden units. Again, the exact form of the function depends in part on the network type and in part on user-controllable specifications. 

<img width="864" alt="Ảnh màn hình 2024-09-21 lúc 18 57 48" src="https://github.com/user-attachments/assets/b60e116c-a8bb-49a1-a406-b74c9d805024">

__Loss on Test Set and Accuracy of the Model__

<img width="560" alt="Ảnh màn hình 2024-09-21 lúc 18 59 08" src="https://github.com/user-attachments/assets/cf6a5bf1-00cd-4eea-9c65-bb7f52678a30">

__Result__

<img width="498" alt="Ảnh màn hình 2024-09-21 lúc 18 59 51" src="https://github.com/user-attachments/assets/5a56b942-ce0c-46a9-8795-e20ece5ec707">


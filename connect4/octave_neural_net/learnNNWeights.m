%% Learns neural network parameters for connect four

%% Initialization
clear ; close all; clc

%% ========== Customizable Zone ===========

input_file = '../generated_data/game_data.csv'

hidden_layer_size = 30;   % N hidden units
maximum_training_iterations = 200;
%  Lambda is the regularization term. 
%  A larger lambda means more bias and less over fitting
lambda = 0.0001;


%% ========== End Customizable Zone ===========
%% ========== Do NOT Modify Anything Below This Line ===========

%% Setup the parameters you will use for this exercise
input_layer_size  = 42;  % 6x7 Input Images of Digits
num_labels = 3;          % win, loss, tie

%% =========== Part 1: Loading The Data =============

% Load Training Data
fprintf('Loading Data ...\n')

D = dlmread(input_file);

X = D(:, 1:(size(D,2) - 1));
y = D(:, size(D,2)); 

% labels must be in the range of 1 to num_labels 
y(y == -1) = 2; %convert losses for player1 to category 2
y(y == 0) = 3; %convert ties to category 3

m = size(X, 1);

%% ================ Part 2: Initializing Pameters ================

fprintf('\nInitializing Neural Network Parameters ...\n')

initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);

% Unroll parameters
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];


%% =================== Part 3: Training NN ===================
%  To train your neural network, we will now use "fmincg", which
%  is a function which works similarly to "fminunc". Recall that these
%  advanced optimizers are able to train our cost functions efficiently as
%  long as we provide them with the gradient computations.
%
fprintf('\nTraining Neural Network... \n')

%  Change the MaxIter to a larger
%  value to see how more training helps.
options = optimset('MaxIter', maximum_training_iterations);

%  Lambda is the regularization term. 
%  A larger lambda means more bias and less over fitting
%lambda = 0.0001;

% Create "short hand" for the cost function to be minimized
costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, X, y, lambda);

% Now, costFunction is a function that takes in only one argument (the
% neural network parameters)
[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

% Obtain Theta1 and Theta2 back from nn_params
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

fprintf('Program paused. Press enter to continue.\n');
pause;


%% ================= Part 4: Visualize Weights =================
%  You can now "visualize" what the neural network is learning by 
%  displaying the hidden units to see what features they are capturing in 
%  the data.

fprintf('\nVisualizing Neural Network... \n')

displayData(Theta1(:, 2:end), 7);

fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ================= Part 5: Implement Predict =================
%  After training the neural network, we would like to use it to predict
%  the labels. You will now implement the "predict" function to use the
%  neural network to predict the labels of the training set. This lets
%  you compute the training set accuracy.

pred = predict(Theta1, Theta2, X);


fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);


%% ================= Part 6: Dump Result To File =================
file_id = fopen('../generated_data/nn_training_output.txt', 'w');

fprintf(file_id, 'Theta 1:\n')

for r = 1:(size(Theta1,1))
	fprintf(file_id, '%f', Theta1(r,1))
	for c = 2:(size(Theta1,2))
		fprintf(file_id, ', %f', Theta1(r,c))
	end;
	if r != size(Theta1,1)
		fprintf(file_id, ';')
	end;
	fprintf(file_id, '\n')
end;

fprintf(file_id, '\n\nTheta 2:\n')
for r = 1:(size(Theta2,1))
	fprintf(file_id, '%f', Theta2(r,1))
	for c = 2:(size(Theta2,2))
		fprintf(file_id, ', %f', Theta2(r,c))
	end;
	if r != size(Theta2,1)
		fprintf(file_id, ';')
	end;
	fprintf(file_id, '\n')
end;

fclose(file_id);



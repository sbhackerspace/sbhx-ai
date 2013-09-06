function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

% calculate feed forward
a1 = [ones(m,1) X];

z2 = a1 * Theta1';
a2 = [ones(m,1) sigmoid(z2)];

z3 = a2 * Theta2';
h = sigmoid(z3);

% calculate cost 
for c = 1:num_labels
	J += (1/m)* ((-(y==c))'*log(h(:,c)) - ((1-(y==c))'*log(1-h(:,c))));
end;


% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

delta_1 = zeros(size(Theta1));
delta_2 = zeros(size(Theta2));

for t = 1:m

	% 1. calculate feed forward
	a_1 = [1; X(t,:)'];

	z_2 = Theta1 * a_1;
	a_2 = [1; sigmoid(z_2)];

	z_3 = Theta2 * a_2;
	a_3 = sigmoid(z_3);

	% 2. deltas for the output layer
	d_3 = (a_3 - ((1:num_labels)' == y(t)));

	% 3. hidden layer l=2
	d_2 = Theta2' * d_3 .* [1; sigmoidGradient(z_2)];
	d_2 = d_2(2:end);
	
	% 4. accumulate gradients
	delta_2 += d_3 * a_2';
	delta_1 += d_2 * a_1';

end;

% 5. calculated gradients
Theta1_grad = (1/m)*delta_1;
Theta2_grad = (1/m)*delta_2;


% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%


% regularization of cost
J += (lambda/(2*m))*(sum(sum((Theta1(:,2:end).*Theta1(:,2:end))))+sum(sum((Theta2(:,2:end).*Theta2(:,2:end)))));


% regularization of deltas

% 5. calculated gradients
tempT1 = Theta1;
tempT1(:,1) = 0;

tempT2 = Theta2;
tempT2(:,1) = 0;

Theta1_grad += (lambda/m)*tempT1;
Theta2_grad += (lambda/m)*tempT2;


% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end

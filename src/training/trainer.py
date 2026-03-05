from src.base import BaseTrainer
import numpy as np
from src.training.metrics import mse, rmse

class GradientDescentTrainer(BaseTrainer):
	"""Trainer for models using gradient descent."""
	
	def __init__(self, model, learning_rate: float = 0.01, iterations: int = 1000):
		"""Init GradientDescentTrainer 
			Args:
				model: The machine learning model to be trained.
				learning_rate: The learning rate for gradient descent.
				iterations: The number of iterations to perform during training.
		"""
		super().__init__(model, learning_rate, iterations)
	
	def train(self, x: np.ndarray, y: np.ndarray) -> None:
		"""Train the model using gradient descent.
			Args:
				x (np.ndarray): The input features for training.
				y (np.ndarray): The target values for training.
		"""
		n = len(x)
		print(f"\033[93mTraining Linear Regression model...\033[0m")
		for i in range(self.iterations):
			sum_error_theta0 = 0
			sum_error_theta1 = 0

			for xi, yi in zip(x, y):
				y_pred = self.model.predict(xi)
				error = y_pred - yi
				sum_error_theta0 += error
				sum_error_theta1 += error * xi
			
			if i % 100 == 0:
				train_y = self.model.predict(x)
				print(f"RMSE: {rmse(y, train_y):.2f}€ | Learning rate: {self.learning_rate} | Iteration: {i}/{self.iterations}")
			correction_theta0 = (self.learning_rate * sum_error_theta0) / n
			correction_theta1 = (self.learning_rate * sum_error_theta1) / n

			self.model.theta0 -= correction_theta0
			self.model.theta1 -= correction_theta1

		print(f"\033[32mTraining of Linear Regression model done\033[0m")
		y_pred = self.model.predict(x)
		print(f"\033[93mFinal RMSE: {rmse(y, y_pred):.2f}€\033[0m")
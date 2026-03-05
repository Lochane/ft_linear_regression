from src.base import BaseModel
import numpy as np

class LinearRegression(BaseModel):
	"""A simple implementation of linear regression using gradient descent."""
	def __init__(self, theta0: float= 0.0, theta1: float = 0.0):
		"""Init Model parameters.
			Args:
				theta0 (float): The intercept of the linear model.
				theta1 (float): The slope of the linear model.
		"""		
		self.theta0 = theta0
		self.theta1 = theta1

	def predict(self, x: np.ndarray) -> np.ndarray:
		"""Predict the target values for the given input features.
			Model hypothesis : price = theta0 + theta1 * mileage
			Args:
				x (np.ndarray): The input features.
			Returns:
				np.ndarray: The predicted target values.
		"""
		return self.theta0 + self.theta1 * x

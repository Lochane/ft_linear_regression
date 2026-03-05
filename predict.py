"""Predict the price of a car based on its mileage using a trained linear regression model.
This script loads a pre-trained linear regression model, takes user input for mileage, and predicts the price of the car. It also handles potential errors in user input and model loading.
"""

import numpy as np
from src.persistence import load_model
from src.preprocessing import StandardScaler
from src.models import LinearRegression


def main():
	try :
		mileage = float(input("Enter a mileage: "))
		if mileage < 0:
			print("\033[31mValueError: Mileage must be a positive number\033[0m")
			return
	except ValueError as e:
		print(f"\033[31mValueError: {e}\033[0m")
		return

	try:
		model_param = load_model("data/models/thetas.json")
	except Exception as e:
		print(f"\033[31m{e}\033[0m")
		return
	model = LinearRegression(model_param["theta0"], model_param["theta1"])
	scaler = StandardScaler(model_param["mileage_mean"], model_param["mileage_std"])

	normalized_mileage = scaler.transform(np.array(mileage))
	estimate_price = model.predict(normalized_mileage)

	print(f"\033[32mEstimate price is : {estimate_price:.2f}€\033[0m")


if __name__ == "__main__":
	main()
import pandas as pd
import json
import math

def main():
	try :
		file = pd.read_csv("data.csv")
	except FileNotFoundError:
		print("Error: File not found")
		return
	except pd.errors.ParserError:
		print("Error: File is not a valid CSV format")
		return
	except Exception as e:
		print(f"Unexpected error: {e}")
		return
	
	try :
		with open("thetas.json", "r") as datafile:
			data = json.load(datafile)
	except FileNotFoundError:
		print("Error: File not found")
		return
	except json.JSONDecodeError:
		print("Error; File is not valid JSON")
		return

	price = file["price"].values
	mileage = file["km"].values

	mileage_mean = data["mileage_mean"]
	mileage_std = data["mileage_std"]
	mileage = (mileage - mileage_mean) / mileage_std
	
	n = len(mileage)
	error_sum = 0.0
	for x, y in zip(mileage, price):
		prediction = data["theta0"] + data["theta1"] * x
		error_sum += (prediction - y) ** 2

	mse = error_sum / n
	rmse = math.sqrt(mse)
	print(f"RMSE: {rmse:.2f}€")

if __name__ == "__main__":
	main()
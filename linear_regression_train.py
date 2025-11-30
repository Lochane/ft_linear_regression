import pandas as pd
import json
from utils import ft_mean, ft_std_dev
import matplotlib.pyplot as plt

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

	price = file["price"].values
	mileage = file["km"].values
	raw_mileage = mileage.copy()

	mileage_mean = ft_mean(mileage)
	mileage_std = ft_std_dev(mileage)
	mileage = (mileage - mileage_mean) / mileage_std

	theta0 = 0
	theta1 = 0
	learning_rate = 0.01
	iterations = 1000
	n = len(mileage)

	for _ in range(iterations):
		sum_error_theta0 = 0
		sum_error_theta1 = 0

		for x, y in zip(mileage, price):
			prediction = theta0 + theta1 * x
			error = prediction - y
			sum_error_theta0 += error
			sum_error_theta1 += error * x
		
		correction_theta0 = (learning_rate * sum_error_theta0) / n
		correction_theta1 = (learning_rate * sum_error_theta1) /n

		theta0 -= correction_theta0
		theta1 -= correction_theta1

	params = {"theta0": theta0, "theta1": theta1, "mileage_mean": mileage_mean, "mileage_std": mileage_std}
	with open("thetas.json", "w") as f:
		json.dump(params, f)

	predicted_price = theta0 + theta1 * mileage

	plt.scatter(raw_mileage, price, label="Original dataset")
	plt.plot(raw_mileage, predicted_price, color="red", label="Linear Regression")
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.title("Linear Regression on data set")
	plt.legend()
	plt.grid(True)
	plt.savefig("linear_regression_graph.png")


if __name__ == "__main__":
	main()
import json

def main():
	try :
		with open("thetas.json", "r") as file:
			data = json.load(file)
	except FileNotFoundError:
		print("Error: File not found")
		return
	except json.JSONDecodeError:
		print("Error; File is not valid JSON")
		return
	
	try :
		mileage = float(input("Enter a mileage: "))
		if mileage < 0:
			print("ValueError: Mileage must be a positive number")
			return
	except ValueError:
		print("ValueError: Invalid input. Please enter a number")
		return
	mileage_mean = data["mileage_mean"]
	mileage_std = data["mileage_std"]
	normalized_mileage = (mileage - mileage_mean) / mileage_std

	estimate_price= data["theta0"] + (data["theta1"] * normalized_mileage)
	print(f"Estimate price is : {estimate_price:.2f}€")


if __name__ == "__main__":
	main()
"""Train a linear regression model to predict car prices based on mileage.
This script loads the dataset, preprocesses the data, trains a linear regression model using gradient descent, saves the trained model parameters, and visualizes the results. It also handles potential errors during data loading and model training.
"""

from src.preprocessing import load_csv, StandardScaler
from src.models import LinearRegression
from src.training import GradientDescentTrainer
from src.persistence import save_model
from src.visualization import LayerConfig, PlotConfig, plot
from dataclasses import dataclass



def main():

	try:
		df = load_csv("data/raw/data.csv")
	except Exception as e:
		return print(f"\033[31m{e}\033[0m")
		
	
	scaler = StandardScaler()
	model = LinearRegression()
	trainer = GradientDescentTrainer(model=model)
	raw_mileage = df["km"].to_numpy()
	price = df["price"].to_numpy()
	normalized_mileage = scaler.fit_transform(raw_mileage)


	trainer.train(normalized_mileage, price)
	params = {"theta0": model.theta0, "theta1": model.theta1, "mileage_mean": scaler.mean, "mileage_std": scaler.std} 
	save_model(params, "data/models/thetas.json")


	predicted_price = model.predict(normalized_mileage)
	plot_layers = [
		LayerConfig(type="line", label="Linear Regression", values=(raw_mileage, predicted_price), color="red"),
		LayerConfig(type="scatter", label="Original dataset", values=(raw_mileage, price))]
	
	plot(PlotConfig(x_label="KM", y_label="Price", tittle="Linear Regression on data set", layers=plot_layers, output_path="linear_regression_graph.png"))


if __name__ == "__main__":
	main()
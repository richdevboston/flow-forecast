import argparse
from typing import Dict
import json
from flood_forecast.pytorch_training import train_transformer_style
from flood_forecast.time_model import PyTorchForecast


def train_function(model_type: str, params: Dict):
    dataset_params = params["dataset_params"]
    dataset_params["forecast_history"] = 1
    dataset_params["forecast_length"] = 1
    dataset_params["forecast_something_or"] = 1
    trained_model = PyTorchForecast(
        params["model_name"],
        dataset_params["training_path"],
        dataset_params["validation_path"],
        dataset_params["test_path"],
        params)
    train_transformer_style(trained_model, params["training_params"], params["forward_params"])
    return trained_model


def main():
    """
    Main function which is called from the command line. Entrypoint for all ML models.
    """
    parser = argparse.ArgumentParser(description="Argument parsing for training and eval")
    parser.add_argument("-p", "--params", help="Path to model config file")
    args = parser.parse_args()
    with open(args.params) as f:
        training_config = json.load(f)
    train_function(training_config["model_type"], training_config)
    # evaluate_model(trained_model)
    print("Process is now complete.")

if __name__ == "__main__":
    main()
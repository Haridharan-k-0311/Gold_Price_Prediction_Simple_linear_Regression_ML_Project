# Gold Price Prediction Using Simple Linear Regression

This project aims to predict the price of gold in India using a simple linear regression model. It leverages historical gold price data along with the USD/INR exchange rate to create a predictive model. The project includes data preprocessing, model training, and evaluation.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Files Included](#files-included)
- [License](#license)

## Introduction

The project uses machine learning to predict the future price of gold based on historical price data and USD/INR exchange rates. A simple linear regression model is used to make predictions based on past trends.

The workflow consists of several steps:
1. **Data Collection**: Gathering gold price data and USD/INR exchange rates.
2. **Data Cleaning**: Preparing and cleaning the data for model training.
3. **Model Training**: Using the Simple Linear Regression algorithm to build a predictive model.
4. **Model Evaluation**: Evaluating the model performance using accuracy metrics.
5. **Prediction**: Using the trained model to predict future gold prices.

## Project Structure

```
Gold_Price_Prediction_Simple_linear_Regression_ML_Project/
├── dataset_combine_And_data_cleaning.ipynb
├── gold_price_dataset_web_scripting.ipynb
├── USD_INR_dataset_web_scriping.ipynb
├── MAIN_gold_price_Prediction_India.ipynb
├── regressor.pkl
├── README.md
└── requirements.txt
```

### Files Included

- `dataset_combine_And_data_cleaning.ipynb`: This notebook contains the data preprocessing and combination of gold price data and USD/INR exchange rate data.
- `gold_price_dataset_web_scripting.ipynb`: This notebook handles web scraping for gold price data.
- `USD_INR_dataset_web_scriping.ipynb`: This notebook handles web scraping for the USD/INR exchange rate data.
- `MAIN_gold_price_Prediction_India.ipynb`: This is the main notebook where the model is trained, evaluated, and predictions are made.
- `regressor.pkl`: A pre-trained model that can be used for gold price prediction.
- `README.md`: This documentation file.
- `requirements.txt`: Contains the necessary libraries to run the project.

## Requirements

To run this project, you need to install the required libraries. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

The necessary libraries include:
- `pandas`
- `numpy`
- `matplotlib`
- `sklearn`
- `requests`
- `beautifulsoup4`
- `joblib`

## How to Run

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Haridharan-k-0311/Gold_Price_Prediction_Simple_linear_Regression_ML_Project.git
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Jupyter notebooks in the following order:

   - First, run `gold_price_dataset_web_scripting.ipynb` to scrape the gold price data.
   - Then, run `USD_INR_dataset_web_scriping.ipynb` to scrape the USD/INR exchange rate data.
   - Next, run `dataset_combine_And_data_cleaning.ipynb` to clean and combine the data.
   - Finally, run `MAIN_gold_price_Prediction_India.ipynb` to train the model and make predictions.

4. Alternatively, you can load the pre-trained model from `regressor.pkl` to skip the training phase and directly make predictions on new data.

## Sample Output

Below is a sample output from the project showing the relationship between the gold price and the USD/INR exchange rate. The plot visualizes how the gold price changes over time based on the model's predictions.

![Sample Output](https://github.com/Haridharan-k-0311/Gold_Price_Prediction_Simple_linear_Regression_ML_Project/sample_output/output.png)

In this example, the predicted gold prices are shown, and the trend over time can be observed. You can modify the path to the image to match the location of your output file.

## Files Included

- `dataset_combine_And_data_cleaning.ipynb`
- `gold_price_dataset_web_scripting.ipynb`
- `USD_INR_dataset_web_scriping.ipynb`
- `MAIN_gold_price_Prediction_India.ipynb`
- `regressor.pkl`
- `README.md`
- `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

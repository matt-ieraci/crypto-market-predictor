
# Market Prediction Model (yfinance)

Financial Market Analysis Using Wyckoff Method and Machine Learning


## Introduction

This project is at the intersection of traditional technical analysis and modern machine learning techniques, aimed at deciphering financial market behaviors to predict future price movements. Leveraging the century-old Wyckoff Method, renowned for its effectiveness in understanding market structures through price actions and volume analysis, the project seeks to translate these classical concepts into quantifiable features that can be utilized by machine learning models.

## Objective

The primary objective is to build a predictive model capable of forecasting future prices of financial instruments. By integrating the principles of the Wyckoff Method with data-driven machine learning approaches, we aim to create a tool that not only predicts market trends but also uncovers the underlying dynamics of supply and demand that drive market movements.

## Features and Target Variable

Features: The project meticulously crafts features from raw financial data, including open, high, low, close prices, and volume. It extends beyond basic metrics to include derived features emblematic of the Wyckoff Method, such as price spread, relative volume, and indicators of accumulation and distribution phases. Additional technical indicators, like moving averages and the Average True Range (ATR), serve to enrich the model's input.
Target Variable: The model focuses on predicting the future closing price, either as a continuous value (regression) or as a classification of the price movement direction (up, down, or sideways).
Data Preprocessing

A comprehensive preprocessing pipeline ensures data quality and relevance. It involves cleaning, normalization, and the creation of engineered features that align with Wyckoff's theoretical constructs. The dataset is time-series in nature, necessitating careful handling to avoid look-ahead bias in training and testing phases.

## Model Selection and Evaluation

The project explores a range of models, from simple linear regression for baseline performance to more complex architectures like Random Forest and Gradient Boosting Machines for enhanced predictive power. For time-series data, deep learning models like RNNs and LSTMs are evaluated for their ability to capture sequential dependencies. Model performance is rigorously assessed using appropriate metrics, including MAE and RMSE for regression tasks, and accuracy, precision, recall, and F1-score for classification objectives.

## Backtesting

An integral part of the project is backtesting the predictive models against historical data. This step is crucial for understanding the model's practical application and its performance across various market conditions. It provides insights into the model's robustness and its potential for real-world trading strategies.

## Conclusion

This project bridges the gap between traditional market analysis and modern predictive modeling, offering a novel approach to financial market prediction. It not only serves as a testament to the enduring relevance of the Wyckoff Method but also showcases the potential of machine learning in enhancing market analysis and forecasting efforts.

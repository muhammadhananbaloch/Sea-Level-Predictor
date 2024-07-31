# Sea Level Predictor

This repository contains a project that analyzes the global average sea level change since 1880 and predicts future changes through the year 2050. This project is part of the freeCodeCamp Data Analysis with Python certification.

## Project Overview

Using historical sea level data from the US Environmental Protection Agency (EPA), this project aims to visualize and predict sea level changes. The analysis includes:
- Importing and visualizing data with Pandas and Matplotlib.
- Using linear regression to fit lines and make predictions.
- Creating visual plots to depict trends and future predictions.

## Data Source

The dataset used in this project is the "Global Average Absolute Sea Level Change, 1880-2014" from the US Environmental Protection Agency, which includes data from CSIRO (2015) and NOAA (2015).

## Project Tasks

1. **Import Data**: Use Pandas to read data from `epa-sea-level.csv`.
2. **Scatter Plot**: Create a scatter plot using the Year column (x-axis) and the CSIRO Adjusted Sea Level column (y-axis).
3. **First Line of Best Fit**: Use `linregress` from `scipy.stats` to find the slope and y-intercept for the line of best fit for the entire dataset and extend it to 2050.
4. **Second Line of Best Fit**: Fit a new line using data from the year 2000 to the most recent year in the dataset and extend this line to 2050.
5. **Plotting**: Visualize both lines of best fit on the scatter plot.
6. **Labeling**: Add labels for the x-axis (Year), y-axis (Sea Level in inches), and a title (Rise in Sea Level).

## File Structure

- `sea_level_predictor.py`: The main script containing the data analysis and plotting code.
- `main.py`: Script for testing and visualizing the results.
- `test_module.py`: Unit tests for validating the project requirements.

## Installation

To run this project, you need to have Python and the following libraries installed:
- Pandas
- Matplotlib
- SciPy

You can install the required libraries using pip:

```bash
pip install pandas matplotlib scipy
```

## Usage

Run the analysis and generate the plots by executing `main.py`:

```bash
python main.py
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
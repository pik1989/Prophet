# Prophet

Prophet is a procedure for forecasting time series data. It is based on an additive model where non-linear trends are fit with yearly and weekly seasonality, plus holidays. It works best with daily periodicity data with at least one year of historical data. Prophet is robust to missing data, shifts in the trend, and large outliers.

Prophet is open source software released by Facebook's Core Data Science team. It is available for download on CRAN and PyPI.

# Installation in Python

Prophet is on PyPI, so you can use pip to install it:

	#bash
	$ pip install fbprophet
The major dependency that Prophet has is pystan. PyStan has its own installation instructions: http://pystan.readthedocs.io/en/latest/installation_beginner.html

After installation, you can get started here: https://facebook.github.io/prophet/docs/quick_start.html#python-api

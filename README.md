# Satellite-Launch-Cost-Minimization-Operations-Research

## Overview
This project leverages Operations Research techniques to solve the complex problem of minimizing the cost of launching Low Earth Orbit (LEO) satellites. By taking into account various factors such as location, weather, satellite size, cost, failure rate, and more, the goal is to identify the optimal day for a satellite launch. This personal project makes use of GCAT data and the National Weather API. Additionally, there is an interactive feature utilizing NWS's API to utilize the forecasted weather to determine the most cost-efficent site to conduct LEO launches within a 14-day period and limit failure rate.

## Key Features
- **Data Analysis**: Utilizes GCAT data for comprehensive satellite and launch information.
- **Weather Integration**: Incorporates data from the National Weather API to factor in historical and forecasted weather conditions.
- **Cost Optimization**: Focuses on minimizing overall launch costs considering multiple variables at various sites. 
- **Failure Rate Assessment**: Evaluates the risk associated with satellite launches.

## Packages/APIs
Python 3.11.1
- Gurobipy (Operations Research Solver)
- Pandas
- Numpy
- Matplotlib
- Seaborn
- National Weather Service API (NWS)

## How It Works
1. **Input Gathering**: Collects data on potential launch locations, satellite specifications, and desired launch windows.
2. **Weather Data Integration**: Fetches weather forecasts from the National Weather API for considered locations and dates.
3. **Optimization Algorithm**: Applies Operations Research algorithms to determine the most cost-effective launch day, balancing factors like weather conditions, satellite size, and failure rates.
4. **Output**: Provides a detailed report on the best day for the satellite launch, including cost analysis and risk assessment.

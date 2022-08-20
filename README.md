# Surfs_Up

## Project Overview:
The purpose of this analysis was to help our client, W. Avy, gather weather data across the island of Oahu. W. Avy wished to know if the weather on Oahu might be conducive to opening a Surf and Ice Cream shop. To accomplish this we used Python, Pandas, Numpy, and SQLAlchemy to query weather related data from weather stations on the island of Oahu. We analyzed weather data in the months of June and December across all years available in the dataset. In addition, we used Flask to create a basic website where other general weather data can be posted / accessed by our clients.  

## Resources
[app.py](app.py) - Establishes Flask routes along with queries to view precipitation and temperature related data from across a year-long period.

[SurfsUp_Challenge.ipynb](SurfsUp_Challenge.ipynb) - Contains the queries and summary statistics regarding temperature weather data from the months of June and December across all years within the given dataset.

## Results
- The mean temperature in June and December are 74.9F (STD=3.3) and 71.0F (STD=3.7), respectively.
- The median temperature in June and December are 75.0F and 71.0F, respectively.
- The minimum temperature in June and December are 64.0F and 56.0F, respectively.

## Summary
The similarity of the mean and median within the weather data indicates this dataset likely follows a normal distribution. Therefore, it is unlikely that outliars would skew this dataset. The mean temperatures in June and December are above 70F suggesting that weather in the winter and summer would be conducive to eating ice cream and surfing. The drop in temperatures to 56F might be somewhat problematic in December. It is unclear from our existing data at what time of day the measurements from the stations were taken. Further analysis could be performed to specifically look at measurements during W. Avy's proposed business hours. Finally, it might be wise to narrow in on specific weather stations that are close to known surf breaks. This would allow us to perform follup analyses on which locations would have the best weather and accessible surf breaks.

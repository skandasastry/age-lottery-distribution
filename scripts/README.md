# Script to read in data/produce visualizations

### Description
This is essentially the workhorse script that ties the project together. After scraping the data and producing the csvs, 
we can run this file, which reads in the draft history, player birthdates, and draft dates datasets. 
Then, it calculates the player age using datetime, as the difference between the Draft Day of the specific year
and the player birthdate. 

Finally, uses matplotlib and Seaborn to plot the box and whisker/lineplots and sends them to the ``output-files`` directory.

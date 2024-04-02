---
layout: default
---

![Banner](assets/cover2.png)


---

# Assigment 2


## Introduction
This is a webpage showcasing a short data-story based on the work done in the DTU 
course: "02806 Social data analysis and visualization-Spring 24" class so far. (This exercise is a kind of "micro version" of what we'll be doing in the final project). Follow the directions in the bulleted list below when you create your data-story.


## The dataset
The dataset which has been worked with is called; "Police Department Incident Reports: Historical 2003 to May 2018" and provides insight into observations of various crimes committed in San Francisco from 2003-2018. 
It consists of 2.13M observations which are categorized into 14 columns. These include e.g. a crime category (prostitution, car theft, robbery), the day and date of the crime, the time, the district and the coordinates of the crime.



## The analysis
In this section, we'll delve into the analysis of SF Crime Data and explore key insights.
The dataset contains observatinos of 37 different types of crimes but as a start we will only look at 14 different focuscrimes. We will also remove the year 2018 as only a fraction of the year is contained in the data.

<iframe src="heatmap2.html" width="800" height="400"></iframe>


### Bokeh plot for focuscrimes from 2003-2017:
To get an overview of the different types of crimes, a Bokeh plot have been made for each of the focuscrimes. As the plot is interactive it's easy to quickly compare the tendencies for each of the crimes. The Bokeh plot shows the development for each crime type in the years from 2003-2017. For better comparison and for all crime types to be interpretable, the data has been normalized:


<iframe src="bokeh_plot.html" width="800" height="400"></iframe>

The bokeh plot above is based on the one from week 6.
Some of the more interesting aspects can be seen in 'Drug/narcotic' falling from 2009 to 2017, 'Vehicle Theft' suddently being reduced from 2005 to 2006, and prostetution falling from 2007 to 2017.
For this analysis we have chosen to continue with 'Vehicle theft'.





![This is a bar plot](https://Madsem2.github.io/bar_plot.png)





---
## References
[1] East Bay Times. (2007, February 18). Auto thefts in state decline for first time in decade. Retrieved March 11, 2024, from https://www.eastbaytimes.com/2007/02/18/auto-thefts-in-state-decline-for-first-time-in-decade-2/

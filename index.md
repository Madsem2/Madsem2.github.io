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

## Bokeh plot for focuscrimes from 2003-2017:
To get an overview of the different types of crimes, a Bokeh plot have been made for each of the focuscrimes (Figure 1). As the plot is interactive it's easy to quickly compare the tendencies for each of the crimes. The Bokeh plot shows the development for each crime type in the years from 2003-2017. For better comparison and for all crime types to be interpretable, the data has been normalized.


<iframe src="bokeh.html" width="800" height="400"></iframe>
Figure 1 - Bokeh plot of the focus crimes over the years

The bokeh plot above is based on the one from week 6.
Some of the more interesting aspects can be seen in 'Drug/narcotic' falling from 2009 to 2017, 'Vehicle Theft' suddently being reduced from 2005 to 2006, and prostetution falling from 2007 to 2017.
For this analysis we have chosen to continue to investigate 'Vehicle theft'.



## Bar plot of Annual crime Descript count from 2003-2017:
When we dive into the data and plot the "type of crime" in a cluster of bar plots, some new patterns are visible.  A lot of the crime counts in the first years come from recovered vehicles from (2003-2005). These data types (VEHICLE, RECOVERED, XXXXX...) has no record of more recovered vehicles in the period 2006-2017, this makes a clear shift of the data and distorts our initial interpretation of the decrease of "Vehicle theft" between 2005 and 2006 obtained from the bokeh plot. There is still a drop, but it is now way closer to the actual numbers found in the article "Auto thefts in state decline for first time in decade" [1]. This article presents that "Car thefts were down 22.9 percent in San Francisco" from 2005 to 2006. Potential reasons to this decreasing trend are said to be:
1. Car owners buy more preventive devices (e.g. locks for the steering wheels & tracking systems)
2. Police officers increasingly using 'bait cars' to nap thieves
3. License Plate Recognition systems to spot stolen cars
4. Newer cars often have build in alarms

Other highlights from the bar chart:
- Raise in motorcycles
- The "Stolen car attempts" data is still heavily impacted by initiatives in from East bay times [1]  
![This is a bar plot](https://Madsem2.github.io/bar_plot.png)
Figure 2 - Bar plots of the various types of vehicle theft committed from 2003-2017

## Heatmap of stolen automibiles in San Francisco
To gain insights into the location of the actual stolen cars (not the recovered ones), the heatmap in Figure 3 is created. Here it becomes clear how the north western parts of San Francisco are the areas where vehicle theft occurs most often. This is much in line with the statement of the article "The Worst Parking Spots in SF for Car Break-Ins"[2], since it concludes that the area with the highest ratio of break-ins to available parking spots is Downtown/Civic Center/Tenderloin (matching the most red area on the heatmap on Figure 3). Even though this article is based on data from 2016,  it is fair to conclude that the least safe place to park your car is in the Tenderloin district.
<iframe src="vehicleHeatmap.html" width="800" height="400"></iframe>
Figure 3 - heatmap of stolen automobiles in San Francisco between 2003 and 2017

## Contributions

We have all been contributing to each of the plots as we have all made them thorugh the weekly assigments in the course, where we have been working collaboratively. 
However, adjusting the plots to this specific analysis have been divided as detailed below:<br>

Introduction: Together <br>
Bokeh plot: Rasmus Kongsted, s193984 <br>
Bar plots: Mads Emil Oxholm Iversen, s191229 <br>
Heatmap: Lin Chang Brendstrup, s193982 <br>




---
## References
[1] East Bay Times. (2007, February 18). Auto thefts in state decline for first time in decade. Retrieved March 11, 2024, from https://www.eastbaytimes.com/2007/02/18/auto-thefts-in-state-decline-for-first-time-in-decade-2/

[2]SpotAngels. (n.d.). SF Parking: Car Break-Ins & How to Prevent Them. Retrieved March 11, 2024, from https://www.spotangels.com/blog/sf-parking-car-break-ins/

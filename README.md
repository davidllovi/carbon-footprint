# What is this project?
The goal is to use the coordinates that google rutinarely stores in the phone to estimate the carbon footprint

## Step 1 
Clone this repository in your local system

## Step 2 Download your data from google
(taken from anthonyschmidt.co)

Navigate to Google Takeout, and first click “Deselect all” at the right. Then, scroll down to “Location History” and click on “Multiple Formats”. Choose JSON and click “OK”. Check the checkbox and scroll down to the bottom. Select “Next step”. Here you can export your data once or set a schedule. Click “create export”. Dependning on the amount of data, the export can take a few minutes (or “days” as Google claims). I got a year’s worth of data in about 3 minutes. Just refresh the page to check on the status.

When its ready, download your zip file. Extract your zip file somewhere convenient. Drill into the extracted folder until you find “Semantic Location Data”. That is what we are after. This will contain a folder for each year and a JSON file for each month in that year.

## Step 3 

### Useful links
To calculate the footprint for travel, food and more:
( I have taken the g per km in the code from here)

https://www.carbonfootprint.com/calculator.aspx

This web already does what I do, with beautiful graphs. Only that its code is hidden, and I wanted to play with the numbers. If you use it, beware that it takes a while to computert the date for a large number of years

http://markd.ie/2020/02/16/Google-Timeline-Carbon-Footprint-Calculator/

Some other docs I found useful:

https://www.anthonyschmidt.co/post/2020-02-10-carbon-footprint-google-data/
https://medium.com/@ggonzalezzabala/graph-your-own-google-location-history-in-tableau-e362d1d8f18d
https://github.com/gabrielgz92/location_history_data
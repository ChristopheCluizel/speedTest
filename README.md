SpeedTest
===

Some scripts to get ip, download and upload from [SpeedTest](http://www.speedtest.net/) and sum up these results in charts.

# Python method
My first approach was to download the results thanks to the [`speedtest-cli`](https://github.com/sivel/speedtest-cli) written in Python and store these results in a CSV file. Then, I read this file with another Python script - using [`Pygal`](http://www.pygal.org/en/latest/) - which generated a line chart and boxplots, before included them in a HTML page. However, `Pygal` was not the best tool to plot hundreds of points. 

# Javascript method
Therefore, I decided to use [Highcharts](http://www.highcharts.com/) for this purpose. The chart resulting can be found [here](http://raspi-pingouin.myftp.org/speedTest/highstock.html).

from subprocess import check_output
import time
import pandas as pd
import pygal
import datetime
import numpy as np

if __name__ == '__main__':

  # import for pygal because link with github fails
  pygal.Config.js.value = ('//kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js', 'pygal-tooltips.min.js')

  # load data
  df_data = pd.read_csv('speedResults.csv', header=None, names=["ts", "ping.value", "ping.unit", "download.value", "download.unit", "upload.value", "upload.unit"])
  # cast timestamp to date
  df_data["date"] = df_data["ts"].apply(lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%d-%m-%Y_%H:%M:%S'))

  # generate statistics
  ping_mean = np.mean(df_data["ping.value"])
  download_mean = np.mean(df_data["download.value"])
  upload_mean = np.mean(df_data["upload.value"])
  nb_values = len(df_data["ts"])


  ######## create evolution graph #######
  line_chart = pygal.Line(secondary_range=(0, 35), truncate_legend=17, legend_at_bottom=True, width=1200, show_x_labels=False) # set range for secondary axis, avoid truncate legend, set width, don't show x labels
  line_chart.title = 'Speedtest'
  line_chart.x_title = "Date"
  line_chart.y_title = "Duration (" + df_data["ping.unit"][0] + ")"
  line_chart.x_labels = df_data["date"].values

  # add data
  line_chart.add("Ping", df_data["ping.value"], dots_size=1.5)
  line_chart.add("Download (" + df_data["download.unit"][0] + ")", df_data["download.value"], secondary=True, dots_size=1.5) # bind to a second y_axis
  line_chart.add("Upload (" + df_data["upload.unit"][0] + ")", df_data["upload.value"], secondary=True, dots_size=1.5) # bind to a second y_axis

  # add means
  # create length(df_data["date"].values) points with value "mean" and draw without dot

  line_chart.render_to_file('website/speedTestEvolution.svg')


  ##### create boxplots #####
  #------ ping boxplot ----
  box_plot = pygal.Box(box_mode="tukey")
  box_plot.title = "Ping boxplot"
  box_plot.add("Ping", df_data["ping.value"])
  box_plot.render_to_file("website/pingBoxplot.svg")

  #------ download/upload boxplot ----
  box_plot = pygal.Box(box_mode="tukey")
  box_plot.title = "Download/upload boxplot"
  box_plot.add("Download", df_data["download.value"])
  box_plot.add("Upload", df_data["upload.value"])
  box_plot.render_to_file("website/downUploadBoxplot.svg")

  ###### display #####
  print "nb values: %s" % nb_values
  print "ping mean: %s" % ping_mean
  print "download mean: %s" % download_mean
  print "upload mean: %s" % upload_mean

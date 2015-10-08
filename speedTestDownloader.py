from subprocess import check_output
import time
import datetime
import sys

if __name__ == '__main__':

  # get the path to save the results
  resultsPath = sys.argv[1]

  # get data from speed-test server
  try:
    allString = check_output(["speedtest-cli", "--simple", "--server", "6027"]).replace(":", "")

    strings = allString.split("\n")
    strings.pop() # remove last void string

    results = {}
    for string in strings:
      splits = string.split(" ")
      value = min(float(splits[1]), 500)
      results[splits[0].lower()] = {
        "value": value}

    results["ts"] = time.time() # get timestamp

    # ts, ping.value, ping.unit, download.value, download.unit, upload.value, upload.unit
    stringResults = "%s,%s,%s,%s\n" % (results["ts"], results["ping"]["value"], results["download"]["value"], results["upload"]["value"])

    # save results in a file
    with open(resultsPath, "a") as myfile:
      myfile.write(stringResults)
  except Exception, e:
    print"error: %s at %s" % (e, datetime.datetime.now())

from subprocess import check_output
import time
import datetime

if __name__ == '__main__':

  resultsPath = "speedResults.csv"

  # get data from speed-test server
  try:
    allString = check_output(["speedtest-cli", "--simple", "--server", "6027"]).replace(":", "")

    strings = allString.split("\n")
    strings.pop() # remove last void string

    results = {}
    for string in strings:
      splits = string.split(" ")
      results[splits[0].lower()] = {
        "value": float(splits[1]),
        "unit": splits[2]}

    results["ts"] = time.time() # get timestamp

    # ts, ping.value, ping.unit, download.value, download.unit, upload.value, upload.unit
    stringResults = "%s,%s,%s,%s,%s,%s,%s\n" % (results["ts"], results["ping"]["value"], results["ping"]["unit"], results["download"]["value"], results["download"]["unit"], results["upload"]["value"], results["upload"]["unit"])

    # save results in a file
    with open(resultsPath, "a") as myfile:
      myfile.write(stringResults)
  except Exception, e:
    print"error: %s at %s" % (e, datetime.datetime.now())

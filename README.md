# IFTTT Applet Helpers

## Calculate average number of hours worked per day
_Date written: 1/28/2017_

`hours_worked.py` reads a CSV in the following format ...
```
Arrived at work,    "December 22, 2016 at 08:07AM"
Left work,          "December 22, 2016 at 04:54PM"
Arrived at work,    "January 03, 2017 at 08:53AM"
Left work,          "January 03, 2017 at 04:59PM"
```

... and computes the average number of hours worked each day. The calculation
    excludes time windows shorter than one hour to reduce outliers.

Designed to work with [this IFTTT applet](https://ifttt.com/applets/YuG24Anb-track-in-a-google-spreadsheet-when-you-arrive-and-leave-work).
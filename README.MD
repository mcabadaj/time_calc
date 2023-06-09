# Time Calculator

A simple Python script to calculate time since and until a certain point in time

## Arguments

This script can be run from the CLI with the following arguments:

```py time_calc.py [start] [end]```

- start time: By entering the start time you will get the time elapsed since then
- end time: By entering the end time you will get the time until then

## Time Format

The entered times have to be be in 24h format, with hours and minutes optionally separated by a colon (`HH:MM`).
When less than 2 digits are entered, it will be parsed to full hours.


## Output

The output is formatted as follows:

`[start time] - ([time since start]) - [current time] - ([time until end]) - [end time]`  
`Total: [total time from start to end]`

```
13:25 - (4:47) - 18:12 - (0:48) - 19:00
Total: 5:35
```
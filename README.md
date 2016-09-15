# YR.no API wrapper

*Wrapper for the YR.no API, for near time weather prediction.*

## Installing

```
pip install yr
```

## Using

### Locations
Locations are defined by Geonames, not coordinates:

**Example**

 - `United_States/California/San_Jose`
 - `Sweden/Södermanland/Himlinge`

### Periods

Each 24 hours consists of four periods(0-3):
 - 0: 00-06
 - 1: 06-12
 - 2: 12-18
 - 3: 18-24

### Code

Retrieving the weather description for a specific period:
```
yr = YR('Sweden/Södermanland/Himlinge')
print(yr.getPeriodWeather(1))
```
`partly cloudy`

Retrieving the weather description for the current period:
```
yr = YR('Sweden/Södermanland/Himlinge')
print(yr.getCurrentWeather())
```
`partly cloudy`

Retrieving temperature for a specific period:
```
yr = YR('Sweden/Södermanland/Himlinge')
print(yr.getPeriodTemperature(1))
```
`17`

Retrieving temperature for the current period:
```
yr = YR('Sweden/Södermanland/Himlinge')
print(yr.getCurrentTemperature())
```
`22`

## Attribution and Terms of Use

You should read and understand the [YR.no terms of use](http://om.yr.no/verdata/vilkar/) which is only available in Norwegian...

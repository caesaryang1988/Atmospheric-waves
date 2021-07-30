# Extrem Weather and Atmospheric-waves

## bakcground
Midlatitude extreme weather such as hurricanes, floods, heat waves, wildfires can cause catestrophic economic loss as well as social impacts. Therefore, predicting these extreme events is essential. It is well documented in the literature that midlatitude extreme weather events, albeit their inherent meso-synoptic scale, are closely related to planetary-scale atmospheric wave patterns. Here we present a case study of heavy precipitation over U.S east in Feburary 2020 that caused floods in Kentucky (https://en.wikipedia.org/wiki/Southeast_Kentucky_floods_of_2020) using Python libraries.

## Dataset
There are mainly two fields we are particularly interested: one is precipitation, and the other is atmospheric wave pattern.

- precipitation: we use 6-hour total precipitation from ERA-5 reanalysis during 2020-02-01_00Z to 2020-02-15_18Z.
- atmospheric wave pattern: we use potential vorticity (PV) at 300 hPa from ERA-5 reanalysis for preliminary analysis as well as subsequent calculations of local wave activity (LWA).

## Python codes
The Python codes here wrapped up analysis in planned three stages.

- stage A: exploratory analysis on the relation between precipitation and atmospheric wave pattern (denoted by PV) during the Kentucky flood event.

From our preliminary analysis, it is shown that atmospheric wave pattern over central U.S. differ significantly between days with heavy precipitation in the Eastern U.S. and days without, see below.
![Image on 2020-02-03_00Z]
(https://github.com/caesaryang1988/Atmospheric-waves/blob/main/tp-pv_2020-02-03_00Z.pdf)
![Image on 2020-02-06_12Z]
(https://github.com/caesaryang1988/Atmospheric-waves/blob/main/tp-pv_2020-02-06_12Z.pdf)

Moreover, there is a clear correlation between rainfall over Eastern U.S. and atmospheric wave patterns over central U.S., see below.

![Image on tp-pv correlation]
(https://github.com/caesaryang1988/Atmospheric-waves/blob/main/tp-pv_ts.pdf) 
- stage B (in progress): calculating LWA and monitor the lifecycle of planetary Rossby waves including wave generation, propagation and break up, and discussing potential impact on precipitation forecast.
- stage C (in progress): revisiting the problem for long-range climate data. Explore possibility of identify LWA using computer vision.

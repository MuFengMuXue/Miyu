# Extensions / Libxt RATEEST

The RATEEST target collects statistics, performs rate estimation calculation and saves the results for later evaluation using the **rateest** match.

**--rateest-name** *name*
Count matched packets into the pool referred to by *name*, which is freely choosable.

**--rateest-interval** *amount*{**s**\|**ms**\|**us**}
Rate measurement interval, in seconds, milliseconds or microseconds.

**--rateest-ewmalog** *value*
Rate measurement averaging time constant.

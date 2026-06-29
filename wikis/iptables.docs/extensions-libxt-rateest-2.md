# Extensions / Libxt Rateest

The rate estimator can match on estimated rates as collected by the RATEEST target. It supports matching on absolute bps/pps values, comparing two rate estimators and matching on the difference between two rate estimators.

For a better understanding of the available options, these are all possible combinations:

Absolute:
- **rateest** *operator* **rateest-bps**

- **rateest** *operator* **rateest-pps**

Absolute + Delta:
- (**rateest** minus **rateest-bps1**) *operator* **rateest-bps2**

- (**rateest** minus **rateest-pps1**) *operator* **rateest-pps2**

Relative:
- **rateest1** *operator* **rateest2** **rateest-bps**(without rate!)

- **rateest1** *operator* **rateest2** **rateest-pps**(without rate!)

Relative + Delta:
- (**rateest1** minus **rateest-bps1**) *operator* (**rateest2** minus **rateest-bps2**)

- (**rateest1** minus **rateest-pps1**) *operator* (**rateest2** minus **rateest-pps2**)

**--rateest-delta**
For each estimator (either absolute or relative mode), calculate the difference between the estimator-determined flow rate and the static value chosen with the BPS/PPS options. If the flow rate is higher than the specified BPS/PPS, 0 will be used instead of a negative value. In other words, "max(0, rateest#\_rate - rateest#\_bps)" is used.

\[**!**\] **--rateest-lt**
Match if rate is less than given rate/estimator.

\[**!**\] **--rateest-gt**
Match if rate is greater than given rate/estimator.

\[**!**\] **--rateest-eq**
Match if rate is equal to given rate/estimator.

In the so-called "absolute mode", only one rate estimator is used and compared against a static value, while in "relative mode", two rate estimators are compared against another.

**--rateest** *name*
Name of the one rate estimator for absolute mode.

**--rateest1** *name*
**--rateest2** *name*
The names of the two rate estimators for relative mode.

**--rateest-bps** \[*value*\]
**--rateest-pps** \[*value*\]
**--rateest-bps1** \[*value*\]
**--rateest-bps2** \[*value*\]
**--rateest-pps1** \[*value*\]
**--rateest-pps2** \[*value*\]
Compare the estimator(s) by bytes or packets per second, and compare against the chosen value. See the above bullet list for which option is to be used in which case. A unit suffix may be used — available ones are: bit, \[kmgt\]bit, \[KMGT\]ibit, Bps, \[KMGT\]Bps, \[KMGT\]iBps.

Example: This is what can be used to route outgoing data connections from an FTP server over two lines based on the available bandwidth at the time the data connection was started:

\# Estimate outgoing rates

iptables -t mangle -A POSTROUTING -o eth0 -j RATEEST --rateest-name eth0 --rateest-interval 250ms --rateest-ewma 0.5s

iptables -t mangle -A POSTROUTING -o ppp0 -j RATEEST --rateest-name ppp0 --rateest-interval 250ms --rateest-ewma 0.5s

\# Mark based on available bandwidth

iptables -t mangle -A balance -m conntrack --ctstate NEW -m helper --helper ftp -m rateest --rateest-delta --rateest1 eth0 --rateest-bps1 2.5mbit --rateest-gt --rateest2 ppp0 --rateest-bps2 2mbit -j CONNMARK --set-mark 1

iptables -t mangle -A balance -m conntrack --ctstate NEW -m helper --helper ftp -m rateest --rateest-delta --rateest1 ppp0 --rateest-bps1 2mbit --rateest-gt --rateest2 eth0 --rateest-bps2 2.5mbit -j CONNMARK --set-mark 2

iptables -t mangle -A balance -j CONNMARK --restore-mark

We see a lot of numbers being dialled. These numbers are dialled from a telephone which uses **DTMF (Dial Tone Multi Frequency)**.
First we extract the numbers which were dialled (the keys which were pressed). We use `multimon-ng` or any DTMF demodulator tool which returns the keys
```11631400670740375753322763532480716737685517086473090911690760345257334690167165```

```from Crypto.Util.number import long_to_bytes as lb
print(lb(11631400670740375753322763532480716737685517086473090911690760345257334690167165))
```

which gives us the flag.



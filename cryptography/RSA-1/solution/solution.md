# RSA - 1

# Challege

I have a lot of big numbers. Here, have a few!

```text
Ever used RSA Encryption?

cyphertext = 10400286653072418349777706076384847966640064725838262071
n = 23519325203263800569051788832344215043304346715918641803
e = 71
```

## Solution

1. Let p and q be the prime factors of n such that p \* q = n. P and Q can be found by factorizing n
   ```python
   p = 5051525354555657585960616263
   q = 4655885807254867892895911581
   ```
2. Let phi be equal to (p-1) \* (q-1). The value of phi is
   ```python
   >>> phi = (p-1)*(q-1)
   >>> phi
   23519325203263800569051788822636803881493821237062113960
   ```
3. Now that we have e and phi, we can calculate the decryption exponent (d)
   ```python
   >>> e = 71
   >>> d = pow(e,-1,phi)
   >>> d
   8943968739269332610766173214242164856342720752122212351
   ```
4. Plaintext decimal can now be calculated using the formula: plaintext = (cyphertext ^ d) % n
   ```python
   >>> cyphertext = 10400286653072418349777706076384847966640064725838262071
   >>> plaintext = pow(cyphertext, d, n)
   >>> plaintext
   9621269132073872010525638902903988134500010392708266109
   ```
5. convert plaintext number to hex code, and then to plaintext flag

### flag = dsc{t00_much_m4th_8898}

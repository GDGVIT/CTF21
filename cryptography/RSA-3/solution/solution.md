# RSA - 3

## Challenge

Alright, this is the big leagues. You have someone's Public Key. This isn't unusual, if you want to send someone an encrypted message, you have to have thier public key. Your job is to evaluate this public key, and obtain the value of the secret exponent or decryption exponent (The value of "d" in an RSA encryption).

Wrap the number that you find with dsc{\<number\>}!

[mykey.pub](mykey.pub)

## Solution

Solution:

1. Open the file, and you find the base64 encoded public key. RSA public keys are made of two components, the value of the encryption exponent, and the value of modulus. With these values, it's theoretically possible to figure out the value of d, so lets first extract these numbers from the public key

2. Using openssl tools we can extract these numbers with this command

   ```text
    openssl rsa -pubin -in mykey.pub -text -noout
   ```

   The output shows the values of modulus and exponent in hexadecimal.<br>
   <img src="solution_imgs\rsa-3-1.png" alt="drawing" width="300"/><br>
   Convert the hex values into decimal and now you have

   ```text
   e = 36222680858414256161375884602150640809062958718117141382923099494341733093172587117165920097285523276338274750598022486976083511178091392849986039384975758609343597548039166024042264614496506087597114091663955133779956176941325431822684716988128271384410010471755324833136859652978240297120618458534306923558546176110055737233883129780378153307730890915697357455996361736492022695824172516806204252765904924281272883818154621932085365817823019773860783687666788095035790491006333432295698178378520444810813882117817329847874531809530929345430796600870728736678389479159328119322587647856274762262358880664585675219093
   n = 64064959164923876064874945473407049985543119992992738119252749231253142464203647518777455475109972581684732621072998898066728303433300585291527582979430276357787634026869116095391514311111174206395195817672737320837240364944609979844601986221462845364070396665723029902932653368943452652854174197070747631242101084260912287849286644699582292473152660004035330616149016496957012948833038931711943984563035784805193474921164625068468842927905314268942153720078680937345365121129404384633019183060347129778296640500935382186867850407893387920482141216498339346081106433144352485571795405717793040441238659925857198439433
   ```

3. The value of e and n look way too big to factorize or calculate d with. This might be problematic, but RSA encryption has an exploit called the [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack), that looks like it could be applied to this RSA encryption

4. Searching online, you come across [an implementation](https://github.com/pablocelayes/rsa-wiener-attack.git) of this vulnerablility in a python program. Making a slight modification of the code lets you print the value of d.

   ```python
   import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

   def hack_RSA(e,n):
       '''
       Finds d knowing (e,n)
       applying the Wiener continued fraction attack
       '''
       frac = ContinuedFractions.rational_to_contfrac(e, n)
       convergents = ContinuedFractions.convergents_from_contfrac(frac)

       for (k,d) in convergents:

           #check if d is actually the key
           if k!=0 and (e*d-1)%k == 0:
               phi = (e*d-1)//k
               s = n - phi + 1
               # check if the equation x^2 - s*x + n = 0
               # has integer roots
               discr = s*s - 4*n
               if(discr>=0):
                   t = Arithmetic.is_perfect_square(discr)
                   if t!=-1 and (s+t)%2==0:
                       print("Hacked!")
                       return d

   # TEST functions
   if __name__ == "__main__":
       n = int(input())
       e = int(input())
       d = hack_RSA(e,n)
       print(d)
   ```

   <img src="solution_imgs\rsa-3-2.png" alt="drawing" width="1000"/><br>

5. Copy the number, wrap it with dsc{}, and you've got your flag

### flag: dsc{6393313697836242618414301946448995659516429576261871356767102021920538052481829568588047189447471873340140537810769433878383029164089236876209147584435733}

Useful links:
https://stackoverflow.com/questions/19850283/how-to-generate-rsa-keys-using-specific-input-numbers-in-openssl<br>
https://stackoverflow.com/questions/38401719/how-do-i-get-the-public-key-of-a-pem-file<br>
https://stackoverflow.com/questions/3116907/rsa-get-exponent-and-modulus-given-a-public-key<br>
https://github.com/pablocelayes/rsa-wiener-attack<br>

Commands used to create required files:

- openssl asn1parse -genconf config.txt -out newkey.der
- openssl rsa -in newkey.der -inform der -text -check
- openssl rsa -in privatekey.pem -pubout > mykey.pub

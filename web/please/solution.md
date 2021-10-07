# Please

## Challenge

Hi there! We used to work together back in our old company DEEMA. I recently had a problem with my computer and lost all the files on it. I remember creating a backup of my files on the company's servers. I know it's been a while, but could you please try to access those files? I would be very grateful!

## Solution

This challenge works on the basis of stages.

1. To get past the first stage, enter Clancy as username
2. To get past the second stage, change the cookie in your browser. Change Admin_access cookie to True
3. Change the request's User-Agent header to DeemaBrowser to get past this stage
4. Refer to [this](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) and make an authorization header, with the credentials as the base64 encoded passphrase

   ```text
   passphrase: What'sTheMagicWord?
   base64(passphrase): V2hhdCdzVGhlTWFnaWNXb3JkPw==
   ```

5. Add the Date header with any date on or before April of 2021.
6. The exact date is then given to you. Refer to [this](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date) for the format, and send the exact date. You get the flag in response.

### flag: dsc{4ll-y0u-g0tt4-d0-15-r3qu35t-n1c3ly}

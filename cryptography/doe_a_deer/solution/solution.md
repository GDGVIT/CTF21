# Doe, a deer

## Challenge

Mark, a very gifted musician, is suddenly missing after his music class. He is said to have been upset after turning in his assignment. He had worked very hard on it, it was his first original. Here, you can see his work. I'm sure you can find him, he wouldn't have gone far.

[Doe, a deer.df](Doe,_a_deer.pdf)

## Solution

1. Download all files
2. Use strings command on tune_700.mp3 to get [this link](https://drive.google.com/uc?export=download&id=1SR0Ztj6QpZlu39q28W0OBBDWJrDMTujB)
3. Download new file my_note.pdf using link
4. Exploring a little about music sheet encryptions brings you to solfa encryption
5. From the first (highlighted) line of the music sheet, we can obtain the Solfa key for the encryption <br>
   <img src="solution_imgs\doe_a_deer1.png" alt="drawing" width="500"/>
   ```
   Clef: Treble; Tonic: C; Mode: Major; Rythmic Unit: Eighth;
   ```
6. Now, we start counting the notes with respect to the rythmic unit of the solfa key, and end up with the following:
   c
7. After counting the notes, you are left with the following sequence
   ```
   R1 M1 F3 F1 T1 D3 D3 R4 F3 T1 F3 R1 M3 M1 T4 S1 M4 T1 D1 D1 T1 M4 T1 L3 R1 T4 S1 F3 R4 F3 T3 F1 R1 R3
   ```
8. Either using [this](https://wmich.edu/mus-theo/solfa-cipher/secrets/) website, or by using the picture below, you can decode the following sequence into letters<br>
   <img src="solution_imgs\doe_a_deer3.png" alt="drawing" width="200"/><br>
   ```
   Obtained plaintext: iamsorrymomihavegottogolivemymusic
   ```
9. Unlock the locked pdf using this plaintext as the password, and obtain flag in the pdf<br>
   <img src="solution_imgs\doe_a_deer4.png" alt="drawing" width="400"/><br>
   Flag: dsc{b3tt3r-b3-h0m3-f0r-d1nn3r}

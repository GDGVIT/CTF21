# Mike

## Challenge

Julia has come to you to ask for help. After spending too much time on his computer, Mike has gone insane, but no one knows why. Can you figure it out? Julia would really appreciate it. Here's how his desktop looked like. Weird how his system time doesn't change..

Wrap the flag that you find with dsc{\<flag\>}!

[desktop_wallpaper.png](desktop_wallpaper.png)

## Solution

The challenge refers to his system time, 1:16 AM, 4/9/20. Lets keep that for later.

As there is nothing obvious with the picture, lets explore its bit planes. On the green 0 bit plane, we see this.

<br><img src="solution_imgs/mike1.png" alt="drawing" width="800"/><br>

Wait! This looks like spotify codes! Wasn't spotify on the desktop? Open the scanner on your phone and scan the code. The song [Level of Concern - twenty one pilots](https://open.spotify.com/track/6xZ4Q2k2ompmDppyeESIY8?si=b2f5651039cf46ec) starts to play. The song is great, but we haven't found the flag yet. Morpheus, our good old friend, gives us the next clue, to check youtube. Search for [Level of Concern on Youtube](https://youtu.be/loOWKm8GW6A).

The release of this video is on 9th of April, 2020, same as on the system time! Let's go to 1:16 on the video. Turning on subtitles at this point gives you this.

<br><img src="solution_imgs/mike2.png" alt="drawing" width="800"/><br>

That looks totally out of place. Wrap it with dsc{}, and you've got the flag!

### flag: dsc{LOC-888-481-90TO?} or dsc{LOC-888-481-90TO}

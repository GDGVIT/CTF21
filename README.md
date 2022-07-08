<p align="center">
<a href="https://dscvit.com">
	<img width="400" src="https://user-images.githubusercontent.com/56252312/159312411-58410727-3933-4224-b43e-4e9b627838a3.png#gh-light-mode-only" alt="GDSC VIT"/>
</a>
	<h2 align="center">DeconstruCT.F 2021</h2>
	<h4 align="center">Repository of all Challenges made for CTF 2021</h4>
</p>

---
[![Join Us](https://img.shields.io/badge/Join%20Us-Google%20Developer%20Student%20Clubs-red)](https://dsc.community.dev/vellore-institute-of-technology/)
[![Discord Chat](https://img.shields.io/discord/760928671698649098.svg)](https://discord.gg/498KVdSKWR)


## Features
- [x]  Contains challenges for the CTF in 2021 with solutions
- [x]  CI/CD pipelines to autodeploy challenges once pushed
- [x]  Source Code, attachments and dependency files

<br>

Tips: [How to run a CTF](https://github.com/pwning/docs/blob/master/suggestions-for-running-a-ctf.markdown)

## Commit convention

- `add-<challenge_name>-<difficulty_level>-<domain>`: Adding
- `modify-<challenge_name>-<difficulty_level>-<domain>: ShortDescriptionAboutTheChangeMade`: Modifying
- `remove-<challenge_name>-<difficulty_level>-<domain>: ReasonForRemoving`: Removing
- `add-<challenge_name>-<difficulty_level>-<domain>: deployment`: Adding deployment config for the challenge

## Creating a challenge

1. Copy the `template` folder and its contents, rename it and put it into the correct category folder

``` 
$ cp -r template web/my-example-web-challenge
```

2. Add a description, flag and other information to the `README.md` of the challenge

``` 
$ vim web/my-example-web-challenge/README.md
# ... (change the README)
```

What you have to put in the README are

    1. Title
    2. Description
    3. Additional notes for the participants
    4. Flag (for CTF team)
    5. Notes for the CTF team (how to deploy or set up the environment for the challenge)

3. Add files, executables, etc. (**Important**: Don't forget to add a solution for it, preferrably code, otherwise add a `solution.txt` file)
4. Update the `challenge.yml` file

**Note**: Use Variable `IP_ADDRESS` in `challenge.yml` where the IP needs to be replaced by the server IP

## Dockerize Challenge

**Note**: Only needed for challenges that require server or that are needed to be hosted

1. Create a `Dockerfile`
2. `docker build` and `docker run` to make sure your container works
3. Update the `docker-compose.yml` in the root folder to include your challenge
    - Incase more than one container is needed create a new network
    - Incase persisting data is needed use volumes
4. Make sure not to use same outer port as some other challenge

## Deploying to CTFd

1. Install `ctfcli` and initialize it

```
$ pip install ctfcli && ctf init
```

2. Add your challenge
```
$ ctf challenge install crypto/my-crypto-example-chall
```

3. Sync/Update challenge
```
$ ctf challenge sync crypto/my-crypto-example-chall
```

4. Sync / Install all challenges in the repo
```
$ ./autosync.sh
```

## Testing a challenge

1. Go to the challenge's directory

``` 
$ cd web/my-exmaple-web-challenge
```

2. Open up the `README.md` and read it carefully (**Important**: Don't look at the solution until you've tried the challenge first!)

3. Setup the environment (if need be)

4. Try to solve the challenge

5. Give feedback to the author of the challenge
    1. Are there bugs, security issues (that could cause harm to the CTF platform) or incorrect files provided?
    2. Is the description clear?
    3. Is the challenge too guessy?
    4. How hard was it for you to solve it? (subjective)
    5. Overall, did you find it fun? (subjective)

## Setting up CTFd

1. Clone CTFd
```
$ git clone https://github.com/CTFd/CTFd.git
```

2. Start CTFd in background
```
$ docker-compose up -d
```
## Contributors

<table>
	<tr align="center">
		<td>
		Vishesh Bansal
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/22132836?v=4" width="150" height="150" alt="Vishesh Bansal">
		</p>
			<p align="center">
				<a href = "https://github.com/VisheshBansal">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
			</p>
		</td>
        <td>
		Krishap S
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/49953521?v=4" width="150" height="150" alt="Krishap S">
		</p>
			<p align="center">
				<a href = "https://github.com/Krishap-S">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
			</p>
		</td>
        <td>

Mayank Kumar

<p  align="center">

<img  src = "https://dscvit.com/images/techteam/mayank.jpg"  width="150"  height="150"  alt="Mayank Kumar">

</p>

<p  align="center">

<a  href = "https://github.com/mayankkumar2">

<img  src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg"  width="36"  height = "36"  alt="GitHub"/>

</a>

</p>

</td>
		<td>
		Krish Chatterjie
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/71811415?s=460&u=08d3940b7ee0105037b88175319ba7f09f83b159&v=4" width="150" height="150" alt="Krish Chatterjie">
		</p>
			<p align="center">
				<a href = "https://github.com/KrishChatterjie">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
			</p>
		</td>
        </tr>
        <tr align="center">
                <td>
		Anish R.
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/49672329?v=4" width="150" height="150" alt="Anish R">
		</p>
			<p align="center">
				<a href = "https://github.com/z404">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
			</p>
		</td>
                        <td>
		Rithik Jain
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/12408595?v=4" width="150" height="150" alt="Rithik Jain">
		</p>
			<p align="center">
				<a href = "https://github.com/rithikjain">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
			</p>
		</td>
	</tr>
</table>

<p align="center">
	Made with :heart: by <a href="https://dscvit.com">GDSC-VIT</a>
</p>

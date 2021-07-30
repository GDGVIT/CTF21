# DSC-CTF 21

Tips: [How to run a CTF](https://github.com/pwning/docs/blob/master/suggestions-for-running-a-ctf.markdown)

Link to Challenge ideas: 

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

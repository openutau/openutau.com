# Compiling OpenUtau from source
Compiling OpenUtau can be done easily.

## Prerequisites
You will need the .NET 6.0 SDK.

For Windows and Mac you can get it [here](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

On Ubuntu, Debian, or any derivatives (e.g. Linux Mint):
```
sudo apt install dotnet-sdk-6.0
```
On an Arch-based distro:
```
sudo pacman -S dotnet-sdk
```
For other instructions see the link above.

You will also neet Git.
[Windows](https://git-scm.com/download/win) | [Mac](https://git-scm.com/download/mac) | [Linux](https://git-scm.com/download/linux)

## Cloning and building
Once you have the prerequisites set up, run the following command to clone the repository

```
git clone https://github.com/stakira/OpenUtau.git
```

Once the clone is complete, navigate to the directory via command line

```
cd OpenUtau
```

And finally, to compile, run the following commands:

```
dotnet restore OpenUtau

dotnet build OpenUtau
```

The executable files will be in the directory `OpenUtau/OpenUtau/bin/Debug/net6.0`
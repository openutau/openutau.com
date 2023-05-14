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

## Download source code
Once you have the prerequisites set up, run the following command to clone the repository

```
git clone https://github.com/stakira/OpenUtau.git
```

## Building in Visual Studio
Visual Studio is an IDE for .NET that supports Windows and MacOS.

Download and install Visual Studio Community 2022 from [Visual Studio Official Website](http://visualstudio.microsoft.com/). Choose ".NET Desktop Development" workload when installing.

Open "OpenUtau.sln" with Visual Studio.

Choose "OpenUtau" and click the green ▶ icon to run.

## Building in Visual Studio Code
Visual Studio Code (aka. VSCode) is a lightweight code editor that supports Windows, MacOS and Linux. 

Download and install VSCode from [VSCode official website](http://code.visualstudio.com/)

Launch VSCode, search and install the C# extension.

![image](https://github.com/stakira/OpenUtau/assets/54425948/354dd290-68c5-4d14-91a0-bd89bb76e71d)

Open the directory where you've downloaded the source code of OpenUtau and open any .cs file. A notification saying "Required assets to build and debug are missing from 'OpenUtau'. Add them?" will pop up. Click "Yes".

![image](https://github.com/stakira/OpenUtau/assets/54425948/dc2dd305-4d87-482c-8a3f-9d4056751fad)

Open `.vscode/launch.json`, change the "OpenUtau.dll" to the executable file name on your OS, like "OpenUtau.exe" on windows.

![image](https://github.com/stakira/OpenUtau/assets/54425948/8d3b4ba1-c4ea-4a1c-8f7a-918e05c9afaf)

Click "Run → Start Debugging"

## Building from command line

Navigate to the directory via command line

```
cd OpenUtau
```

And finally, to compile, run the following commands:

```
dotnet restore OpenUtau

dotnet build OpenUtau
```

The executable files will be in the directory `OpenUtau/OpenUtau/bin/Debug/net6.0`
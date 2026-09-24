# Compiling OpenUtau from source
Compiling OpenUtau can be done easily.

## Prerequisites
You will need the .NET 8.0 SDK.

For Windows and Mac you can get either [here](https://dotnet.microsoft.com/en-us/download/dotnet)

On Ubuntu, Debian, or any derivatives (e.g. Linux Mint):

```
sudo apt install dotnet-sdk-8.0
```
On an Arch-based distro:
```
sudo pacman -S dotnet-sdk
```
For other instructions see the link above.

You will also need Git.
[Windows](https://git-scm.com/download/win) | [Mac](https://git-scm.com/download/mac) | [Linux](https://git-scm.com/download/linux)

## Download source code
Once you have the prerequisites set up, run the following command to clone the repository

```
git clone https://github.com/stakira/OpenUtau.git
```

## Building in Visual Studio
Visual Studio is an IDE for .NET that supports Windows.

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

## Building in GitHub Codespaces
GitHub Codespaces is an online linux environment provided by GitHub with a vscode webui. Users can access to GitHub Codespaces from any device with a browser.

On OpenUtau's repo page, click "Code → Codespaces → +"

![image](https://github.com/stakira/OpenUtau/assets/54425948/6063718d-a77b-47a7-b2d2-4cd0a043eef2)

Open any .cs file under the `OpenUtau` folder, and click the Debug button

![image](https://github.com/stakira/OpenUtau/assets/54425948/330c8926-a425-40e8-bd14-5354ed1c1766)

Ports → Add Port → input `6080` → Open In Browser

![image](https://github.com/stakira/OpenUtau/assets/54425948/136aad0a-affe-45aa-bde8-cf37325e3696)

In the noVNC page poped up, connect → input `vscode`

![image](https://github.com/stakira/OpenUtau/assets/54425948/b6510a2f-7e4b-4742-b6bc-d3629283dcc7)

Successfully connected to the remote desktop of GitHub Codespaces.

![image](https://github.com/stakira/OpenUtau/assets/54425948/3a0569da-bf01-4203-9af7-b7a7220ec7e8)

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

## Building worldline
Worldline is the C++ part of OpenUtau.
1. Install Bazelisk
2. In the command line, `cd` to the `cpp` folder
3. Run `bazelisk build //worldline` to build .dll on Windows, .dylib on macOS or .so on Linux.
You can also run `bazelisk build //worldline:main` to build a executable version, though curve expressions won't be available.

Notes:
- On Windows omits // in commands.
- Recommends Visual Studio Code to leverage IntelliSense.
- If Bazel ever freezes on Windows, open up Task Manager and kill the Java process.
- `bazelisk clean` cleans up build cache.
- `bazelisk clean --expunge` cleans up build cache and dependencies.

### Debugging worldline in visual studio
1. Build worldline with `bazelisk build worldline -c dbg`
2. Copy the compiled dll and pdb (in `<path to your openutau repo>\cpp\bazel-out\x64_windows-dbg\bin\worldline`) into `runtimes\win-x64\native`
3. In visual studio, open OpenUtau.sln, right click on the OpenUtau project -> properties -> Debug -> Open debug launch profiles UI -> enable native code debugging
4. In visual studio, debug -> options -> debugging -> symbols, add `<path to your openutau repo>\cpp\bazel-out\x64_windows-dbg\bin\worldline`
5. run

## Testing pull requests from other developer
1. navigate to your openutau development folder
2. `git stash` to save any uncommitted changes
3. `git fetch https://github.com/{author}/OpenUtau {branch}; git checkout FETCH_HEAD`, replacing {author} and {branch} with the author and branch you want to test(e.g. git fetch https://github.com/lennyservant/OpenUtau improve-classic-pitch-timing; git checkout FETCH_HEAD)
4. open visual studio, build and run

You can find the author and branch name in the pull request on github, which usually have a line with the format author:branch just below the pull request title

After testing, you can switch back to your branch and pop/apply your stashed changes through visual studio (menu -> view -> git changes), or you can type `git checkout {branch}` to switch branches and `git stash pop` to pop stashed changes

## Developer Documentation
[DeepWiki](https://deepwiki.com/stakira/OpenUtau/1-overview)  

**DeepWiki is not automatically updated, so please update it yourself as needed.**


# PIR – BLE Frequency Analyzer

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/PIR-IDS/ble-frequency-analyzer">
    <img src="https://avatars.githubusercontent.com/u/99486891" alt="Logo" width="130">
  </a>

  <p align="center">
    IDS: Code analyzing BLE advertising emissions frequency of surrounding objects 
    <br />
    <a href="https://github.com/PIR-IDS/ble-frequency-analyzer/releases"><strong>See Releases »</strong></a>
    <br />
    <br />
    <a href="#">Research Paper</a>
    ·
    <a href="https://github.com/PIR-IDS/ble-frequency-analyzer/actions/workflows/test.yml">Test Results</a>
    ·
    <a href="https://github.com/PIR-IDS/ble-frequency-analyzer/projects">Show Project</a>
  </p>
  
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#execution">Execution</a></li>
      </ul>
    <li><a href="#tree-structure">Tree Structure</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>

***

<!-- ABOUT THE PROJECT -->
## About The Project

This code will be used in order to study the different ways to detect BLE attacks.  

### Built With
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install the latest version of pyenv (https://github.com/pyenv/pyenv-installer [ UNIX ], https://pyenv-win.github.io/pyenv-win/ [ WINDOWS ]) or update it with the following command:
  ```sh
  pyenv update
  ```
* Install the latest version of pipenv (https://pipenv.pypa.io/) or update it with the following command:
  ```sh
  pip install pipenv --upgrade
  ```
  
### Installation

1. Clone the project
   ```sh
   git clone https://github.com/PIR-IDS/ble-frequency-analyzer.git
   ```
2. Install the dependencies by typing the following command while being in the project root:
   ```sh
   pipenv install --dev
   ```
> :warning: **If you are using pyenv-win (WINDOWS)** : If you do not have the version of Python used in the project, it is possible that pipenv does not detect pyenv, preventing you from using it directly. To solve this problem, first install the desired version `pyenv install 3.10.0` and then instead of the above command use this one: `pipenv --python %USERPROFILE%\.pyenv\pyenv-win\versions\3.10.0\python.exe install --dev`
3. The project is now ready to run.

<!-- USAGE EXAMPLES -->
## Usage

The user can employ the four functions to obtains different informations from `<file_to_read>` situated in the `<folder>`. 

The function `calcul_frequency` return the BLE advertising emissions frequency of an object based on it `<mac_address>`.

The function `rssi_analyse` return the rssi of a BLE object at each advertising emission based on it `<mac_address>`.


### Execution

To use the functions, it is needed to modify the file using `print`.  
To execute the file, run the following instructions:
   ```sh
   pipenv run run 
   ```

<!-- TREE STRUCTURE -->
## Tree Structure
<details>

_TODO_

</details>

<!-- CREDITS -->
## Credits

Romain Monier [ [GitHub](https://github.com/rmonier) ] – Co-developer
<br>
Noé Chauveau [ [GitHub](https://github.com/Noecv) ] – Co-developer
<br>
Amélie Muller [ [GitHub](https://github.com/AmelieMuller) ] – Co-developer


<!-- CONTACT -->
## Contact

Project Link : [https://github.com/PIR-IDS/ble-frequency-analyzer](https://github.com/PIR-IDS/ble-frequency-analyzer)

Organization Link : [https://github.com/PIR-IDS](https://github.com/PIR-IDS)

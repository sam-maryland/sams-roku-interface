# Sam's Roku Interface

Ever get tired of using your remote or not being in control of what's on the TV? Then this app is for you! Sam's Roku Interface is a Python-based application that allows you to control your Roku devices from the Command Line.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes. 

### Prerequisites

First, you need to set up your workstation to communicate with your Roku device. Find the IP Address for your Roku device by navigating to Settings > Network > About. Make a note of your IP.

Next, export your IP address as an environment variable by running this command:

```
export ROKU_IP_ADDRESS='YOUR IP ADDRESS HERE'
```

The requirements.txt file is located in the 'sams-roku-interface' subdirectory.

```
pip install -r requirements.txt
```

To run the program:

```
python main.py
```

## Authors

* **Sam Maryland** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

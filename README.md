# CLI Website Blocker

The CLI Website Blocker is Python3-based utility designed to improve productivity by temporarily blocking access to specified websites. The program works by modifying the system's '**/etc/hosts**' file to redirect listed websites to the localhost (127.0.0.1) for a specified duration.


## Features

- Block multiple websites simultaneously.
- Specify the duration (in minutes) for the websites to be blocked.
- Automatically unblocks websites after the specified duration.
- Simple command-line interface for ease of use.


## Prerequisites

- Python 3.x installed on your machine.
- Administrative access to modify your ```/etc/hosts``` file.
- MacOS or Linux operating system.


## Installation

1. **Clone the repository**
Open a terminal and run the following command to clone the repository to your local machine:
```git clone https://github.com/aandrews72/website-blocker.git```

2. **Navigate to Directory Containing the Script**

3. **Make the Script Executable (Optional):**
Run this following command in your terminal:
```chmod +x main.py```

You're now ready to use the Website Blocker!

## Usage

To use the program, follow these steps:
1. **Prepare the list of websites to block:**
Edit the blocked_websites.txt file to include all websites to block only separate lines. Include the regular domain and 'www' subdomain. For example:

```
www.example.com 
example.com
```

2. **Run the script:**
Open a terminal and navigate to the directory containing the main.py file. Run the script with sudo and specify the blocking duration in minutes as an argument:

```sudo python3 main.py 60```

This would block the websites in the ```blocked_websites.txt``` file for 60 minutes.


## Troubleshooting

After the script has run or if you notice the changes aren't taking effect, you may need to flush your system's DNS cache. Refer to the "Flushing DNS Cache" section for the appropriate command for your operating system.


## Contributing

Contributions to this program are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue in this repository. 


## License

This project is licensed under the MIT license - see the LICENSE file for details.

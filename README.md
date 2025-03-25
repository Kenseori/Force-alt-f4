Force Alt+F4
-------------

Description:
The program terminates the active process and its child processes by pressing Alt+F4.
Exceptions for processes can be specified in the forcef4.ini file.
What is the difference from the others? It shuts down child processes and parent non-system processes, among other things. And it also works unlike the others!

Project Files:
1. forcef4.py - the main script of the program.
2. forcef4.ini file with exceptions.
3. requirements.txt - a list of libraries to install.

How to use:
1. Install dependencies:
pip install -r requirements.txt

2. Add exceptions to forcef4.ini (for example, explorer, steam).

3. Run the script:
python forcef4.py

4. To build the exe without the console, run the command:
pyinstaller --noconsole --onefile forcef4.py

Example of forcef4.ini:
-------------------

steam
chrome explorer

Requirements:
- Python 3.13 or higher
- Installed libraries from requirements.txt

# Password Checker

Python script to check if you passwords has been leaked or not.
To check if your passwords are safe or not run the script as following.

This script makes use of API from **_haveibeenpwned.com_**[https://haveibeenpwned.com]

Additional details of thE API used here can be found on page [https://haveibeenpwned.com/API/v3] with the title "Searching by range".

There are also additional APIs described on the webpage for other methods.

## How to run the script

**Step 1:** Create a txt file containing a list of passwords to check. The txt file should have separate passwords in separate lines.
Example txt file:<br>
_passwords.txt_

```
hello
hi
password
password123

```

**Step 2:** Save this file on the same directory as the one containing hte '_check_password.py_' script.

**Step 3:** Make sure that you have activate a virtual environment which satisfies the requirements written in the '_requirements.txt_' file. If such a virtual environment is not available create one and installed the requirements using '_requirements.txt_' file. Then activate it.

**Step 4:** Run the script as follows. Use the filename of your text file if it has been names something else than '_passwords.txt_'.

```
python check_password.py passwords.txt
```

**Step 5:** The result is printed in your terminal with count of how many times the password was found or leaked.

import hashlib
import os
import sys

import requests


def request_api_data(query):
    """
    Takes the first 5 characters of the SHA1 hash of a password and queries the pwned API and returns the response

    Args:
        query (str): first 5 characters of the SHA1 hash of a password

    Raises:
        RuntimeError: raised if error in fetching data.

    Returns:
        object: response object of pwned API.
    """
    url = f"https://api.pwnedpasswords.com/range/{query}"
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching data: {res.status_code}. Check the api and try again.")

    return res


def pwned_api_check(password):
    """
    Checks password if it exists in API response

    Args:
        password (str): password to check if it has been leaked

    Returns:
        int: returns count of number of times the password
    """
    sha1_hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first_5_char, tail = sha1_hashed_password[:5], sha1_hashed_password[5:]
    response = request_api_data(first_5_char)
    print(response)

    return get_password_leaks_count(response, tail)


def read_response(response):
    """
    Takes the response object from the pwned API and prints the text data of leaked passwords's SHA1 hash after the 5th character.

    Args:
        response (object): pwned API response object
    """
    print(response.text)


def get_password_leaks_count(response, hash_to_check):
    """
    Takes the response object from the pwned API and converts it to tuples of tail hashes 

    Args:
        response (object): pwned API response object
        hash_to_check (bool): tail string after the 5th character of the SHA1 hash of the password user entered

    Returns:
        int: returns count of number of times the password
    """
    hashes = (line.split(':') for line in response.text.splitlines())

    for h, count in hashes:
        # print(h, count, hash_to_check)
        if h == hash_to_check:
            return count

    return 0


def main(passwords_filename):
    """
    Takes one argument when running the file. Takes a argument filename which contains a list of password to check if it has been leaked, hacked or pawned, etc.
    Args:
        passwords_filename (str): filename of file containing list of passwords written in separate lines to check in the pwned API if it has been leaked.
    """
    print(passwords_filename)
    if not os.path.exists(passwords_filename) or os.path.getsize(passwords_filename) == 0:
        raise FileNotFoundError(
            f"File '{passwords_filename}' which should contain list of passwords separated by line-break to check is not found or is empty. Please create the file and enter passwords in it separated by line-break to check in it.")

    with open(file=passwords_filename, mode='r') as file:
        data = file.read()
        passwords_list = data.splitlines()
        print(passwords_list)

    for password in passwords_list:
        count = pwned_api_check(password)
        if count:
            print(
                f"`{password}` was FOUND {count} times... You should probably change your password.")
        else:
            print(f"`{password}` was NOT FOUND. No need to change password.")


if __name__ == "__main__":
    """
    Runs the following code only when this file is run directly.

    Example:
    if you have to check passwords has been leaked or not, run the file as:
    `python check_password.py [txt_filename].txt`
    where the [txt_filename].txt file has list of passwords.
    passwords are separated by line-breaks.
    """
    sys.exit(main(sys.argv[1]))

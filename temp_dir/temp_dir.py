import os
import argparse
import datetime
import win32clipboard

DEFAULT_TEMP_DIR = r'C:\Temp'
TOTALCMD_PATH = r'C:\totalcmd\totalcmd64.exe'


def copy_to_clipboard(text):
    """
    Copies the specified text to the clipboard
    :param text: The text to be copied
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()


def get_temp_directory_for_date(required_date=datetime.date.today(), temp_dir=DEFAULT_TEMP_DIR):
    """
    Returns the temp directory path for the given date
    :param required_date: The date to construct the temp directory for (Default: today)
    :param temp_dir: The base temp directory to use
    :return: The path of the temp directory
    """
    return os.path.join(temp_dir, required_date.strftime("%Y-%m-%d"))


def main():
    """
    Creates the temp directory and executes the desired script mode (Open / Copy path)
    """
    parser = argparse.ArgumentParser(
        description="Creates a temp directory with a format of the current date, opens it (in Total Commander) and / or copies its path to the clipboard.")
    parser.add_argument("-o", "--open", action="store_true", help="Open the directory after creation")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Copy the full directory path to the clipboard")
    parser.add_argument("-td", "--temp-dir", help="The base temp dir to use", default=DEFAULT_TEMP_DIR)

    args = parser.parse_args()

    temp_dir_path = get_temp_directory_for_date(temp_dir=args.temp_dir)

    if not os.path.exists(temp_dir_path):
        os.makedirs(temp_dir_path)

    if args.clipboard:
        copy_to_clipboard(temp_dir_path)

    if args.open:
        os.system(f'{TOTALCMD_PATH} "{temp_dir_path}"')


if __name__ == "__main__":
    main()

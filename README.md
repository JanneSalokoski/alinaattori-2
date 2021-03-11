# Alinaattori 2.0

Alinaattori 2.0 is a tool made for handling reservations of Alina-sali, a ballroom organizations operating under HYY, the Student Union of the University of Helsinki, can reserve for themselves.

## Getting started

These instructions will get you up and running with a local copy of alinaattori

### Prerequisites

Python 3 is needed to run Alinaattori 2.0. Instructions for installing Python on your system can be found on [www.python.org](https://www.python.org/).

While a program for viewing .csv-files is not strictly necessary for using Alinaattori 2.0, you might have to edit .csv-files. Output is also written into a .csv-file, so software capable of viewing them is required. [Microsoft Excel](https://www.office.com/), [Open Office Calc](https://www.openoffice.org/) and [Google Sheets](https://www.google.com/sheets/about/) are tools capable of outputting .csv-files. This document will give examples from Microsoft Excel. You can also use a plain-text -editor for writing and reading .csv-files, such as [Sublime Text](https://www.sublimetext.com/), Notepad or [vim](https://www.vim.org/). Using a plain-text -editor for handling .csv-files is probably the safest way of preserving file formats, but it might not be the easiest way for beginners. 

### Installing

Easiest way to acquire Alinaattori 2.0 is to clone this git-repository.

```
$ git clone https://github.com/JanneSalokoski/alinaattori-2.git
```

Or you can download the program from the [Releases-page](https://github.com/JanneSalokoski/alinaattori-2/releases). Download the archive and extract it into a directory you want to use Alinaattori 2.0 from.

Now you can run Alinaattori 2.0 from the command line. You can test your installation by running this command:

```
$ py .\alinaattori.py -s --no-output
```

If the command runs without errors, installation was succesfull.

## Usage

Alinaattori 2.0 is a python program you run using a command-line-interface. On Windows you can use Powershell or Command Prompt. On MacOS you can use the Terminal app or iTerm2. I hope everyone running linux already knows to use their terminal of choice, so I don't have to list my favourites (alacritty, urxvt).

### Windows

#### Acquiring input files

##### Input data

This file you will probably output from Lyyti, with some modifications. Generate a report consisting of organization name, contact-email, request one, two and three. Open the report in excel. Change the header rows into 'organization', 'email', '1', '2' and '3' respectively. Save the file as UTF-8 encoded CSV file `input.csv`. This option should be the first .csv-option in Excels file-type selection. 

You can also run `dev/generate_input.py` in order to generate some sample data for testing.

##### Email template

If you want to output emails, create a text file `email_template.txt`. Write a message you want to send to your recipients. Words `{organization}` and `{date}` will be replaced with the name of the organization, and the date reserved to them.

#### Running alinaattori.py

Open the start-menu, type run, press enter, write cmd and press enter again. A black window appears. Navigate to the directory you have alinaattori.py in file explorer and copy the directory path (for example `C:/Users/example/Documents/Alinaattori 2.0/`). Write cd into the command prompt window and press Ctrl+V. Press enter.

Now you can run Alinaattori 2.0 by running the following command:

```
$ py .\alinaattori.py 
```

If no errors appear in the Command Prompt, a new file called `output.csv` should have appeared in your Alinaattori 2.0 directory. Open it and see how the reservations came out.

### MacOS and linux

Really the process is the same on all of these operating system. You can follow the instructions for Windows, but use your systems terminal app and edit the .csv-files with what you have available.

#### Controlling the program

Alinaattori 2.0 can be customized by command line flags. Information on customizable options can be seen by running

```
$ py .\alinaattori.py -h
```

## Contributing

Feel free to create a new issue on GitHub if you feel there is a need for some new feature, or something needs fixing. If you can solve the problem yourself, a PR will likely get accepted.

## Authors

- Janne Salokoski <[@JanneSalokoski](https://github.com/JanneSalokoski)>

Alinaattori 2.0 is based on Alinaattori, a software written for the same purpose as Alinaattori 2.0 The original Alinaattori was written by someone for HYY, but it had broken and needed updating. Alinaattori 2.0 shares no code with the original Alinaattori.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/JanneSalokoski/alinaattori-2/blob/main/LICENSE.md) file for details
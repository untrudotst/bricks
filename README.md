CSV Processor
=============

This Python script processes a CSV file from rebrickable database.

-   List mode: Creates a new CSV file with one line for every part number and color ID with the highest quantity found. Optional argument: --include_spare to include spare parts.

-   Part mode: Returns the highest quantity found for a specific part number. Optional arguments: --part_id to filter by inventory ID, --color_id to filter by color ID, --include_spare to include spare parts.

Requirements
------------

-   Python 3.6 or higher

Usage
-----

1.  Download or clone the script from the repository.
2.  Download the latest [inventory_parts](https://rebrickable.com/downloads/) csv from rebrickable and place it in the same folder.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where the script is located.
4.  Run the script using one of the following commands:

### List mode

`python script.py file.csv list [--include_spare]`

-   Replace `file.csv` with the name of the CSV file (inventory_parts.csv).
-   The `--include_spare` flag is optional and can be added to include spare parts in the output.
-   The output file will be named `output.csv` and will be saved in the same directory as the script.

### Part mode

`python script.py file.csv part_num [--color_id COLOR_ID] [--include_spare]`

-   Replace `file.csv` with the name of your CSV file (inventory_parts.csv).
-   Replace `part_num` with the part number you're interested in.
-   Replace `COLOR_ID` with the color ID you're interested in (if you're filtering by color ID).
-   The `--include_spare` flag is optional and can be added to include spare parts in the output.
-   The output will be the highest quantity found for the specified part number (filtered color ID if specified).

License
-------

This script is licensed under the MIT License. Feel free to modify and distribute it as needed.

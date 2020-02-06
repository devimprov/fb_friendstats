# fb_friendstats
Scripts to process JSON data from Facebook and provide stats or whatever I feel like.

## Requires

Python 3.6 or greater. 

## How To get Friends List from Facebook
* Go to Settings> Your Facebook Information> Download Your Information> 
* Deselect All, Select Friends. 
* Change format from HTML to JSON in the dropdown. 
* Press Create File
* Wait a few minutes for Facebook to create file, you'll get a notification with download link. 
* Download the file and unzip
* Put script in the same directory as the script, or pass as first argument. 

## Running the script

To get list of the most common first names of your friends and how many of them have that name, run from the command line using Python 3. If you run the script with the friends.json file in the same folder you don't need to pass an argument. otherwise you can pass the location of the file as the first argument. 


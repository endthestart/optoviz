# optoviz
A module to track and visualize options/stock strategy payoffs. It uses a dataframe (holdings chart) to store dictionaries of metadata associated with securities and contracts held. The visualization functions can grab this info and dynamically visualize the payoffs, against the current price as well.

# Example
Please check out the jupyter notebook for an example of it in action!

# Development note
Currently in development - I will be adding more functionality, documentation, and improving/streamlining current functionality as I go on (OOP, efficiency, readthedocs, added/simplified functionality, more options strategies so they don't need to be coded out by hand.). I will admit - this is extremely rough right now. Of note you must create a (free) robinhood account, as the program interacts with their API to gather price data. I will change this to use yahoofinance or some other API which does not require a sign in soon.

# Current Dependencies
fast_arrow (and an associated robinhood account)
https://github.com/westonplatter/fast_arrow
pandas
numpy
seaborn
matplotlib

# Installation
Right now the two ways to use this module are to either clone it into a folder in the folder you are working in and import these functions directly, or alternately clone it into the file your python packages are held in and import it as you would any other module.



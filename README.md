# After Hours Trading Script
A significant body of research has gone into analyzing and understanding the significance of after hours trading. While it is certainly true that the vast majority of trades are done between 9:30-4 when the market is open, it is important not to overlook. As [Barclay and Hendershot (2003)](https://www.jstor.org/stable/1262737) note:
> The low trading volume after hours generates significant, albeit inefficient, price discovery. Individual trades contain more information after hours than during the day. Because information asymmetry declines over the day, price changes are larger, reflect more private information, and are less noisy before the open than after the close

This script and accompanying python file are meant as a data generation tool to do data research on after hours trading to get a better sense of its impact on the overall market.

Indeed, there exists many costly APIs which would enable someone to obtain after hours trading data including [Finhub](https://finnhub.io/) or [databento](https://databento.com/), which are particularly useful due to their ease of use and user-friendly downloading formats. The goal of this project was too as cost-efficient as possible, however, so I was lucky to identify [polygon.io](https://polygon.io/) which offers a free tier API which returns data in a JSON format.

## Using the script
1. To properly use the code, one first has to register an account on polygon.io above and create an account which gives them access to an **API Key**. Once you have this key it should input in the *stockdataimporter* script under the space "INSERT API KEY HERE".

2. One you have completed the script in this way, go the [Master Google Sheet](https://docs.google.com/spreadsheets/d/1AISbsv-6wl_Yd41V81a2f2ODq3WvCoTBtyZ6yKeb-0I/edit?usp=sharing) and make a copy.

3. Under extensions press 'Apps Scripts' which should open up a IDEesc environment. Copy into this space your script with API key and press the save icon

4. Now you should be able to return to the main page of the Google Sheet, refresh the page, and input the stocks, dates, and whether you would like pre-market data (7-8 AM), after-market close data (4-5) or simply data for the entire day. Note to follow the example structure provided exactly for proper resulted and that the Polygon.io API is rate limited to 5 calls per minute, so it will pause for a minute after every 5 calls before continuing.

5. Once all the stocks you would like have been input go up to the 'Stock Data' tab (which should be right next to the 'Help' button and on the same line as 'File' and 'Edit'). Press the 'Import Stock Data' button and allow the script to run. All your data should be returned in a flat spreadsheet titled 'Results'
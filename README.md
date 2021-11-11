# House Rocket

<img src = "images/small logo.jpg" alt="Drawing" style="width: 250px;"/>

## House Rocket Company

**House Rocket** is a buy and sells houses enterprise based in Seattle. Their business model is to buy houses and sell them for a higher price, sometimes renovating the acquired house before selling to maximize their value. Hence, the business core is finding undervalued properties and selling them for a higher price. 

## Business Problem

As the main business is to buy and sell houses, their main problems are: 

* Determinate the undervalued houses;
* What should be the selling price; 
* When should they to sell it;

In order to solve these problems we will create premisses to analyze if a house is undervalued and for how much it should be sold. A analysis of the best period to sell the houses will also be made. 

## Project Scope and Premisses

The initial part of the job is to analyze the available houses in the database provided by House Rocket and determine which are the best business prospects. To organize the opportunities, we will use the BCG matrix (or growth-share matrix) to scale the importance of the business opportunity. 

<img src = 'images/BCG Matrix.png' style = 'width: 500px;'/>

Below follows the description of each classification and which type of house will be in each:  

* **Cash Cows:** This product requires little investment and generates cash that can be utilized for investment in other business units. These are the corporation's key source of cash and are specifically the core business. We will consider that houses with the following characteristics are our Cash Cows: 
 * Houses with good conditions that are in the first quantile of price in their region.
 * Houses with waterfront and good conditions that are in the first quantile of price.
 
* **Stars:**  These products require large investment but also provide large rentability. We will consider that houses with the following characteristics are our Stars:
 * Houses with waterfront in bad condition will require renovation before being sold. We will assume that the renovation cost will be 10% of the house value.
 * Houses with waterfront and grade 11 and 12. We will assume that with the renovation we can improve the grade and increase the selling price and that the renovation cost will be 10% of the house value.

* **Question Marks:** These products require a huge amount of cash to maintain and special attention to determine if the venture can be indeed viable. We will consider that houses with the following characteristics are our Question Marks:
 * Houses with grades 11 and 12 and prices below the regional median. We will consider that with the renovation we could improve the grade and increase the selling price. The renovation cost will be estimated as 10% of the house value.

* **Dogs:** These products don’t generate profit nor require a huge amount of cash and are not to be focused on by the company. We will consider all houses that do not fulfil the requirements above to be Dogs. An important point is that a Dog property can become a cash cow or question mark with the market moves. Hence, it is crucial to keep the housing database updated and follow up with the market.

After we segregate the best buy opportunities for the company, we analyzed the seasonality effect on the buy prices. We concluded that the best seasons to sell the houses are spring and summer, in which the mean price and the amount of houses offered is higher, into these seasons the best months are March, April, May, June and July. On the other hand, the best seasons to buy houses for a lower price are autumn and winter, especially on November, December, January and Febuary. 

## Job Deliver

This project had two steps, the first one was the analysis of the data base in order to filter the houses that matched the definition in our categories and the second one was to create an app with the streamlit library that shows on map the selected houses for the company to buy and sell. The app can be found [here](https://house-rocket-analytic.herokuapp.com/). 

The main objective of the app is to enable the House Rocket team to filter by classification, margin, profit, cost of the house or revenue the houses that were selected as market opportunities. They will be able to download the filtered database and use it to guide their next buy and sell. 

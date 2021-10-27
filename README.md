# House Rocket

<img src = "small logo.jpg" alt="Drawing" style="width: 200px;"/>

## House Rocket Company

**House Rocket** is a buy and sells houses enterprise based in Seattle. The business model is to buy houses and sell them for a higher price, sometimes renovating the acquired house before selling to maximize their value. Hence, the business core is finding undervalued properties and selling them for a higher price. 

## Business Problem

As the main business is to buy and sell houses, their main problems are: 

* Determinate the undervalued houses;
* What should be the selling price; 
* When should they to sell it;

In order to solve these problems we will create premisses to analyze if a house is undervalued and for how much it should be sold. A analysis of the best period to sell the houses will also be made. 

## Project Scope and Premisses

The initial part of the job is to analyze the available houses in the database provided by House Rocket and determine which are the best business prospects. To organize the opportunities, we will use the BCG matrix (or growth-share matrix) to scale the importance of the business opportunity. 

Below follows the description of each classification and which type of house will be in each:  

* **Cash Cows:** This product requires little investment and generates cash that can be utilized for investment in other business units. These are the corporation's key source of cash and are specifically the core business. We will consider that houses with the following characteristics are our Cash Cows: 
 * Houses with good conditions that are in the first quantile of price in their region.
 * Houses with waterfront and good conditions are in the first quantile of price.
 
* **Stars:**  These products require large investment but also provide large rentability. We will consider that houses with the following characteristics are our Stars:
 * Houses with waterfront in bad condition will require renovation before being sold. We will assume that the renovation cost will be 15% of the house value.
 * Houses with waterfront and grade between 6 and 8. We will assume that with the renovation we can improve the grade up to 2 points and increase the selling price. We will assume that the renovation cost will be 10% of the house value.

* **Question Marks:** These products require a huge amount of cash to maintain and special attention to determine if the venture can be indeed viable. We will consider that houses with the following characteristics are our Question Marks:
 * Houses with grades between 6 and 8 and prices below the regional median. We will consider that with the renovation we could improve the grade up to 2 points and increase the selling price. We will assume that the renovation cost will be 10% of the house value.

* **Dogs:** These products don’t generate profit nor require a huge amount of cash and are not to be focused on by the company. We will consider all houses that do not fulfil the requirements above to be Dogs. An important point is that a Dog property can become a cash cow or question mark with the market moves. Hence, it is crucial to keep the housing database updated and follow up with the market.

After we segregate the best buy opportunities for the company, we must analyze when and how much the company should sell the properties. To get this result, we will make a seasonality study among the sell prices and estimate the best period of the year for the real state market.  

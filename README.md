# CreditSuisseCodingChallenge










#Challenge 2 - Risk and Reward

A team of traders have a series of trades, numbered 0-i, that they can fulfill for a client.

We have three arrays: trader, risk, and bonus.
Trader[i] gives the skill level of the ith trader.
Risk[i] gives the difficulty of the ith trade. Only traders with a skill level at or above risk[i] can complete trade[i]. Completion of a trade[i] gives the team a bonus of bonus[i].
What is the biggest total bonus the traders can make?

Constraints

trader.length, risk.length, bonus.length >= 1 and <= 10,000
The arrays are not necessarily in ascending order (although bonusi and riski will always correspond to the bonus and risk of trade i)
Each trader is only able to take on at most one trade, but multiple traders can complete the same trade.
Output Format

The value returned should be the maximum profit that can be made from your trading stategy.

Examples

Example 1

For the following input trader = [6, 7, 2, 8, 1] risk = [5, 4, 3, 1, 8] bonus = [9, 9, 1, 9, 4]

Output: 45

Example 2

For the following input trader = [2, 10, 9, 10, 10] risk = [9, 1, 1, 6, 1] bonus = [9, 9, 8, 10, 10]

Output: 50



#Challenge 4 - Choosing Wisely

Lisa has a maximum total complexity of trades that she is able to fulfill in one day. In the morning, she is given a list of trades to choose from. Each one has a value, v and a complexity, c. What is the maximum value of trades that she can execute, given her complexity constraint?

Input Format

The inputs are a pair of arrays, v and c, and a maximum complexity, mc. The elements of v represent trade value in millions of dollars and is any positive integer. The complexity is between 0-100 and represents a percentage. The maximum complexity is a scalar integer.

Output Format

The value returned should be the maximum value of trades that Lisa can execute.

Examples

Example 1

For the following inputs

v = [6, 10, 12]

c = [30, 60, 90]

mc = 150

The output should be 22. This is because the maximum value elements that Lisa has capacity for is at index 1 and 2, which have complexities 60 + 90 = 150 and values 10 + 12 = 22.



#Challenge 6 - Starting and Ending well

You are a developer at Canary Investments, and are currently working on a project which involves handling an highly confidential portfolio of emerging market, real estate and technology stocks S. Si has value i.

You are given the task of evaluating the portfolio, and finding the stock with maximum value which has the provided starting and ending in order to make further decisions about this portfolio. If such a stock does not exist in your portfolio, then return -1 in order to indicate this.

Your method of evaluating a portfolio must be able to efficiently evaluate portfolios of varying values and stocks.

Input Formats

The input is an array of stocks S, such that Si has value i

Your method to evaluate will take as parameters the starting and ending which has been provided

Output Format

The return value should be an integer n, which denotes the index of highest valued stock with the given starting and ending.

Example

<b>Input</b>

Array portfolio s: {VPAI, HRLG, AIGHRW, DBPF, AJWW}

The given starting and ending are "A", and "W" respectively

<b>Output</b>

class.yourMethod(“A”,”W”) should return the following :

4

As the stock AJWW, has a higher value than the stock AIGHRW, even though they both have the same starting and ending characters

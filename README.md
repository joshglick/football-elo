##A elo calculator for simulated football##
---

###Variables

- MAX_ADJUST - The maximum ELO a team can gain or win for a loss
- GUINEA_PIG - The name of the team to print all of their results to guineapig.txt useful for checking the numbers with a single team which is easier to follow along with
- USE_MOV - Rather to use the mov ELO or revert to classic ELO based on win/lose
- STARTING_ELO - A dictionary containing the starting ELO by year
- BASE_ELO - The ELO to fallback to if the year is not in STARTING_ELO

### Files
- games.csv - Where we read the data into to process the data must be space separated and in the following format: 
	`"2015 Week 8 FINAL SCORE: (4-3) California 17-3 WestVirginia (2-5)"`
	*Note: Team names should NOT contain spaces*
	
- starting-elo.csv - a starting list of ELO's useful if you are doing it year by year, can be left blank. ELOs in this list must be in the following format:  
	`WestVirginia,1650`  
	*Note: Team names should NOT contain spaces*
	
- guinea-pig.txt - The results of the single team specified in GUINEA_PIG will be printed out here

- results.txt - The final ELO for all the teams provided in either starting-elo.csv or games.csv

### To run the project

`python elo.py`

### A simpler ELO

[Here is a link to the older version with less customizeable features](https://github.com/joshglick/football-elo/tree/basic_elo)
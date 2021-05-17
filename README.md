# Election-Analysis

## Overview of Election Audit

The purpose of this election audit analysis was to automate the work of counting votes from across several Colorado counties. With the use of python, we were able to eliminate the need for a person to manually recount every vote tabulated in our CSV file. Our script will also be able to provide summary statistics around the election. Such as, the winning candidate, the number of votes cast for each candidate, and where the most votes were cast based from voter’s resident county.

## Results

- Number of Votes Cast: **369,711**
- Number of Votes Cast by County:

![County Breakdown](https://github.com/rulma/Election-Analysis/blob/1fa2f3c0a945e8e84d8cd862fb948bc1626815a1/Resources/County%20Breakdown.PNG)

- County with the Largest Voter Turnout: **Denver**

- Candidate Vote Breakdown:

![Candidate Breakdown](https://github.com/rulma/Election-Analysis/blob/f3973e0415392d17322dc5d65b6c3d3e199ac996/Resources/Candidate%20Breakdown.PNG)

- Winning Candidate Summary:

![Winner Breakdown](https://github.com/rulma/Election-Analysis/blob/f3973e0415392d17322dc5d65b6c3d3e199ac996/Resources/Winner%20Breakdown.PNG)

## Summary

Our script works exceptionally well for the dataset we were tasked with auditing. What I would propose is making this script more robust and able to handle not only local elections in Colorado, but any election cast anywhere in the greater USA. The foundation we created in this project would serve as an excellent launching point for creating an audit software that could be used anywhere in the USA.

There would be several necessary changes that must take place for us to be able to handle a larger, more complicated dataset. First, if we wanted to handle national elections, we would need to be able to account for States. Our dataset would come with an extra column listing the state the votes were cast in and we would need to be able to tally and calculate percentages in the same way we do for counties now.

Second, if we wanted to be able to handle primaries, we would need to account for a candidate’s party affiliation. This is because during primary elections votes cast for the Republican ticket do not have any effect on the outcome Democratic party race. By knowing the respective parties for candidates, we would know where to apply their vote totals by keeping two separate dictionaries to account for Republican candidates and Democratic candidates. As only other candidates of the same party can compete with one another for the nomination. 

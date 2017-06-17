Task: Create a file input.csv using simple.csv file.

- input.csv file contains events data. 

1st colume contains Initial key name, 

2nd colume contians Key Number, 

3rd colume contains combination of column 1 and column 2,

4th column contains Entry Location value

5th column contains Exit Location value

6th column contains Entry Date 

7th column contains Exit Date


#### input.csv

| Initial | Number | Key | EntryLocation | ExitLocation | EntryDate | ExitDate |
| ------- | ------ | --- | ------------- | ------------ | --------- | -------- |
| ALS 	  | 2000   | ALS 2000| X 344E    | X 344E       | 3/24/2017 | 3/24/2017|
| CNW 	|8646	|CNW 8646	|NZ021S	|NZ021 |	2/15/2017	| 2/16/2017 |
| CNW 	| 8646	| CNW 8646	| NZ021S	| NZ022S |	2/16/2017 |	2/17/2017 |
| CNW 	| 8646	| CNW 8646	| NZ021S	| NZ021S |	2/19/2017 |	2/20/2017 |


input.csv file contains all days event data. So we want to create new output.csv file that is combination of same event data.
If two event key is same and different between exit date of one event and entry date of another event is more than 1 then that event is consider as new event.

#### output.csv 

| Initial | Number | Key | EntryLocation | ExitLocation | EntryDate | ExitDate |
| ------- | ------ | --- | ------------- | ------------ | --------- | -------- |
| ALS 	  | 2000   | ALS 2000| X 344E    | X 344E       | 3/24/2017 | 3/24/2017|
| CNW 	|8646	|CNW 8646	|NZ021S	|NZ022S |	2/15/2017	| 2/17/2017 |
| CNW 	| 8646	| CNW 8646	| NZ021S	| NZ021S |	2/19/2017 |	2/20/2017 |


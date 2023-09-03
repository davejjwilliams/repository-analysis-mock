# Mock Repository for Analysis Script Testing

Repository to test the functionality of the analysis script for the completion of COMP0111 Industry Project. Please access [Junction40/comp0111-repo-analysis](https://github.com/Junction40/comp0111-repo-analysis) to view usage instruction for the script.

## Given Input

#### **`config.py`**

```py
github_enterprise_repo = False
github_enterprise_hostname = ""
analysed_repository = "davejjwilliams/repository-analysis-mock"
filter_date = "01/01/2000"
```

## Expected Output

| repo                                       | pr_ID | creation_date    | suggestion | bassist_comment | comment_text                                                                        | comment_code                                                        | action           | response_time | url                                                                                      |
| ------------------------------------------ | ----- | ---------------- | ---------- | --------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------- | ------------- | ---------------------------------------------------------------------------------------- |
| b'davejjwilliams/repository-analysis-mock' | 2     | 03/09/2023 13:48 | TRUE       | FALSE           | b" - CODE - Looks like I've found the missing factor of 10 from above. Great work." | b'return num\*3'                                                    | Ignored/Rejected | No Reaction   | https://github.com/davejjwilliams/repository-analysis-mock/pull/2#discussion_r1314262465 |
| b'davejjwilliams/repository-analysis-mock' | 2     | 03/09/2023 13:48 | TRUE       | FALSE           | b'You messed up the conversion here by a factor of 10. - CODE - '                   | b'return num\*1760'                                                 | Ignored/Rejected | No Reaction   | https://github.com/davejjwilliams/repository-analysis-mock/pull/2#discussion_r1314262409 |
| b'davejjwilliams/repository-analysis-mock' | 1     | 18/08/2023 13:46 | FALSE      | FALSE           | b'Because this is the sq function. What did you expect?'                            | No Code                                                             | -                | No Reaction   | https://github.com/davejjwilliams/repository-analysis-mock/pull/1#discussion_r1298473158 |
| b'davejjwilliams/repository-analysis-mock' | 1     | 18/08/2023 13:45 | TRUE       | FALSE           | b'Why are you returning square? - CODE - '                                          | b'return num \* num \* num'                                         | Ignored/Rejected | No Reaction   | https://github.com/davejjwilliams/repository-analysis-mock/pull/1#discussion_r1298472536 |
| b'davejjwilliams/repository-analysis-mock' | 1     | 18/08/2023 13:35 | TRUE       | FALSE           | b'You called the wrong function in this line! - CODE - Hope this helps!'            | b'print("{} miles is {} kilometres".format(num, miles_to_km(num)))' | Accepted         | 1859          | https://github.com/davejjwilliams/repository-analysis-mock/pull/1#discussion_r1298461092 |



In social media, hashtags like "#info1" are used to mark topics or keywords in a text. In this task, you will write a function `analyze` that scans a list of social media posts for such hashtags. The function will receive a list of posts, your task is to analyze the strings, identify the hashtags, and count them. The result should be a dictionary, in which all hashtags are included with their count.

For example, consider the following list of posts:

    [
        "hi #weekend",
        "good morning #zurich #limmat",
        "spend my #weekend in #zurich",
        "#zurich <3"
    ]

After analyzing this list, your function should return:

	{'weekend': 2, 'zurich': 3, 'limmat': 1}


A Hashtag is defined as a '#' followed by any combinations of letters (lower/upper) and numbers. For simplicity, we assume that only the basic characters that are also available in ASCII can be used in a hashtag (i.e., a-z, A-Z, 0-9). Every other character (e.g., space or '.') ends the current hashtag. Hashtags need to start with a letter and cannot be empty.

You can assume that the parameter is always a valid list of strings and you do not need to provide any kind of input validation.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail.

**Note:** For this task, hashtags are case-specific. #ZURICH should be counted as a different hashtag than #zurich.




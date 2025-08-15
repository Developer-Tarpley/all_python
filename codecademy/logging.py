'''
Logging in Python

Learn about the benefits and functionalities of using a logging module!
Introduction

In this article, we will introduce logging for programmers. We will learn about:

    Advantages of using logs instead of using print statements
    Briefly introduce the logging module to write logs in Python

Advantages of Logs

Imagine you are developing an application, and upon running tests, you find some unexpected behavior occurring. You decide to add some print statements throughout the code to see what could be causing your errors. Before long, your beautiful, clean code is littered with print statements! As your code becomes messier, tracking where your print statements exist in your program can become a massive headache. These print statements will also need to be removed before the application enters a final, production-ready state, which can be tedious. There is a potential risk of a print statement getting left behind.

To circumvent a myriad of untidy print statements scattered throughout the code, you can use a logging utility to provide programmers with logs that detail either error messages or general information and output from a program. We can keep our code neatly organized by utilizing a logging utility, making it easy for other programmers to view and understand what is happening and maintain the code. Organized code also makes the task of debugging significantly easier. Using a logging utility can help with debugging by providing detailed information on what caused an error, what time the error occurred, where inside the code the error occurred, or simply providing general information like the values of variables that you need to debug. Finally, by using a logging module, we can save time from needing to remove print statements manually.
Using Logs in Python

Now that we’ve covered some high-level examples of why we would want to use a logging utility, let’s look at how to log specifically with Python. By importing Python’s logging module, we can:

    Identify the date and time of a custom or error message
    Format logs to make debugging easier
    Set severity levels for the logs
    Output the logs to various streams

We’ll briefly introduce these functionalities in this article. In the next lesson, we will go more in-depth on these concepts and practice with them in some interactive coding exercises!

To show how logging is used in a real-world example, imagine we are building an application that accepts username and password input from the user and is responsible for verifying that the entered information matches a registered user in the system. If it does not, it will raise an error. We can add logging statements to the function where this code occurs to log the values entered and log the error message if an exception or error is raised.

import logging
logger = logging.getLogger(__name__)
def attempt_login(username, password):
  logger.info("Attempting to validate the entered credentials!")
  if not verify_credentials(username, password):
    logger.error(“Invalid credentials for username: {username}!”.format(username=username))

Dated Timestamps

It is almost always helpful to know the date and time when a logged message or error occurred for debugging or investigative purposes. The Python logging module provides a formatting option to include dated timestamps for logged messages. Take our login application, for example. Timestamped log messages can help us determine the exact time and date that login attempts occurred in our application. We can look at an example of such a log message below:

[2021-11-08 03:16:05,980] {ERROR} login:attempt_login - Invalid credentials for username: foo!
Additional Formatting Options

Debugging an application can be cumbersome, especially the more complex the application is and the more lines of code and modules it has. The logging module fortunately provides several options for formatting what information is included in the log message and how that information appears. We’ve just seen that there is a formatting option that allows us to include timestamps. We can also include information like the module name where the logged message occurred, or even more, the specific line number within the code file. These formatting options eliminate any need to figure out which module, function, or line number a debugging message originated from.
Severity Level

There are varying levels of severity for logging messages in Python: notset, debug, info, warning, error, and critical. These log levels are used in specific cases that range from providing general information to alerting of severe errors. Being able to set different severity levels for logged messages allows us to filter out logs of certain levels or limit easily. For our login application, once we are ready to move it into a production-ready state, we will not need to have any debug log messages included in our log file. The great advantage to using the logging module is that we do not have to go back and manually remove our logging debug statements from the code like we would have to for print statements. We can filter out any logging statements that have a debug severity level by setting a log level for the logger.
Log Files

Another advantage of using the logging module over console print statements is that the logs can be saved to a file, allowing the log messages to be accessed beyond code execution time. Additionally, the saved log file can then be indexed and made searchable through other software and applications.
Conclusion

In short, logging provides many benefits over using print statements, including:

    the ability to set a destination for the logged messages (e.g. console, file, sockets)
    formatting options for the log messages that include timestamps and line numbers, filtering of log messages based on log level severity
    much more!

This powerful module is key to making clean, readable, maintainable code that can easily be debugged and investigated by using the generated log output.
'''
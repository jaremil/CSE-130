# 1. Name:
#      Jade Miller
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program will count the days between specific dates.
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was a bit harder than others for me. I'm glad that we write the pseudocode because it helps be a lot at this stage.
# 5. How long did it take for you to complete the assignment?
#      3 hours

# PROMPT for start
# GET start_day, start_month, end_year
# PROMPT for end
# GET end_day, end_month, end_year
# IF end_year < start_year
#     ERROR
# IF end_year = start_year and end_month = start_month
#     IF end_day < start_day
#         ERROR
#     ELSE
#       RETURN end_day - start_day
#days= daysInMonth(start_month, start_year) - start_day
#IF start_year = end_year
# FOR month = start_month + 1 TO end_month - 1
#   days += daysInMonth(month, start_year)
#ELSE
#    FOR month = start_month + 1 TO end_month  - 1
#       days += daysInMonth(month, end_year)
#RETURN days + end_days
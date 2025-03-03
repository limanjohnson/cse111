import math

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Enter you age: "))

heart_rate_max = int(220 - age)

heart_rate_65 = round((heart_rate_max * .65))
heart_rate_85 = round((heart_rate_max * .85))

print(heart_rate_65)
print(heart_rate_85)

print(f"When exercising, you should aim to have a heart rate between {heart_rate_65} and {heart_rate_85} bpm.")

'''

You're given a list containing the schedules of multiple people. 
Each person's schedule is a list of non-overlapping intervals in sorted order. 
An interval is specified with the start time and the end time, 
both being positive integers. 
Your task is to find the list of intervals representing the free time for all the people. 
We're not interested in the interval from negative infinity to zero or 
from the end of the last scheduled interval in the input to positive infinity.

'''


from interval import Interval


def employee_free_time(schedule):
    res = []
    all_schedules = [s for p in schedule for s in p]
    all_schedules.sort(key=lambda s: s.start)
    prev_end = all_schedules[0].end
    for i in range(1, len(all_schedules)):
        cur = all_schedules[i]
        if prev_end < cur.start:
            res.append(Interval(prev_end, cur.start))
        prev_end = max(prev_end, cur.end)

    return res

# Function for displaying interval list


def display(vec):
    string = "["
    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "
    string += "]"
    return string

# Driver code
def main():
    print('')
    inputs = [
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
        [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
        [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
        [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)], [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)], [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    ]
    i = 1
    for schedule in inputs:
        print(i, '.\tEmployee Schedules:', sep="")
        for s in schedule:
            print("\t\t", display(s), sep="")
        print("\tEmployees' free time", display(employee_free_time(schedule)))
        print('-'*100)
        i += 1


if __name__ == "__main__":
    main()
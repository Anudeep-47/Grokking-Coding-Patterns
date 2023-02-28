'''

You're given a list of non-overlapping intervals, 
and you need to insert another interval into the list. 
Each interval is a pair of non-negative numbers, 
the first being the start time and the second being the end time of the interval. 
The input list of intervals is sorted in ascending order of start time.

The intervals in the output must also be sorted by the start time, 
and none of them should overlap. 
This may require merging those intervals that now overlap as a result of the addition of the new interval.

'''

from interval import *

def insert_interval(existing_intervals, new_interval):
    result = []
    not_inserted = True
    for cur in existing_intervals:
        if not_inserted and cur.end < new_interval.start:
            result.append(cur)
        elif not_inserted:
            if new_interval.end < cur.start:
                result.append(new_interval)
                result.append(cur)
            else:
                result.append(Interval(min(cur.start, new_interval.start), max(cur.end, new_interval.end)))
            not_inserted = False
        else:
            last = result[-1]
            if last.end < cur.start:
                result.append(cur)
            else:
                last.end = max(last.end, cur.end)
    if not_inserted:
        result.append(new_interval)
        
    return result

# Printing list of intervals
def interval_list_to_str(lst):
    result_str = ""
    for i in range(len(lst)):
        result_str += str(lst[i]) + ", "
    return "[" + result_str[:-2] + "]"

def main():
    print('')
    new_interval = Interval(9, 10)
    existing_intervals = [Interval(1, 2), Interval(3, 4), Interval(7, 8)]
    print("1.\tExisting intervals: ", interval_list_to_str(existing_intervals), sep="")
    print("\tNew interval: ", new_interval, sep="")
    output = insert_interval(existing_intervals, new_interval)
    print("\tUpdated intervals: ", interval_list_to_str(output), sep = "")

if __name__ == "__main__":
    main()
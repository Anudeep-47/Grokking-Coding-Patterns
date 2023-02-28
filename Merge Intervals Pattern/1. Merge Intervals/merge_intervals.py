'''
We're given an array of closed intervals as input where each interval has a start and end timestamp. 
The input array is sorted by starting timestamps. 
Merge the overlapping intervals and return a new output array.

'''

from interval import *

def merge_intervals(v):
    res = []
    if v and len(v) == 0:
        return res
    res.append(Interval(v[0].start, v[0].end))
    for i in range(1, len(v)):
        cur = v[i]
        last_added = res[-1]
        if last_added.end >= cur.start:
            last_added.end = max(last_added.end, cur.end)
        else:
            res.append(Interval(cur.start, cur.end))
    return res

# Printing list of intervals
def interval_list_to_str(lst):
    result_str = ""
    for i in range(len(lst)):
        result_str += str(lst[i]) + ", "
    return "[" + result_str[:-2] + "]"


def main():
    print('')
    v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
    v2 = [Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)]
    v3 = [Interval(3, 7), Interval(6, 8), Interval(10, 12), Interval(11, 15)]
    v4 = [Interval(1, 5)]
    v6 = [Interval(1, 9), Interval(3, 8), Interval(4, 4)]
    v7 = [Interval(1, 2), Interval(3, 4), Interval(8, 8)]
    v8 = [Interval(1, 5), Interval(1, 3)]
    v9 = [Interval(1, 5), Interval(6, 9)]
    v10 = [Interval(0, 0), Interval(1, 18), Interval(1, 3)]

    v_list = [v1, v2, v3, v4, v6, v7, v8, v9, v10]

    for i in range(len(v_list)):
        print(i + 1, ". Intervals to merge: ", interval_list_to_str(v_list[i]), sep="")
        result = merge_intervals(v_list[i])
        print("   Merged intervals:\t", interval_list_to_str(result))
        print("-"*100)


if __name__ == '__main__':
    main()
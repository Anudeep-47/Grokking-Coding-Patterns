'''

For two lists of closed intervals given as input, 
interval_list_a and interval_list_b, 
where each interval has its own start and end time, 
write a function that returns the intersection of the two interval lists.

For example, the intersection of [3, 8] and [5, 10] is [5, 8].

'''


from interval import *


# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    result = []
    list_a_len = len(interval_list_a)
    list_b_len = len(interval_list_b)
    i = j = 0
    while i<list_a_len and j<list_b_len:
        list_a_item = interval_list_a[i]
        list_b_item = interval_list_b[j]
        start = max(list_a_item.start, list_b_item.start)
        end = min(list_a_item.end, list_b_item.end)
        if start <= end:
            result.append(Interval(start, end))
        if list_a_item.end < list_b_item.end:
            i += 1
        else:
            j += 1

    return result


# Driver code
def main():
    print('')
    input_interval_list_a = [[Interval(1, 2)],
                             [Interval(1, 4), Interval(5, 6), Interval(9, 15)],
                             [Interval(3, 6), Interval(8, 16), Interval(17, 25)],
                             [Interval(4, 7), Interval(9, 16), Interval(17, 28), 
                                 Interval(39, 50), Interval(55, 66), Interval(70, 89)],
                             [Interval(1, 3), Interval(5, 6), Interval(7, 8), 
                                 Interval(12, 15)]
                             ]

    input_interval_list_b = [[Interval(1, 2)],
                             [Interval(2, 4), Interval(5, 7), Interval(9, 15)],
                             [Interval(2, 3), Interval(10, 15), Interval(18, 23)],
                             [Interval(3, 6), Interval(7, 8), Interval(9, 10),
                                 Interval(14, 19), Interval(23, 33), Interval(35, 40),
                                 Interval(45, 59), Interval(60, 64), Interval(68, 76)],
                             [Interval(2, 4), Interval(7, 10)]
                             ]

    for i in range(len(input_interval_list_a)):
        print(i + 1, '.\t Interval List A: ',
              display(input_interval_list_a[i]), sep="")
        print('\t Interval List B: ',
              display(input_interval_list_b[i]), sep="")
        print("\t Intersecting intervals in 'A' and 'B' are: ",
              display(intervals_intersection(
                  input_interval_list_a[i], input_interval_list_b[i])), sep="")

        print('-' * 100)


if __name__ == "__main__":
    main()
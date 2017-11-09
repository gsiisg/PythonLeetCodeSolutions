#!/usr/bin/env python
"""
https://leetcode.com/problems/the-skyline-problem/description/
https://discuss.leetcode.com/topic/34119/10-line-python-solution-104-ms

A city's skyline is the outer contour of the silhouette formed by all the buildings
in that city when viewed from a distance.

Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A),
write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively,
and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ]
that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline,
and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
[...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # events are the (beginning, -height, ending) of buildings sorted in ascending order
        # Must place negative height as 2nd element so all the 0 height comes at the end
        # this is needed so that ending of a building and beginning of building with same height
        # does not add extra 'result' element
        # use negative height for later (negative since python uses min heap)
        # ending of buildings only have (endings,0,0) padded with zeros
        events = sorted([[L, -H, R] for [L, R, H] in buildings] + [[R, 0, 0] for [L, R, H] in buildings])

        # initialize the result array and heap containing the information: (negativeHeight, ending-x-of-building)
        # res is 0,0 for the origin, return res[1:] so the first element place holder is not included
        # hp is (0, inf) because x can never be greater than 10000
        # so setting x to inf means that building at height=0 and x=inf will not be removed
        result = [(0, 0)]
        buildingHeap = [(0, float("inf"))]

        for L, negH, R in events:
            # at a current x, check the front of the heap if the first building is past its ending
            # if past, then remove it from heap
            # since buildings are not removed whenever the ending is encountered, but past, the while loop will remove
            # all the buildings that are past the location x if they are at the front of the heap
            # if they are not at the front of the heap now,
            # they will get removed later when the front of the heap is removed
            while L >= buildingHeap[0][1]:
                heapq.heappop(buildingHeap)

            # if negativeHeight exist that means it is not an ending building event
            # add the building (height,ending) to heap
            if negH:
                heapq.heappush(buildingHeap, (negH, R))

            # if there is height from the last building or the event (by their addition),
            # then add the height of the tallest building to result
            # if the height from the event is 0 that means there is no building in heap and
            # the event is ending of a building so set height to 0 which is the
            if result[-1][1] + buildingHeap[0][0]:
                result += [L, -buildingHeap[0][0]],

        return result[1:]

# O(n log n) 102ms

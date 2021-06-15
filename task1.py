"""
Suppose you have time intervals (1000,1800) and (3400,4500), i.e., the first interval starts at time t=1000, and ends at time t=1800. Define (100,200) and (200,250) to be overlapping, since they overlap at timestep 200. However, (100,199) and (200,250) are non-overlapping.

Task: Implement function to check if a new time segment overlaps with any of the previous segments. 
"""


def is_overlapping(segment_time : tuple, previous_segments : tuple):
    """
    Checks if the time of a segment overlaps with the times of existing segments.
    
    Arguments:
    segment_time -- a tuple of (segment_start, segment_end) for the new segment
    previous_segments -- a list of tuples of (segment_start, segment_end) for the existing segments
    
    Returns:
    True if the time segment overlaps with any of the existing segments, False otherwise
    """

    return 


# Run test:
#-----------
overlap1 = is_overlapping((950, 1430), [(2000, 2550), (260, 949)])
overlap2 = is_overlapping((2305, 2950), [(824, 1532), (1900, 2305),(3424, 3656)])

print("Overlap 1 = ", overlap1)
print("Overlap 2 = ", overlap2)
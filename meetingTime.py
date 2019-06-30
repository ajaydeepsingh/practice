# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

def canAttendMeetings(intervals):
    if not intervals:
        return 0
    
    timeline = []
    for i in intervals:
        timeline.append(('start', i[0]))
        timeline.append(('end', i[1]))
    

    timeline = sorted(timeline, key=lambda x: (x[1], x[0]))

    room = 0
    max_room = 0

    for k,v in timeline:
        if k == 'start':
            room += 1
        else:
            room -= 1
        if room > max_room:
            max_room = room
    
    return max_room



# driver code

print(canAttendMeetings([[0, 30],[5, 10],[15, 20]]))
print(canAttendMeetings([[0, 6],[5, 10],[8, 20]]))
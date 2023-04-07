class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start_time = sorted([interval[0] for interval in intervals])
        end_time = sorted([interval[1] for interval in intervals])

        si = ei = max_room = room_used = 0
        while si < len(start_time):
            if start_time[si] < end_time[ei]:
                room_used += 1
                si += 1
            else:
                room_used -= 1
                ei += 1
            max_room = max(max_room, room_used)
        return max_room

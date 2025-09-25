from typing import List

class LogAnalyzer:
    def __init__(self):
        self.events = {} # key timestamp; value = user_id[]

    def add_event(self, timestamp: int, user_id: str):
        new_list = [user_id] # start this as a list so we have Methods

        current_list = self.events.get(timestamp)

        if current_list != None:
            new_list.extend(current_list)

        self.events[timestamp] = set(new_list) # here we make it a set for unique values at the timestamp

    # not a required function, but unless there is a reason not to split it off (reveals PII)
    # it doesn't add any code complexity and would allow for intermediate testing
    def list_active_users(self, window_size: int, current_time: int) -> List[str]:
        active_users = []
        start = current_time - window_size + 1
        end = current_time + 1 
        for i in range(start, end):
            ct_users = self.events.get(i)

            if ct_users != None:
                active_users.extend(ct_users)

        return set(active_users)

    def count_active_users(self, window_size: int, current_time: int) -> int:

        return len(self.list_active_users(window_size, current_time))
    
analyzer = LogAnalyzer()

analyzer.add_event(1, "alice")
analyzer.add_event(2, "bob")
analyzer.add_event(3, "alice")
analyzer.add_event(7, "carol")
print(analyzer.list_active_users(5, 7))
print(analyzer.count_active_users(5, 7))  # Window = [3..7] → {"alice", "carol"} → 2
print(analyzer.list_active_users(10, 7))
print(analyzer.count_active_users(10, 7)) # Window = [−2..7] → {"alice", "bob", "carol"} → 3

analyzer.add_event(7, "steve")
analyzer.add_event(7, "steve")
print(analyzer.list_active_users(10, 7))

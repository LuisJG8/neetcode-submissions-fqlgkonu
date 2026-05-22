class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # ../ = +1
        # ./ = 0
        # x/ = -1

        counter = 0
        for log_folder in logs:
            if log_folder[0].isalpha() or log_folder[0].isnumeric():
                counter -= 1
            if len(log_folder) == 2:
                counter += 0
            if len(log_folder) > 2 and ".." in log_folder:
                if counter == 0:
                    pass
                else:
                    counter += 1
        return abs(counter)
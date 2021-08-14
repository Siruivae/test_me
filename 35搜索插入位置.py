class solution:
    def search(self, str, x):
        n = len(str)
        k = 0
        for i in range(n):
            if str[i] == x:
                return i
            else:
                i += 1
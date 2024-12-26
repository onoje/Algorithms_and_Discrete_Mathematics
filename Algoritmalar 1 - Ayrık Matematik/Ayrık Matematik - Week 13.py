import heapq,time

class MRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = {}
        self.heap = []
        self.key_to_timestamp = {}
   

    def _update_access_time(self, key):
        if key in self.key_to_timestamp:
            self.key_to_timestamp[key] = time.time()
            heapq.heappush(self.heap, (-self.key_to_timestamp[key],key))
            return


    def get(self, key):
        if key not in self.hash_table:
            return -1
        self._update_access_time(key)
        return self.hash_table[key]


    def put(self, key, value):
        if key in self.hash_table:
            self.hash_table[key] = value
            self._update_access_time(key)
            return

        if len(self.hash_table) >= self.capacity:
            while self.heap:
                oldest_time, oldest_key = heapq.heappop(self.heap)
                if self.key_to_timestamp.get(oldest_key) == -oldest_time:
                    del self.hash_table[oldest_key]
                    del self.key_to_timestamp[oldest_key]
                    break

        self.hash_table[key] = value
        self.key_to_timestamp[key] = time.time()
        heapq.heappush(self.heap, (-self.key_to_timestamp[key], key))

 
class Solution:
    def get_next_chunk(self,version,version_length,pointer):
        if pointer>version_length-1:
            return 0,pointer
        chunk_end = pointer
        while chunk_end < version_length and version[chunk_end]!=".":
            chunk_end=chunk_end+1
        chunk_value = int(version[pointer:chunk_end])
        pointer = chunk_end+1
        return chunk_value,pointer
    def compareVersion(self, version1: str, version2: str) -> int:
        pointer1 =0
        pointer2 =0
        length1 = len(version1)
        length2 = len(version2)
        while pointer1<length1 or pointer2<length2:
            chunk1, pointer1 = self.get_next_chunk(version1,length1,pointer1)
            chunk2, pointer2 = self.get_next_chunk(version2,length2,pointer2)
            if chunk1 != chunk2:
                return -1 if chunk2>chunk1 else 1
        return 0

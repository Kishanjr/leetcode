class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # create an empty hashmap to store anagrams
        hashmap = {}

        # loop through each string in the input list
        for s in strs:
            # sort the string
            sortedStr = "".join(sorted(s))

            # check if the sorted string exists in the hashmap
            if sortedStr in hashmap:
                # if it does, append the original string to its corresponding list
                hashmap[sortedStr].append(s)
            else:
                # if it doesn't, create a new key-value pair with the sorted string as key
                # and the original string as the first value in the list
                hashmap[sortedStr] = [s]

        # return a  the values
        result = hashmap.values()
        return result

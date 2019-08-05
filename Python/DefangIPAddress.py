class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

s = Solution()
addr = "127.0.0.1"
print("New address: ", s.defangIPaddr(addr))

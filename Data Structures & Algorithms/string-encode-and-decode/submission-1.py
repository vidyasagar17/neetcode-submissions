class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res, i = [], 0
        
        while i < len(s):
            # Find the delimiter
            j = s.find('#', i)
            
            # Extract length
            length = int(s[i:j])
            
            # Extract the actual string
            res.append(s[j + 1 : j + 1 + length])
            
            # Move pointer to the start of the next length-prefix
            i = j + 1 + length
            
        return res

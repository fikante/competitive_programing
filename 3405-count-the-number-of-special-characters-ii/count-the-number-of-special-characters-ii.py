class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_indices = {}  # Store indices of lowercase letters
        upper_first_index = {}  # Store first occurrence of uppercase letters
        count = 0

        # First pass: gather indices
        for index, char in enumerate(word):
            if char.islower():
                if char not in lower_indices:
                    lower_indices[char] = []
                lower_indices[char].append(index)  # Store all occurrences of the lowercase letter
            elif char.isupper():
                lower_char = char.lower()
                if lower_char not in upper_first_index:
                    upper_first_index[lower_char] = index  # Store first occurrence of uppercase letter

        # Second pass: check conditions for special characters
        for char, indices in lower_indices.items():
            if char in upper_first_index:
                upper_index = upper_first_index[char]
                # Check if all lowercase indices appear before the first uppercase index
                if all(index < upper_index for index in indices):
                    count += 1

        return count




# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         lower = {}
#         upper ={}
#         count = 0
#         for index, char in enumerate(word):
#             if char.islower():
#                 if char not in lower:
#                     lower[char] = index
#                 elif char in lower:
#                     same_index = lower.get(char)
#                     if same_index < index:
#                         lower[char] = index
#             elif char.isupper():
#                 lower_char = char.lower()
#                 if lower_char not in upper:
#                     upper[lower_char] = index
#         for char, lower_index in lower.items():
#             if char in upper:
#                 upper_index = upper[char]
#                 if lower_index < upper_index:
#                     count += 1
#                 else:
#                     return 0
#         return count

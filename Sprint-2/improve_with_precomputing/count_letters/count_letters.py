 def count_letters(s: str) -> int:
     """
     count_letters returns the number of letters which only occur in upper case in the passed string.
     """
     only_upper = set()
     for letter in s:
-        if is_upper_case(letter):
+        if is_upper_case(letter) and letter.isalpha():
             if letter.lower() not in s:
                 only_upper.add(letter)
     return len(only_upper)


 def is_upper_case(letter: str) -> bool:
-    return letter == letter.upper()
+    return letter.isalpha() and letter == letter.upper()

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        len_t = len(t)
        len_s = len(s)
        for i in range(len_t):
            if t[i] == s[0]:
                # print(f't at letter {t[i]} matched start of {s}')
                search_t_index=i
                search_s_index=0

                while (search_t_index < len_t) and (search_s_index < len_s):
                    t_letter = t[search_t_index]
                    s_letter = s[search_s_index]
                    if t_letter == s_letter:
                        if search_s_index == len_s - 1:
                            return True
                        search_t_index += 1
                        search_s_index += 1
                    else:
                        search_t_index += 1

        return False
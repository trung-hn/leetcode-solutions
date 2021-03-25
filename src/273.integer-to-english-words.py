#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
# TAGS: Math, String
# REVIEWME: Recursion


class Solution:
    # Ugly Code. 36 ms, 44.57%
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        table = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
                 "90": "Ninety", "80": "Eighty", "70": "Seventy", "60": "Sixty", "50": "Fifty", "40": "Forty", "30": "Thirty",
                 "20": "Twenty", "10": "Ten", "19": "Nineteen", "18": "Eighteen", "17": "Seventeen", "16": "Sixteen",
                 "15": "Fifteen", "14": "Fourteen", "13": "Thirteen", "12": "Twelve", "11": "Eleven"}

        def two_digits(digits, lst):
            if len(digits) == 1:
                lst.append(table[digits])
                return
            f, s = digits
            if f in "23456789":
                lst.append(table[f + "0"])
            elif f == "1":
                lst.append(table[f + s])
                return
            lst.append(table[s])
            return

        def three_digits(digits, lst):
            if len(digits) <= 2:
                two_digits(digits, lst)
                return
            f, *rest = digits
            if int(f) > 0:
                lst.append(table[f])
                lst.append("Hundred")
            return two_digits(rest, lst)

        num = str(num)
        groups = []
        s = ""
        for i in range(len(num)):
            if i and i % 3 == 0:
                groups.append(s[::-1])
                s = ""
            s += num[~i]

        groups.append(s[::-1])
        ans = []
        for g, post in zip(groups, ("", "Thousand", "Million", "Billion")):
            lst = []
            three_digits(g, lst)
            if lst and lst[0] and lst[0] != " ":
                ans.append(" ".join(lst + [post]))

        return (" ".join(ans[::-1])).strip().replace("  ", " ")

    # Clean Code from Stefan
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n - 1: n]
            if n < 100:
                return [tens[n // 10-2]] + words(n % 10)
            if n < 1000:
                return [to19[n // 100-1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p + 1):
                    return words(n // 1000 ** p) + [w] + words(n % 1000 ** p)
        return ' '.join(words(num)) or 'Zero'
# @lc code=end

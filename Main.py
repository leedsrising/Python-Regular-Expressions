class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def printlist(lst):
            accum = "placeholder"
            for x in lst:
                accum = accum + ", " + x
            print accum
        
        def areStars(lst):
            for x in lst:
                if len(x) < 2:
                    return False
            return True
        
        def getMatchables(p):
            matchables = []
            counter = 0
            while counter <= (len(p) - 1):
                if counter == (len(p) - 1):
                    if p[counter] == "*":
                        counter += 1
                    else:
                        matchables.append(p[counter])
                        counter += 1 
                elif p[(counter + 1)] == "*":
                    matchables.append(p[counter] + "*")
                    counter += 1
                else:
                    if p[counter] == "*":
                        counter += 1
                    else:
                        matchables.append(p[counter])
                        counter += 1  
            print("matchables are ")
            printlist(matchables)
            return matchables
        
        matchables = getMatchables(p)
        
        def isMatching(s, potentials):
            if (s == "" and areStars(potentials)):
                print("return true1")
                return True
            elif (s == ""):
                if potentials == []:
                    print("return true2")
                    return True
                else:
                    printlist(potentials)
                    print("return false1")
                    return False
            elif potentials == []:
                print(s)
                printlist(potentials)
                print("return false2")
                return False
            elif len(potentials[0]) == 2:
                print("s is " + s)
                print("s0 is " + s[0])
                if (potentials[0])[:1] == s[0] or (potentials[0])[:1] == ".":
                    return isMatching(s[1:], potentials)
                else:
                    return isMatching(s, potentials[1:])
            elif potentials[0] == ".":
                return isMatching(s[1:], potentials[1:])
            else:
                if s[0] == potentials[0]:
                    return isMatching(s[1:], potentials[1:])
                else:
                    print("return false3")
                    return False
            
        return isMatching(s, matchables)
            

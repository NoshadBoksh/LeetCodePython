from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            curr_max = 0
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalize slope so direction is consistent
                if dx < 0:
                    dx, dy = -dx, -dy
                
                slopes[(dx, dy)] += 1
                curr_max = max(curr_max, slopes[(dx, dy)])
            
            max_points = max(max_points, curr_max + duplicates + 1)
        
        return max_points

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ETA = [0] * len(position)
        sortedPos = sorted(zip(position, speed), reverse=True)
        for i in range(len(sortedPos)):
            eta = (target - sortedPos[i][0])/sortedPos[i][1]
            ETA[i] = eta
        
        fleets = 1
        target = ETA[0]
        for i in range(len(ETA)):
            if ETA[i] > target:
                target = ETA[i]
                fleets += 1
        
        return fleets
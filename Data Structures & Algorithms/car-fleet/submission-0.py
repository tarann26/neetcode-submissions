class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = [(position[i],speed[i]) for i in range(len(speed))]
        l.sort(reverse=True)
        fleet = 1
        prevTime = (target - l[0][0]) / l[0][1]
        for i in range(1, len(l)):
            currCar = l[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleet += 1
                prevTime = currTime
        return fleet

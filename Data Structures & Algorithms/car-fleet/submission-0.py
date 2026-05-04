class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        leadingFleetStack = [] # contains time to target of the leading fleet

        cars = sorted(zip(position, speed), reverse = True)

        for carPosition, carSpeed in cars:
            timeToTarget = (target - carPosition) / carSpeed

            if not leadingFleetStack or timeToTarget > leadingFleetStack[-1]:
                leadingFleetStack.append(timeToTarget)

        return len(leadingFleetStack)
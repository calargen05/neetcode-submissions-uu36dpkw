import math

class Solution:

    """

        U - Understand: The problem is asking me to return the number
        of groups of cars that reach the end.

        P - Plan: The plan is to sort the position list by descending order
        and iterate through the position list and compute the time for each 
        car to reach the target. Then, I'll use a stack to maintain the times
        of the fleets of cars. If the current car's time is less than or 
        equal to the top of the stack, it joins the same fleet. Otherwise, it
        forms a new fleet, and I'll push its time onto the stack. Return the
        length of the stack at the end

        I - Implement: See code below vvv

    """

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # var definitions
        stack = []

        # sort the position list by descending order
        combined = list(zip(position, speed))
        combined.sort(key=lambda x: x[0], reverse=True)
        position, speed = zip(*combined)

        # convert back to lists
        position = list(position)
        speed = list(speed)

        
        for i in range(len(position)):
            time = self.arrival_time(target, position[i], speed[i])
            if not stack:
                stack.append(time)
            elif time > stack[len(stack)-1]:
                stack.append(time)
        return len(stack)

    def arrival_time(self, t, p, s):
        return (t-p)/s
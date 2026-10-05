import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {position[i] : speed[i] for i in range(len(position))}
        sorted_position = sorted(position)

        fleet_stack = []
        for pos in sorted_position:
            time_to_reach = ((target - pos) / pos_speed[pos])
            while len(fleet_stack) > 0 and fleet_stack[-1] <= time_to_reach:
                fleet_stack.pop()

            fleet_stack.append(time_to_reach)

        return len(fleet_stack)
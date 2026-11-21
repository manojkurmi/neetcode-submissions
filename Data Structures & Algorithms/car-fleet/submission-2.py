class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - position is the miles marker as well
        - speed in miles
        constraint:
        - car cannot pass the car ahead of it
        sol:
        - sort by descending position
        - calc hour n for 1 car to target
        - calc next set of cars to reach target by the hour n
        - this become one fleet
        - repeat above process for next fleet

        """

        def sol1():
            arr = [val for val in zip(position, speed)]
            arr.sort(reverse=True)
            n = len(position)

            fleet = 0
            idx = 0
            while idx < n:
                # find hour for 1st
                val = arr[idx]
                hours = (target - val[0]) / val[1]
                # find others who can reach target by that hour
                while idx < n:
                    val = arr[idx]
                    if (val[0] + val[1] * hours) < target:
                        break
                    idx += 1
                
                fleet += 1
            
            return fleet


        # using stack
        def sol2():
            arr = [(p, s) for p, s in zip(position, speed)]
            arr.sort(reverse=True)
            st = [float('-inf')]

            for p, s in arr:
                hr = (target-p) / s
                if hr > st[-1]:
                    st.append(hr)

            return len(st) - 1

        return sol2()

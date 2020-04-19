# Please add your answers to the ***Analysis of  Algorithms*** exercises here

## Exercise I

a) O(n^3)

b) O(log^2 n)

c) O(2n) -> O(n)

## Exercise II

> First of all, I hate this question. If you drop and egg from any height, it's going to break.
> Secondly, it doesn't give us any information to determine what floor f is going to be. Is it in the middle???
> That would seem to make sense, but it doesn't say that. It just says if it's thrown off floor "f" or higher it will break.
> But what is floor f????? Is floor f equal to n/2???? Realistically, f = floor 0, cause if you drop an egg on the ground floor,
> it's still going to break.

Our low point would be 0 for the ground.

Our high point would be "n" for the top of the building.

Our breakpoint would be "f" for the floor that the eggs can no longer be safely dropped.

For each floor, starting from the ground floor (low point) we drop an egg.

The egg will not break until we hit floor f, so we keep dropping eggs on each floor until the egg breaks.

Once the egg finally breaks (probably on floor 0) then we've found f and we no longer drop eggs from that floor or higher.

As far as runtime complexity, probably something like O(1). Because, realistically, the height of the building shouldn't determine
the value of f, because that's not how gravity and the laws of physics work. Once we figure out the value of f on one building, we should know the value of f of every building. If the laws of physics work differently in this universe this question takes place in, that should have been defined in the question.

> P.S. I'm sorry for the snappy attitude, I'm currently going through the longest and worst headache I've ever had (~36 hours) and this question isn't really helping that.

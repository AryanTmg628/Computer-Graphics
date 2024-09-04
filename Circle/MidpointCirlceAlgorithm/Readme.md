The main drawback of other methods are floating points

Just like in straight line to solve floating problem, bersenhams alogorithm is used,

Similarly, In circle also we can use bersenham's algorithm -

We are taking the the straight y-axis that is x=0 and y = radius

We are going to find one octect and then we can use reflection to plot all other point

so one octed is only when x <=y if x> y then it means slope is greater, which means x is greater that y and another octet starts\

Since we are dealing with integer only we need decision parameter

p = 1 - radius

if (p<0) {
set p = p + 2x + 1
set x = x+ 1

}

else {
p = p + 2x + 1 -2y
set y= y-1

}

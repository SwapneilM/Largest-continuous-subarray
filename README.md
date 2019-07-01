# Largest-continuous-subarray

Intent: Make a program which can find the continuous sub-array with maximum sum.

Logic: We will start from the first element in the array, then we will keep adding the next element to the sub-array.
For Example, list is our sub-array []. let's add the first element to the subarray [5]. then we keep adding the next element
[5,3,1]. If all elements are positive then answer is very simple(ans=array). The problem arise when we encounter a negetive value
[5,3,1,-1]. Now the total sum of our array greater than 0, so we can still use the this sub-array for our answer.
If the next element is -10 making the sub-array net negative, we are now unsure whether this sub-array is our answer or not.
so we will save the sub-array with max sum which is [5,3,1] and we will continue on.

Assume the next few elements after -10 are -1,14,-50,9. we will skip all the negetive number as we know it will not be greater 
than the sum of our sub-array [5,3,1]. We will accept 9 as our first element and continue the process again [9]. Next few element are -11,14
Making our new sub-array [9,-11,14]. We can see that our current sub-array beats our previous record holder [5,3,1] for maximum sum. We will 
therefore replace [5,3,1] and store [9,-11,14]. Now we will continue expanding our sub-array to check whether we can increase the sum of our sub-array.
the last 2 elements of the array are -100,50. Our new sub-array is [9,-11,14,-100,50], we can see this sub-array total sum is less than previous
one. So the correct answer is [9,-11,14].

Our logic we will be fine if there are any positive elements in the array but will fail there are none. 
To rectify this we will add a IF statement that will return the max element if the srray has no positive element.



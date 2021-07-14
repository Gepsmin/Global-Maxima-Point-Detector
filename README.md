# Global Maxima Point Detector

## Used Method

For this project, I tried both methods mentioned in the description which are Gradient method and Evolutionary method. But, after the experiments, I faced with a problem. When I was trying to pull a chosen point towards the mean point, the point was trying to act according to the derivative of itself. In some cases, the points were stuck in same coordinate with the forces from two opposite directions. So, I decided to use second method to at least be able to generate a reasonable solution. This method suggests a programmer to code in a way that program selects best points from selected points until the program ends up with a solution. 

## Explanation of Code

Firstly, the program creates the reward function and the parameters of it as suggested in the description. Addition to the given function, we need to define helper functions. They are find_sample which chooses sample points from normal distribution function according to the given mean and variance and sample_range which finds the range of a sample via calculating the difference between the maximum and the minimum points. After defining and plotting our base graph, we randomly choose our sample space and the values of them from the graph. We iterate the program until the range of the sample space is less then 0.01 which means the points are approximately in the same coordinate. But the maximum iteration number is 6 because of the technique I used to choose the best m points from sample space. The m refers to the equation:  12 – iteration * 2. With this recipe, first iterations are less strict, and the subsequent iterations are stricter. In first steps, we need to avoid making strict assumptions about the best possible coordinates because of the wide variety of the range against to the small number of points we have. But in the preceding steps, we have more information in our range. So, we can make strict assumptions. After calculating the mean and variance of the chosen points, we continue to iterate.

## Results

I run 1000 times the algorithm to see the average performance of it and the correct answer number it gave. If we say that the correctness boundary of the program is when the maximum point it gave is close to the absolute maxima up to 0.01, we can reach the results given below.

![result](https://user-images.githubusercontent.com/12373950/125694109-bffae887-09f8-46fa-b87a-0024026a212c.PNG)

Also, there are snapshots from five different experiments below. 

![5result](https://user-images.githubusercontent.com/12373950/125694259-600c26ae-d43e-4049-8b62-ad652505f4d4.PNG)
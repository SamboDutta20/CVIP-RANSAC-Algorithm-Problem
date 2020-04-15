"""
RANSAC Algorithm Problem
(Due date: Oct. 23, 3 P.M., 2019)
The goal of this task is to fit a line to the given points using RANSAC algorithm, and output
the names of inlier points and outlier points for the line.

Do NOT modify the code provided to you.
Do NOT use ANY API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import ANY library (function, module, etc.).
You can use the library random
Hint: It is recommended to record the two initial points each time, such that you will Not 
start from this two points in next iteration.
"""
import random
def solution(input_points, t, d, k):
    """
    :param input_points:
           t: t is the perpendicular distance threshold from a point to a line
           d: d is the number of nearby points required to assert a model fits well, you may not need this parameter
           k: k is the number of iteration times
           Note that, n for line should be 2
           (more information can be found on the page 90 of slides "Image Features and Matching")
    :return: inlier_points_name, outlier_points_name
    inlier_points_name and outlier_points_name is two list, each element of them is str type.
    For example: If 'a','b' is inlier_points and 'c' is outlier_point.
    the output should be two lists of ['a', 'b'], ['c'].
    Note that, these two lists should be non-empty.
    """
    # TODO: implement this function.
    #raise NotImplementedError
    
    comblist=[]
    comblist_temp=[]
    inlist=[]
    outlist=[]
    min_dist=1000
    r=len(input_points)

    for i in range (k):
    
        a=random.randrange(0,r)
        b=random.randrange(0,r)
        if(a!=b):
            comblist_temp.append(input_points[a]['name'])
            comblist_temp.append(input_points[b]['name'])
            comblist_temp=sorted(comblist_temp)
            if (comblist_temp not in comblist):
                dist=0
            
            
                point1=input_points[a]['value']
                point2=input_points[b]['value']
                x1=point1[0]
                y1=point1[1]
                x2=point2[0]
                y2=point2[1]
                if(x1==x2):
                    x_coeff=1
                    y_coeff=0
                    intercept=-x1
                elif(y1==y2):
                    x_coeff=0
                    y_coeff=1
                    intercept=-y1
                else:
                    x_coeff=(y2-y1)/(x2-x1)
                    y_coeff=-1
                    intercept=y2-x_coeff*x2
            
                c_in_l=0
                in_l=[]
                out_l=[]
                for j in range(len(input_points)):
                    i_point=input_points[j]['value']
                    i_point_x=i_point[0]
                    i_point_y=i_point[1]
                
                    thr=(x_coeff*i_point_x+y_coeff*i_point_y+intercept)
                    if(thr<0):
                        thr=thr*-1
                    thr=thr/((x_coeff*x_coeff+y_coeff*y_coeff)**0.5)
                
                    if(thr<t):
                        in_l.append(input_points[j]['name'])
                        dist+=thr
                        c_in_l+=1
                    else:
                        out_l.append(input_points[j]['name'])
                    
                if(c_in_l-2>=d):
                    dist=dist/((c_in_l-2))
                    if(dist<min_dist):
                        min_dist=dist
                        inlist=in_l
                        outlist=out_l
                
            
                comblist.append(comblist_temp)
                comblist_temp=[]
            comblist_temp=[]
         
            
            
    return(inlist,outlist)
    


if __name__ == "__main__":
    input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},
                    {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},
                    {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},
                    {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]
    t = 0.5
    d = 3
    k = 100
    inlier_points_name, outlier_points_name = solution(input_points, t, d, k)  # TODO
    assert len(inlier_points_name) + len(outlier_points_name) == 8  
    f = open('./results/task1_result.txt', 'w')
    f.write('inlier points: ')
    for inliers in inlier_points_name:
        f.write(inliers + ',')
    f.write('\n')
    f.write('outlier points: ')
    for outliers in outlier_points_name:
        f.write(outliers + ',')
    f.close()



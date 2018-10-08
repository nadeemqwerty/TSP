import numpy as np
import os
import argparse
import time
import sys
def str_to_float(item):
    if isinstance(item,list):
        return [str_to_float(x) for x in item]
    return float(item)


class TSP:
    type =0
    t0 = 0
    t1 = 0
    n = 0
    points = [[]]
    distance = [[]]
    tour = []
    cost = 0
    def __init__(self):
        pass

    
    def take_input(self):
        self.type=input()
        self.n=(int)(input())

        temp=[]
        temp1=[]
        for i in range(self.n):
            x,y=input().split(' ')
            self.points.append([x,y])

        for i in range(self.n):

            temp=input().split()
            temp2=[]
            for j in range(len(temp)):
                x=float(temp[j])
                temp2.append(x)


            temp1.append(temp2)

        self.distance=temp1

    def generate_tour(self):

        
        for i in range(self.n-1):
            (self.tour).append(i)

            self.cost += self.distance[i][i+1]

        self.cost += self.distance[self.n-1][0]
        self.tour.append(self.n - 1)
        
    def greedy_util(self, visited, i):
        mn = 1000000
        pos = 0
        for x in range(self.n):
            if(visited[x] == 0 and self.distance[i][x] < mn and x != i):
                mn = self.distance[i][x]
                pos = x
        return pos

    def generate_greedy(self):
        visited = np.zeros(self.n)
        visited[0] =1
        pos = self.greedy_util(visited,0)
        self.cost += self.distance[0][pos]
        self.tour.append(0)
        self.tour.append(pos)
        visited[pos] = 1
        
        for x in range(self.n-2):
            tem = self.greedy_util(visited,pos)
            visited[tem] = 1
            self.cost += self.distance[pos][tem]
            self.tour.append(tem)
            pos = tem

        self.cost += self.distance[self.tour[-1]][0]
        

    def all_segment(self):
        return [(i,j,k) for i in range(len(self.tour)) for j in range(i+2,len(self.tour)) for k in range(j+2, len(self.tour) + (i>0) )]

    def reverse_if_better(self,i,j,k):

        A = self.tour[i-1]
        B = self.tour[i]
        C = self.tour[j-1]
        D = self.tour[j]

        E = self.tour[k-1]

        F = self.tour[k%self.n]

        d0 = self.distance[A][B] + self.distance[C][D] + self.distance[E][F]
        d1 = self.distance[A][C] + self.distance[B][D] + self.distance[E][F]
        d2 = self.distance[A][B] + self.distance[C][E] + self.distance[D][F]
        d3 = self.distance[A][D] + self.distance[E][B] + self.distance[C][F]
        d4 = self.distance[F][B] + self.distance[C][D] + self.distance[E][A]

        if d0>d1:
            self.tour[i:j] = reversed(self.tour[i:j])

            return -d0+d1
        elif d0 > d2:
            self.tour[j:k] = reversed(self.tour[j:k])
            return d2-d0
        elif d0>d4:
            self.tour[i:k] = reversed(self.tour[i:k])
            return d4-d0
        elif d0>d3:
            tmp = self.tour[j:k]
            tmp=tmp+self.tour[i:j]
            self.tour[i:k] = tmp

            return d3-d0
        return 0

    def three_opt(self):

        delta = 0

        for(a,b,c) in self.all_segment():

            self.t1=time.time()
            if (self.t1-self.t0)>=float(280):

                print("\n")
                for i in range(len(self.tour)):
                	print((self.tour)[i], end=" ")
                sys.exit(0)

            delta += self.reverse_if_better(a,b,c)

        self.cost += delta
        self.t1=time.time()
        if (self.t1-self.t0)>=float(280):
        	print("\n")
        	for i in range(len(self.tour)):
        		print ((self.tour)[i], end =" ")
        	sys.exit(0)


        if delta<0:

            self.three_opt()




def main():
    tsp=TSP()
    tsp.take_input()
    tsp.t0=time.time()
   
    tsp.generate_greedy()
    tsp.three_opt()
    
    for i in range(len(tsp.tour)):
    	print ((tsp.tour)[i],end=" ")
   	

    
    
if __name__ == '__main__':
    main()

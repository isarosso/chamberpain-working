import os
import glob
import pandas
import numpy as np

# def point_in_poly(x,y,poly):

#    # check if point is a vertex
#    if (x,y) in poly: return "IN"

#    # check if point is on a boundary
#    for i in range(len(poly)):
#       p1 = None
#       p2 = None
#       if i==0:
#          p1 = poly[0]
#          p2 = poly[1]
#       else:
#          p1 = poly[i-1]
#          p2 = poly[i]
#       if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
#          return "IN"
      
#    n = len(poly)
#    inside = False

#    p1x,p1y = poly[0]
#    for i in range(n+1):
#       p2x,p2y = poly[i % n]
#       if y > min(p1y,p2y):
#          if y <= max(p1y,p2y):
#             if x <= max(p1x,p2x):
#                if p1y != p2y:
#                   xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
#                if p1x == p2x or x <= xints:
#                   inside = not inside
#       p1x,p1y = p2x,p2y

#    if inside: return "IN"
#    else: return "OUT"


    	  #   if df.tail(1)[['Date']].values==date_inp:
  #   	active = np.array(df[df.Date==date_inp][['Lat','Lon']].values)
  #   	xend,yend = m(active[:,1],active[:,0])
  #   	m.plot(xend,yend,'ro',markersize = 6)
#      else:
		# inactive = np.array(df[df.Date==date_inp][['Lat','Lon']].values)	    
		# xend,yend = m(inactive[:,1],inactive[:,0])
		# m.plot(xend,yend,'bo',markersize = 6)
	return m
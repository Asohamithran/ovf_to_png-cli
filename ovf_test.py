#!/usr/bin/env python
from ovf import ovf 
import matplotlib.pyplot as plt
import numpy as np
#read all the segments properly
#no need to give the length of the header 
#plot for all different length of data
filename = "test.ovf"
# configure to your taste to see what do the indices mean 
# segment has the information about the number of cells
# first read the segment head and then read data from the segment
data = np.zeros(20,dtype='f')
data[1] = 21
import argparse as ap
parser = ap.ArgumentParser(prog= 'ovf_to_png',add_help =False)
parser.add_argument('-h', action ='help',
        help='this program creates a png file for the omf file passed as the argument')
parser.add_argument('ovf_filename')
args = parser.parse_args()
filename=(args.ovf_filename)

#I have added this line now and its new
#def func1(filename):
    #with ovf.ovf_file(filename) as ovf_file:
        #segment =ovf.ovf_segment(n_cells=[20,0,0],comment="cells are added")
        #ovf_file.write_segment(segment, data)
        #print(ovf_file.n_segments)
        #print(segment.n_cells[0],segment.n_cells[1],segment.n_cells[2])
    ## reading the ovf file
    #with ovf.ovf_file(filename) as ovf_file:
        #rec_data=np.zeros(data.shape,dtype='f')
        #ovf_file.read_segment_header(0,segment)
        #ovf_file.read_segment_data(0,segment,rec_data)
        #print(type(segment))
        #print(rec_data)
        #return
#def func3(filename2):
    #with ovf.ovf_file(filename2) as ovf_file:
        #some_segment=ovf.ovf_segment()
        #n = ovf_file.n_segments
        #ovf_file.read_segment_header(1,some_segment)
        #print("the number of segments are ",n)
        #data_shape= (some_segment.n_cells[0],some_segment.n_cells[1],
                    #some_segment.n_cells[2],3) 
        #print(data_shape)
        #record_data = np.zeros(data_shape,dtype='f')
        #ovf_file.read_segment_data(1,some_segment,record_data)
        #return
# read the ovf file 
def get_mag(x_flat,y_flat):
    mag= np.empty_like(x_flat)
    for i,j,k in zip(x_flat,y_flat,range(len(x_flat))):
        mag[k]=(np.sqrt(i**2+j**2))
    return mag
def visualise(image_data,index):
    # make the meshgrid (u,v)
    # plot the graph with parameters solely from the image data 
    nodes = len(image_data[:,:,:,0])
    U,V =np.meshgrid(np.arange(nodes),np.arange(nodes))
    u=image_data[:,:,:,0]
    v=image_data[:,:,:,1]
    #print(p)
    #print('the node is ',nodes)
    u_flat=u.ravel()
    v_flat=v.ravel()
    mag=get_mag(u_flat,v_flat)

    mag=mag.reshape(nodes,nodes)
    #print(mag.shape)
    plt.contourf(U,V,mag)
    #plt.quiver(U,V,u,v)
    plt.quiver(U,V,u_flat,v_flat)
    plt.title(f'spin_x/spin_y:{np.round(np.max(mag),2)}to{np.round(np.min(mag),2)}')
    plt.xlabel('x_nodes')
    plt.ylabel('y_nodes')
    plt.colorbar()
    plt.savefig(f'spin data header-{index}')
    plt.close()
    #print(len(mag))
    #plt.show()

    return

def func2(filename,dim):
    with ovf.ovf_file(filename) as ovf_file:
        some_segment=ovf.ovf_segment()
        n = ovf_file.n_segments
        print("the number of segments are ",n)
#
        for i in range (n):
            ovf_file.read_segment_header(i,some_segment)
            data_shape= (some_segment.n_cells[0],some_segment.n_cells[1],
                        some_segment.n_cells[2],3) 
#
            record_data = np.zeros(data_shape,dtype='f')
            ovf_file.read_segment_data(i,some_segment,record_data)

#
            visualise(record_data,i)
            #if (dim =='x'or dim =='X'):
                #print("spin_x",record_data[:,:,:,0])
            #elif (dim =='y'or dim =='Y'):
                #print("spin_y",record_data[:,:,:,1])
            #elif (dim =='z'or dim =='Z'):
                #print ("spin_y",record_data[:,:,:,2])
        return

dim='z'
#try:
    #dim =input("enter the dimension x or y or z")
#except EOFError:
    #print("eof error encountered")
func2(filename,dim)
#func3(filename2)

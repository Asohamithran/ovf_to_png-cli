#!/usr/bin/env python
from ovf import ovf 
import matplotlib.pyplot as plt
import numpy as np
import argparse as ap
parser = ap.ArgumentParser(prog= 'ovf_to_png',add_help =False)
parser.add_argument('-h', action ='help',
        help='this program creates a png file for the omf file passed as the argument')
parser.add_argument('ovf_filename')
parser.add_argument('-show_plot',required =False,action='store_true',
        help='-show plot will display the plot for each segment in a window')

args = parser.parse_args()
filename=(args.ovf_filename)
show_plot= args.show_plot
print(show_plot)

# read the ovf file 
def get_mag(x_flat,y_flat):
    mag= np.empty_like(x_flat)
    for i,j,k in zip(x_flat,y_flat,range(len(x_flat))):
        mag[k]=(np.sqrt(i**2+j**2))
    return mag
def visualise(image_data,index,sp):
    # make the meshgrid (u,v)
    # plot the graph with parameters solely from the image data 
    nodes = len(image_data[:,:,:,0])
    U,V =np.meshgrid(np.arange(nodes),np.arange(nodes))
    u=image_data[:,:,:,0] # x_dimension
    v=image_data[:,:,:,1] # y_dimension
    w=image_data[:,:,:,2] # z_dimension

    #print(p)
    #print('the node is ',nodes)
    u_flat=u.ravel()
    v_flat=v.ravel()
    w_flat=w.ravel()
    mag=get_mag(u_flat,v_flat)

    mag=mag.reshape(nodes,nodes)
    #print(mag.shape)
    plt.contourf(U,V,mag)
    #plt.quiver(U,V,u,v)
    # adjusted for scaling
    plt.quiver(U,V,u_flat,v_flat,angles='xy',scale_units='xy',scale=1.0)
    plt.title(f'spin_x/spin_y:{np.round(np.max(mag),2)}to{np.round(np.min(mag),2)}')
    plt.xlabel('x_nodes')
    plt.ylabel('y_nodes')
    plt.colorbar()
    plt.savefig(f'spin data header-{index}')
    #print(len(mag))
    if(sp == True):
        plt.show()
        return

    else:
        plt.close()
        return


def func2(filename,dim,show_plot):
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
            visualise(record_data,i,show_plot)
        return

dim='z'
func2(filename,dim,show_plot)
#func3(filename2)

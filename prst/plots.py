import numpy as np
import plotly.graph_objects as go

def plot_3d(G,block,property,min,max):
    
    block_cord=[]
    for i in block:
        block_cord_1=[]
        for x in G.cells.faces[G.cells.facePos[i,0] : G.cells.facePos[i+1,0]][:,0]:
            for y in G.faces.nodes[G.faces.nodePos[x,0] : G.faces.nodePos[x+1,0]][:,0]:
                node_cord = G.nodes.coords[y]
                if(block_cord_1==[]):
                    block_cord_1.append(node_cord)
                else:
                    p=1
                    for z in block_cord_1:
                        if(z[0]==node_cord[0] and z[1]==node_cord[1] and z[2]==node_cord[2]):
                            p=0
                    if(p==1):
                        block_cord_1.append(node_cord)
                        
        block_cord.append(np.array((block_cord_1[7],block_cord_1[3],block_cord_1[2],block_cord_1[6],
                                block_cord_1[4],block_cord_1[0],block_cord_1[1],block_cord_1[5])))
    
    prop = property
    rw=0
    x1=[block_cord[rw][0][0],block_cord[rw][1][0],block_cord[rw][2][0],block_cord[rw][3][0],block_cord[rw][4][0],block_cord[rw][5][0],block_cord[rw][6][0],block_cord[rw][7][0]]
    y1=[block_cord[rw][0][1],block_cord[rw][1][1],block_cord[rw][2][1],block_cord[rw][3][1],block_cord[rw][4][1],block_cord[rw][5][1],block_cord[rw][6][1],block_cord[rw][7][1]]
    z1=[block_cord[rw][0][2],block_cord[rw][1][2],block_cord[rw][2][2],block_cord[rw][3][2],block_cord[rw][4][2],block_cord[rw][5][2],block_cord[rw][6][2],block_cord[rw][7][2]]
    prop1=(np.ones(8)*prop[rw]).tolist()
    block1=[str(int(rw))]*8
    i1 = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
    j1 = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
    k1 = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6]

    for rw in range(1,len(block_cord)):
        x1.extend([block_cord[rw][0][0],block_cord[rw][1][0],block_cord[rw][2][0],block_cord[rw][3][0],block_cord[rw][4][0],block_cord[rw][5][0],block_cord[rw][6][0],block_cord[rw][7][0]])
        y1.extend([block_cord[rw][0][1],block_cord[rw][1][1],block_cord[rw][2][1],block_cord[rw][3][1],block_cord[rw][4][1],block_cord[rw][5][1],block_cord[rw][6][1],block_cord[rw][7][1]])
        z1.extend([block_cord[rw][0][2],block_cord[rw][1][2],block_cord[rw][2][2],block_cord[rw][3][2],block_cord[rw][4][2],block_cord[rw][5][2],block_cord[rw][6][2],block_cord[rw][7][2]])
        prop1.extend((np.ones(8)*prop[rw]).tolist())
        block1.extend([str(int(rw))]*8)
        i1.extend((np.array([7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2])+8*rw).tolist())
        j1.extend((np.array([3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3])+8*rw).tolist())
        k1.extend((np.array([0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6])+8*rw).tolist())

    prop2=[str(x) for x in prop1]
    prop3=[str(i) + '  ' + str(j) for i, j in zip(block1, prop2)]
    
    del block_cord,block_cord_1,prop
    
    fig = go.Figure(data=[
    go.Mesh3d(
    # 8 vertices of a cube
    x=x1,
    y=y1,
    z=z1,
    # set colour scale
    colorscale=[[min/(min+max), 'white'],[0.5, 'blue'],[max/(min+max), 'green']],
    cmax = max,
    cmin = min,
    # Intensity of each vertex, which will be interpolated and color-coded
    intensity = prop1,
    # i, j and k give the vertices of triangles
    i = i1,
    j = j1,
    k = k1,
    showscale=True,
    hoverinfo='text+x+y+z',
    hovertext = prop3
        )
    ])
                
    fig.update_layout(scene=dict(xaxis_showspikes=False,
                             yaxis_showspikes=False,
                             zaxis_showspikes=False))
    
    return fig
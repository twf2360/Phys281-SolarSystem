x = [[1,2,3], [1,2,3]]
i = 0 
listsoflists = []

for y in x[0]:
    i +=1 
    listsoflists.append(i)

print(listsoflists)

    



   for y in range(len(lob)):
            print(lob[y])
            xplot =[]
            yplot =[]
            zplot =[]
            for x in range(len(lob[0])):
                
                xplot.append(lob[y][x].position[0])
                yplot.append(lob[y][x].position[1])
                zplot.append(lob[y][x].position[2])
            ax = plt.axes(projection = '3d')
            ax.plot3D(xplot, yplot, zplot, label = '{} Orbit'.format(lob[y][0].Name)) 
        plt.show()
            


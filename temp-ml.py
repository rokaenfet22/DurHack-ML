#assuming input is imported to here someway
#input of array of a single img of the posenet output
def find_state_within_pushup_rep(inp):

    try:
        f=open("initial.txt","r")
        (max_y,min_y,forgive)=f.split()
    except:
        f=open("intiial.txt","w"):
        #Don't what the inp looks like yet
        f.write(str(1)+" "+str(1)+" "+str(1))
        (max_y,min_y,forgive)=[1,1,1]
    f.close()

    head_y=1.3 #also temp input

    if head_y>=max_y-forgive:
        motion="top"
    elif head_y<=min_y+forgive:
        motion="bottom"
    else:
        motion="moving"
    return motion

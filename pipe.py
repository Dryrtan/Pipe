#!/usr/bin/python
# Coded by Dryrtan - https://github.com/Dryrtan
import sys,math

print ""
print ""
print "EXPANSION CHAMBER DESIGN"
print ""
print "INTRODUCTION"
print """This program aims to help the user calculate the dimensions
of a two-stroke's expansion chamber. You will need to know:
The area of the exhaust port,
The exhaust port open duration in degrees,
The engine's peak horsepower RPM's (the program can help you to estimate this)
The cylinder capacity.

Just type in the information requested and the program
will return the chamber dimensions.
At the prompts throughout this program, you can enter "q" to quit, or "h"
for help and to see more information.

IMPORTANT- If you are using this for the first time, you should type "h" at
each prompt and read the information shown."""
print ""

print "NOTE: All dimensions should be given in millimetres."
print ""
keepon=raw_input("Press <enter> to continue..")
print ""

print """First, we need to determine how the engine will be used.
Below is a list of typical engine applications together with a
number. Type in the appropriate number for your application,
then press <enter>. For example, if you are building an enduro
engine you should have: ENGINE TYPE =2 """

print ""
print "ENGINE USAGE LISTING "
print "Roadster-1"
print "Enduro-2"
print "Motocrosser-3"
print "Grand Prix-4 "
print ""
while __name__=="__main__":
    engtype=raw_input("ENGINE TYPE= ")
    if  engtype=="1":
        bmep=5
        k0=0.7
        k1=1.125
        k2=2
        extmp=400
        usage="Roadster"
        break
    else:
        if engtype=="2":
            bmep=8
            k0=0.7
            k1=1.125
            k2=2.25
            extmp=500
            usage="Enduro"
            break
        else:
            if engtype=="3":
                bmep=9.5
                k0=0.65
                k1=1.1
                k2=2.75
                extmp=580
                usage="Motocrosser"
                break
            else:
                if engtype=="4":
                    bmep=11
                    k0=0.6
                    k1=1.05
                    k2=3.25
                    extmp=650
                    usage="GrandPrix"
                    break
                else:
                    if engtype=="q":
                        sys.exit()
                    else:
                        if engtype=="h":
                            print """As you can see there are four choices here: Roadster, Enduro, Motocross
and GrandPrix. Using the roadster type will produce a pipe with a mild but
fairly flat powerband, while at the other extreme choosing the GrandPrix type
will produce a pipe that makes maximum horsepower over a very narrow RPM
range. Try to select a type that matches your engine's porting and intended
usage, ie. don't try a GrandPrix type pipe on a stock trailbike - you'll be
disappointed. Most high-performance street bikes will probably work best using
the enduro or mx type pipe. Always remember that in designing for maximum
acceleration you should aim for the highest AVERAGE horsepower over the
engines usable rev range. Impressive numbers at max. RPM are meaningless if
your competition has just passed you while you wait for your engine to pull itself
into the powerband."""
                        else:
                            print "Invalid Engine Type Number..try again...."
print""
from math import *
pwv=sqrt(401.80*extmp)#the pressure wave velocity or the speed of the sound waves thru the exhaust
print""
print """Now we need to know the area of the exhaust port in sq.mm.
Type in the area at the prompt. For help and more info on
measuring and calculating the area, enter "h", or "q" to
quit."""
print""
import string
from string import atof
while __name__=="__main__":
    exarea=raw_input("PORT AREA= ")
    print ""
    if exarea=="h":
        print"""If the port is a simple square or rectangular shape, calculating the
area is simply a matter of multiplying the width and height. Just
remember to measure the width in a straight line across the port,
don't follow the curve of the cylinder. Unfortunately, most ports
are not simple rectangles, and are often quite irregular in shape.
One method is to measure the width at various points,(say 1mm
increments from bottom to top) using inside calipers and the piston
crown as aid to keeping the calipers "square". The first measurement
should be taken 1mm above the bottom edge of the port, while the last
should be across the top edge. Add all the widths and divide this figure
by the number of measurements to get the area. Use whatever patience
and ingenuity is required to get an accurate figure as any sloppiness
here will affect the accuracy of the chamber dimensions. Type in the
area, or "q" to quit."""
        print ""
    else:
        if exarea=="q":
            sys.exit()
        else:
            exarea=atof(exarea)
            break
print""
print """Okay, now we need the exhaust port timing.Type in the port duration in
degrees, eg. PORT DURATION=188. For more information, and help with
measuring the port timing, enter "h", or "q" to quit."""
print""
while __name__=="__main__":
    exdur=raw_input("PORT DURATION=")
    if exdur=="q":
        sys.exit()
    else:
        if exdur=="h":
            print """The port duration is simply a measurement of the number of degrees of
crankshaft rotation between the port opening and closing. For example,
if the port opens 92 degrees before BDC,(and closes 92deg after BDC),
the duration will be 184 degrees. Measure by attaching a graduated
degree wheel to the end of the crankshaft.
     If the top edge of the port is significantly curved, the effective
duration will be somewhat less than that measured. You'll have to use
your own judgement here, however a reduction of 5 to 10 degrees
should be close. Type in the duration or enter "q" to quit."""
        else:
            exdur=atof(exdur)
            break
print ""
print """Now an easy one. Enter the cylinder capacity in cubic centimetres-
if the engine is multi-cylindered, use the capacity of one cylinder only.
(round the number to the nearest cc)."""
while __name__=="__main__":
    print ""
    disp=raw_input("UNIT CYLINDER DISPLACEMENT IN CC's= ")
    print ""
    if disp=="q":
        sys.exit()
    else:
        if disp=="h":
            print """Cylinder capacity=(bore/2) x (bore/2) x 3.142 x stroke,
where bore and stroke are in centimetres."""
        else:
            disp=atof(disp)
            break
meanarea=exarea*0.0072
meanareaoverdisp=meanarea/disp
time=0.000145/meanareaoverdisp
bestrpm=(exdur/time)/6
bestrpm=round(bestrpm,0)
print """The RPM's at which the engine will produce maximum power has been
estimated at """,bestrpm
print """Enter "y" at the prompt below to accept this figure, or "n" to see
more information on selecting an alternative"""
print ""
while __name__=="__main__":
    pickrevs=raw_input("Accept suggested RPM's? y/n ")
    if pickrevs=="q":
        sys.exit()
    else:
        if pickrevs=="n":
            print """The suggested RPM figure to use in calculating the pipe dimensions
should be reasonably accurate providing the exhaust is a fairly regular
shape.If the port is assymetrical, ie. the top half of the port is markedly
different in shape to the bottom half, you should work out the port time/area
figure manually to find a suitable RPM number.If you elect to use your own
RPM figure you should make sure it closely matches the port characteristics of
the engine. Any mismatching of the pipe and the port time/areas (or any engine
components for that matter) will give disappointing results."""
            revs=input("RPM's= ")
            break
        else:
            if pickrevs=="y":
                revs=bestrpm
                break
#ok now we can calculate the tuned length of the system using the formula
#tuned length=1000*pressure wave velocity*exhaust duration in degrees divided by
#12*engineRPMs. Lets do it in a couple of steps and call the tuned length tl
step1=1000*pwv*exdur
step2=12*revs
tl=step1/step2
#exd= the sqrt of (exarea*4/pi) we'll do it in a couple of steps.*/
ea4pi=exarea*4/pi
exd=sqrt (ea4pi)#exd=the exhaust port's effective dia.
lp01=0.1*tl;Lp01=round(lp01,2);LP01=str(Lp01)#length of the engine pipe measured from the piston skirt to the diffuser entry
lp12=0.41*tl;Lp12=round(lp12,2);LP12=str(Lp12)#length of the 1st diffuser stage
lp23=0.14*tl;Lp23=round(lp23,2);LP23=str(Lp23)#length of the 2nd diffuser stage
lp34=0.11*tl;Lp34=round(lp34,2);LP34=str(Lp34)#length of the belly section
lp45=0.24*tl;Lp45=round(lp45,2);LP45=str(Lp45)#length of the plugging cone
lp56=0.24*tl;Lp56=round(lp56,2);LP56=str(Lp56)#length of the outlet pipe
oal=lp01+lp12+lp23+lp34+lp45+lp56;Oal=round(oal,2);OAL=str(Oal)#the pipe's overall length
d1=k1*exd;dd1=round(d1,2);D1=str(dd1)#the engine pipe dia. (ie. the pipe from the port face to the diffuser entry
d3=k2*exd;dd3=round(d3,2);D3=str(dd3)#the dia. of the big end of the first diffuser stage / little end of the second stage
d4=k0*exd;dd4=round(d4,2);D4=str(dd4)#the dia. of the big end of the 2nd diffuser stage / belly section / big end of plugging cone
d2=0.67658*d3;dd2=round(d2,2);D2=str(dd2)#the outlet pipe dia.
###########################################################################
###########################################################################
def conepattern(d10,d11,d12,g29,g30):
    #this is a function for calculating the dimensions of a pattern used to roll a cone from sheetmetal.
    #you need to import the math module to run this function
    #d10 is the cones large diameter
    #d11 is the cones small dia.
    #d12 is the axial length of the cone
    #g29 specifies the cone in question...
    #g30 specifies output to screen or file
    g11=(d10-d11)/2  #find the included angle of the cone
    #now we get opp/adj
    g12=g11/d12
    #now we find the angle of tan g11/d12
    from math import *
    g13=atan(g12)
    g14=g13*57.3 #this converts from radians to degrees
    d13=g14*2 #this doubles the angle to give the cones included angle
    D13=round(d13,2)
    global DD13
    DD13=str(D13)
    #now we find the long radius of the pattern
    g15=d10*0.5 #step1 halves the cone large dia.
    #g13 is half the included angle in radians
    g16=sin(g13) #this is the sine of g13
    d14=g15/g16 #this is the long radius
    D14=round(d14,2)
    global DD14
    DD14=str(D14)
    #next we find the length of the side of the cone
    g17=d12*d12
    g18=g11*g11
    g19=g17+g18
    d16=sqrt(g19) #this is the cone side length
    d15=d14-d16 #the short radius
    D15=round(d15,2)
    global DD15
    DD15=str(D15)
    g21=pi*d10
    #next the circumference of the long rad.circle
    g22=d14*2*pi
    #now we divide the cone big circumference by circle circ.
    g23=g21/g22
    #find included angle by multiplying g23 by 360
    g24=g23*360
    G24=round(g24,2)
    global GG24
    GG24=str(G24)
    #now we find the chord lengths
    #chord length = sine of half include angle x radius
    #first find half included angle and convert to radians
    g25=(g24/2)/57.3
    g26=sin(g25)
    #then multiply sine of angle by radius and double to get length of complete chord
    g27=g26*d14*2
    G27=round(g27,2)
    global GG27
    GG27=str(G27)
    g28=g26*d15*2
    G28=round(g28,2)
    global GG28
    GG28=str(G28)
    global bigarc
    bigarc="The outer arc has a radius of "
    global lilarc
    lilarc="The inner arc has a radius of "
    global bigchord
    bigchord="The chord across the outer arc has a length of "
    global lilchord
    lilchord="The chord across the inner arc has a length of "
    global segangle
    segangle="The sides of the piece to be cut out form an included angle of "
    global coneangle
    coneangle="The completed cone will have an angle of "
    degr=" degrees."
    global thecone
    if g29==1:
        thecone="First diffuser stage:"
    else:
        if g29==2:
            thecone="Second diffuser stage:"
        else:
            if g29==3:
                thecone="Plugging cone:"
    if g30==11:
        print thecone
        print bigarc,D14
        print lilarc,D15
        print bigchord,G27
        print lilchord,G28
        print segangle,G24,degr
        print coneangle,D13,degr
        print ""
    else:
        if g30==22:
            pass
####################################################################################
welcome="   EXPANSION CHAMBER DIMENSIONS"
summaryintro="These are the pipe dimensions for a "
intropart2="type engine with the following dimensions:"
revstring= str(revs)
exareastring=str(exarea)
sqmm="square millimetres."
exdurstring=str(exdur)
epd="Engine pipe diameter="
epl="Engine pipe length="
fdld="First diffuser cone large dia.="
fcl="First diffuser cone length="
sdld="Second diffuser cone large dia.="
sdcl="Second diffuser cone length="
bsl="Belly section length="
pcsd="Plugger cone small dia.="
pcl="Plugger cone length="
opd="Outlet pipe dia.="
opl="Length of outlet pipe="
ovel="Overall length of chamber="
nline=" \n" #this is just to print output to separate lines
portdims="The exhaust port has an area of "
Revss="The peak h.p. rpms are "
duration="The port open duration is "
degrs=" degrees."
note1="""NOTE: This includes the the port length as measured
from the port window to the pipe mounting flange."""
note2="REMEMBER that this includes the port length and the outlet pipe."
print "====================================================="
print "====================================================="
#everything in this block are dims. output to screen
print welcome
print ""
print summaryintro,usage
print intropart2
print portdims,exareastring,sqmm
print duration,exdurstring,degrs
print Revss,revstring
print ""
print "  DIMENSIONS"
print epd,D1
print ""
print epl,LP01
print note1
print ""
print fdld,D2
print ""
print fcl,LP12
print ""
print sdld,D3
print ""
print sdcl,LP23
print ""
keepon=raw_input("Press <enter> to continue..")
print ""
print bsl,LP34
print ""
print pcsd,D4
print ""
print pcl,LP45
print ""
print opl,LP56
print ""
print ovel,OAL
print ""
print note2
print ""
print "====================================================="
print "====================================================="
print ""
print """Now that the expansion chamber dimensions are known,
we can also show the dimensions of the sheetmetal pieces that
will be cut out and rolled into cones.(press "n" to skip this bit)"""
patternresponse=raw_input("Show sheetmetal marking-out details? y/n ")
print ""
if patternresponse=="q":
    sys.exit()
else:
    if patternresponse=="y":
        print """The sheetmetal will be cut into fan shaped segments for each cone.Each segment
has a long and a short radius, an included angle and chord lengths across
both the arcs.The chords are simply straight lines drawn between the 'points'
or ends of each arc. In practice, only the two radii and the chord length of
the large arc are required.Just scribe the two arcs,then draw a line from
any point on the big arc to the centre.Measure across the big arc a distance
equal to the outer arc's chord length, and mark. Then draw another line from
this mark back to the centre point.That's all there is to it.If you wish, you
can double check your work by measuring the included angle or the smaller arc's
chord length."""
        print ""
        print ""
        conepattern(d2,d1,lp12,1,11)
        print ""
        keepon=raw_input("Press <enter> to continue..")
        print ""
        conepattern(d3,d2,lp23,2,11)
        print ""
        keepon=raw_input("Press <enter> to continue..")
        print ""
        conepattern(d3,d4,lp45,3,11)
        print ""
#this next section sends the dims. to a file for later reading or printing out
print "If you wish, you can save the results to a file"
print "for future reference or printing out."
saver=raw_input("Save to file? y/n ")
print ""
if saver=="y":
    print """You need to name the path to the file to be used. Type in the complete
pathname, or enter "h" for help, or "q" to quit."""
    while __name__=="__main__":
        userspath=raw_input("Path= ")
        if userspath=="q":
            sys.exit()
        else:
            if userspath=="h":
                print """The pathname shows the location or 'address' of a file on your disk. For example
a pathname of C:\my_documents\suzuki.txt on a Windows system describes a file
named 'suzuki.txt' located in a folder named 'my_documents' which in turn is
located on the disk 'C:'. Note the ':' and the backslashes. On a Linux box you
could use something like '/home/me/suzuki.txt'. If the file doesn't yet exist,
it will be created. If the file already exists, however, it will be overwritten,
so check first if you are not sure.
    Typing the only the filename will put the file into the current directory.
    If you prefer, you can just press "d" to accept the default pathname which will
write to a file named 'pipe.txt' in the current directory."""
            else:
                if userspath=="d":
                    userspath="pipe.txt"
                    break
                else:
                    try:
                        f=open(userspath, 'w')
                    except:
                        print "Oops! Invalid pathname, try again."
                    else:
                        break
    f=open(userspath, 'w')
    f.write (nline)
    f.write (welcome)
    f.write (nline)
    f.write (summaryintro);f.write (usage)
    f.write (nline)
    f.write (intropart2)
    f.write (nline)
    f.write (portdims);f.write (exareastring);f.write (sqmm)
    f.write (nline)
    f.write (duration);f.write (exdurstring);f.write (degrs)
    f.write (nline)
    f.write (Revss);f.write (revstring)
    f.write (nline);f.write (nline)
    f.write (epd);f.write (D1)
    f.write (nline);f.write (nline)
    f.write (epl);f.write (LP01)
    f.write (nline)
    f.write (note1)
    f.write (nline);f.write (nline)
    f.write (fdld);f.write (D2)
    f.write (nline);f.write (nline)
    f.write (fcl);f.write (LP12)
    f.write (nline);f.write (nline)
    f.write (sdld);f.write (D3)
    f.write (nline);f.write (nline)
    f.write (sdcl);f.write (LP23)
    f.write (nline);f.write (nline)
    f.write (bsl);f.write (LP34)
    f.write (nline);f.write (nline)
    f.write (pcsd);f.write (D4)
    f.write (nline);f.write (nline)
    f.write (opl);f.write (LP56)
    f.write (nline);f.write (nline)
    f.write (ovel);f.write (OAL)
    f.write (nline)
    f.write (note2)
    f.write (nline);f.write (nline)
    ###########################this is where the layout dims. start
    f.write ("Sheetmetal Marking-Out Dimensions")
    f.write (nline)
    conepattern(d2,d1,lp12,1,22)
    f.write (thecone)
    f.write (nline)
    f.write (bigarc);f.write (DD14)
    f.write (nline)
    f.write (lilarc);f.write (DD15)
    f.write (nline)
    f.write (bigchord);f.write (GG27)
    f.write (nline)
    f.write (lilchord);f.write (GG28)
    f.write (nline)
    f.write (segangle);f.write (GG24);f.write (degrs)
    f.write (nline)
    f.write (coneangle);f.write (DD13);f.write (degrs)
    f.write (nline);f.write (nline)
    conepattern(d3,d2,lp23,2,22)
    f.write (thecone)
    f.write (nline)
    f.write (bigarc);f.write (DD14)
    f.write (nline)
    f.write (lilarc);f.write (DD15)
    f.write (nline)
    f.write (bigchord);f.write (GG27)
    f.write (nline)
    f.write (lilchord);f.write (GG28)
    f.write (nline)
    f.write (segangle);f.write (GG24);f.write (degrs)
    f.write (nline)
    f.write (coneangle);f.write (DD13);f.write (degrs)
    f.write (nline);f.write (nline)
    conepattern(d3,d4,lp45,3,22)
    f.write (thecone)
    f.write (nline)
    f.write (bigarc);f.write (DD14)
    f.write (nline)
    f.write (lilarc);f.write (DD15)
    f.write (nline)
    f.write (bigchord);f.write (GG27)
    f.write (nline)
    f.write (lilchord);f.write (GG28)
    f.write (nline)
    f.write (segangle);f.write (GG24);f.write (degrs)
    f.write (nline)
    f.write (coneangle);f.write (DD13);f.write (degrs)
    f.write (nline)
    f.close ()
    print "Results have been written to ",userspath
else:
    print "Bye."

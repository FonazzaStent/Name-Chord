"""Name Chord 1.0.1 - Name a chord from a group of notes.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
note=''
steps=[[0, 1, 3, 4, 6, 8, 10, 0], [0, 1, 3, 5, 6, 8, 10, 0], [0, 1, 3, 5, 7, 8, 10, 0], [0, 1, 3, 5, 7, 9, 10, 0], [0, 2, 3, 5, 6, 8, 10, 0], [0, 2, 3, 5, 7, 8, 10, 0], [0, 2, 3, 5, 7, 9, 10, 0], [0, 2, 3, 5, 7, 9, 11, 0], [0, 2, 4, 5, 7, 8, 10, 0], [0, 2, 4, 5, 7, 9, 10, 0], [0, 2, 4, 5, 7, 9, 11, 0], [0, 2, 4, 6, 7, 9, 10, 0], [0, 2, 4, 6, 7, 9, 11, 0], [0, 2, 4, 6, 8, 9, 11, 0]]
stepsitem=[]
stepscale=[]
stepscales=[]


def init():
    global scale
    global scales
    global stepstransposed
    global chordsteps
    scale=[]
    scales=[]
    stepstransposed=[]
    chordsteps=[]
    

def name_chord():
    global chord
    global root
    global chordsteps
    root=1
    notesinput=''
    chordstring=''
    noteslist=[]
    chord=[]
    check=False
    notesinput=input("Input notes (q to quit): ")
    if notesinput=="q":
        quit()
    chord=notesinput.split(" ")
    n=1
    for item in notes:
        if chord[0]==item:
            root=n
        n=n+1
    x=1
    for singlenote in chord:
        for item in notes:
            if singlenote==item:
                chordsteps.append(x)
            x=x+1
        x=1
    #print (chordsteps)

            
    for singlenote in chord:
        for item in notes:
            if singlenote==item:
                check=True
        if check==False:
            chord.remove(singlenote)
        check=False
    for singlenote in chord:
        for item in notes:
            if singlenote==item:
                chordstring=chordstring+singlenote+" "

    #print (chordstring)
        
    chordname=[]
    chordname_string=""

    chord_notes=[]


    chord_length=len(chord)
    chordname_string=''
    for n in range (0,12):
        if chord[0]==notes[n]:
            index=n
            for i in range (0,12):
                chord_notes.append(notes[index])
                index=index+1
                if index>11:
                    index=0

    chordname.append(chord[0])

    sus=False
    sus_index=999
    ninth=False
    ninth_index=999
    seventh_maj=False
    seventh_maj_index=999
    seventh=False
    seventh_index=999
    sixth=False
    sixth_index=999
    eleventh=False
    eleventh_index=999
    ninth_maj=False
    ninth_maj_index=999
    thirteenth=False
    maj=False
    minr=False
    plusninth=False
    mincheck=False
    bfive=False
    fifth=False
    dim=False
    aug=False
    add_fifth=False
    minr_index=999
    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        #print (step)
        if step==5:
            maj=True
            minr=False
        if step==4:
            minr=True
            maj=False
        if maj==True and minr==True and plusninth==False:
            plusninth=True
            minr=False
            chordname.append(" 9+")
            plusninth_index=len(chordname)
        elif minr==True and mincheck==False:
            chordname.append("m ")
            minr_index=len(chordname)
            mincheck=True
        if step==8:
            fifth=True

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        if step==6 and sus==False:
            sus=True
            chordname.append(" Sus")
            sus_index=len(chordname)
        if minr==True and step==7 and dim==False and fifth==False:
            dim=True
            chordname.append(" Dim")
            dim_index=len(chordname)
            if minr_index!=999:
                chordname[minr_index-1]='delete'
        if dim==False and step==7 and bfive==False:
            bfive=True
            chordname.append(" Add5b")
            bfive_index=len(chordname)
        if step==9 and fifth==False and aug==False:
            aug=True
            chordname.append(" Aug")
            aug_index=len(chordname)-1
        if step==9 and fifth==True and add_fifth==False:
            add_fifth_plus=True
            chordname.append(" Add5+")
            add_fifth_plus_index=len(chordname)
        if step==10:
            sixth=True
            chordname.append(" 6")
            sixth_index=len(chordname)
        if step==11:
            seventh=True
            chordname.append(" 7")
            seventh_index=len(chordname)

        if step==12:
            seventh_maj=True
            chordname.append(" 7maj")
            seventh_maj_index=len(chordname)
        if step==3 and seventh==True:
            ninth=True
            chordname.append(" 9")
            ninth_index=len(chordname)
            if seventh_index!=999: 
                chordname[seventh_index-1]='delete'
        if step==3 and sus==False and seventh_maj==True:
            ninth_maj=True
            chordname.append(" 9maj")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'
        if step==3 and seventh_maj==False and seventh==False:
            add_ninth=True
            chordname.append(" Add9")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'        
        if step==2:
            ninthb=True
            chordname.append(" Add9b")
            ninthb_index=len(chordname)
        if ninth==True and sus==True and sixth==False and(seventh==True or seventh_maj==True):
            eleventh=True
            chordname.append(" 11")
            eleventh_index=len(chordname)

            chordname[ninth_index-1]='delete'
            chordname[sus_index-1]='delete'

        if ninth==True and sus==True and sixth==True and(seventh==True or seventh_maj==True):
            thirteenth=True
            chordname.append(" 13")
            thirteenth_index=len(chordname)
            if ninth_index!=999:
                chordname[ninth_index-1]='delete'
            if sixth_index!=999:
                chordname[sixth_index-1]='delete'
            if sus_index!=999:

                chordname[sus_index-1]='delete'
            if seventh_index!=999:

                chordname[seventh_index-1]='delete'
            if eleventh_index!=999:
                chordname[eleventh_index-1]='delete'
            

    length=len(chordname)           
    for x in range(0,length):

        if chordname[x]!='delete':
            chordname_string=chordname_string+chordname[x]

    print ("\n")
    print ("Chord: ",chordstring)
    print ("\n")
    print ("Chord name: ",chordname_string)
    print ("\n")
    note=''

def guess_scale():
    global match
    global matchlist
    global scale
    global scales
    global stepstransposed
    global stepsitem
    global root
    global stepscale
    global stepscales
    match=0
    matchlist=[]
    stepscale=[]
    stepscales=[]
    chordlen=len(chord)
    stepslen=len(steps)
    for n in range (0, stepslen):
        for m in range (0,7):
            transpose=steps[n][m]+root
            if transpose>11:
                transpose=transpose-12
            stepsitem.append(transpose)
            transpose=0
        stepstransposed.append(stepsitem)
        stepsitem=[]
    #print (stepstransposed)
    for n in range (0, stepslen):
        for m in range (0,7):
            for o in range (0,chordlen):
                #print (chordsteps[o])
                if chordsteps[o]==stepstransposed[n][m]:
                    match=match+1
                    
        matchlist.append(match)
        match=0


    for n in range (0,stepslen):
        if matchlist[n]==max(matchlist):
            #print (steps[n])
            #print (stepstransposed[n])
            for x in range (0,7):
                noteindex=stepstransposed[n][x]
                scalenote=notes[noteindex]
                scale.append(scalenote)
                stepscale.append(noteindex)
        if scale!=[]:
            scales.append(scale)
            stepscales.append(stepscale)
        scale=[]
        stepscale=[]
    scalestring=''
    print ("Scales:")
    guess=1
    for item in scales:
        for note in item:
            scalestring=scalestring+note+" "
        print ("Match",str(guess)+": ",scalestring)
        guess=guess+1
        scalestring=''
    guess=0
    print ("\n")

while True:
    init()
    name_chord()
    guess_scale()


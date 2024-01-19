row1=['*','*','*']
row2=['*','*','*']
row3=['*','*','*']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
pos=input("Where do you want the treasure map?: ")
vertical=int(pos[0])
horizontal=int(pos[1])
sel_row=map[vertical-1]
sel_row[horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")
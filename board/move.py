from pieces.nullpiece import nullpiece


class move:

    def __init__(self):
        pass

    def checkb(self,gametiles):
        x=0
        y=0
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.tostring()=='K'):
                    x=m
                    y=k
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.alliance=='White'):
                    moves=gametiles[m][k].pieceonCell.legalmoveb(gametiles)
                    for move in moves:
                        if(move[0]==x and move[1]==y):
                            return["checked",[m,k]]
        return["notchecked"]

    def updateposition(self,x,y):
        a=x*8
        b=a+y
        return b

    def movesifcheckedb(self,gametiles):
        movi=[]
        piece=None
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.alliance=='Black'):
                    moves=gametiles[m][k].pieceonCell.legalmoveb(gametiles)
                    for move in moves:
                        x=move[0]
                        y=move[1]
                        piece=gametiles[x][y].pieceonCell
                        gametiles[x][y].pieceonCell=gametiles[m][k].pieceonCell
                        gametiles[m][k].pieceonCell=nullpiece()
                        s=self.updateposition(x,y)
                        gametiles[x][y].pieceonCell.position=s
                        if(self.checkb(gametiles)[0]=='notchecked'):
                            movi.append([m,k,x,y])
                            gametiles[m][k].pieceonCell=gametiles[x][y].pieceonCell
                            gametiles[x][y].pieceonCell=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonCell.position=s
                        else:
                            gametiles[m][k].pieceonCell=gametiles[x][y].pieceonCell
                            gametiles[x][y].pieceonCell=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonCell.position=s


        return movi

    def checkw(self,gametiles):
        x=0
        y=0
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.tostring()=='k'):
                    x=m
                    y=k
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.alliance=='Black'):
                    moves=gametiles[m][k].pieceonCell.legalmoveb(gametiles)
                    if moves==None:
                        print(m)
                        print(k)
                    for move in moves:
                        if(move[0]==x and move[1]==y):
                            return["checked",[m,k]]
        return["notchecked"]

    def movesifcheckedw(self,gametiles):
        movi=[]
        piece=None
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.alliance=='White'):
                    moves=gametiles[m][k].pieceonCell.legalmoveb(gametiles)
                    for move in moves:
                        x=move[0]
                        y=move[1]
                        piece=gametiles[x][y].pieceonCell
                        gametiles[x][y].pieceonCell=gametiles[m][k].pieceonCell
                        gametiles[m][k].pieceonCell=nullpiece()
                        s=self.updateposition(x,y)
                        gametiles[x][y].pieceonCell.position=s
                        if(self.checkw(gametiles)[0]=='notchecked'):
                            movi.append([m,k,x,y])
                            gametiles[m][k].pieceonCell=gametiles[x][y].pieceonCell
                            gametiles[x][y].pieceonCell=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonCell.position=s
                        else:
                            gametiles[m][k].pieceonCell=gametiles[x][y].pieceonCell
                            gametiles[x][y].pieceonCell=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonCell.position=s


        return movi

    def castlingb(self,gametiles):
        array=[]
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.tostring()=='K'):
                    if(gametiles[m][k].pieceonCell.moved==False):
                        if(gametiles[m][k+3].pieceonCell.tostring()=='R'):
                            if(gametiles[m][k+3].pieceonCell.moved==False):
                                if(gametiles[m][k+1].pieceonCell.tostring()=='-'):
                                    if(gametiles[m][k+2].pieceonCell.tostring()=='-'):
                                        array.append('ks')
                        if(gametiles[m][0].pieceonCell.tostring()=='R'):
                            if(gametiles[m][0].pieceonCell.moved==False):
                                if(gametiles[m][3].pieceonCell.tostring()=='-'):
                                    if(gametiles[m][2].pieceonCell.tostring()=='-'):
                                        if(gametiles[m][1].pieceonCell.tostring()=='-'):
                                            array.append('qs')
                    return array
    def castlingw(self,gametiles):
        array=[]
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonCell.tostring()=='k'):
                    if(gametiles[m][k].pieceonCell.moved==False):
                        if(gametiles[m][k+3].pieceonCell.tostring()=='r'):
                            if(gametiles[m][k+3].pieceonCell.moved==False):
                                if(gametiles[m][k+1].pieceonCell.tostring()=='-'):
                                    if(gametiles[m][k+2].pieceonCell.tostring()=='-'):
                                        array.append('ks')
                        if(gametiles[m][0].pieceonCell.tostring()=='r'):
                            if(gametiles[m][0].pieceonCell.moved==False):
                                if(gametiles[m][3].pieceonCell.tostring()=='-'):
                                    if(gametiles[m][2].pieceonCell.tostring()=='-'):
                                        if(gametiles[m][1].pieceonCell.tostring()=='-'):
                                            array.append('qs')
                    return array



    def enpassantb(self,gametiles,y,x):

        if(gametiles[y][x].pieceonCell.tostring()=='P' and y==4):
            if(x+1<8 and gametiles[y][x+1].pieceonCell.tostring()=='p' and gametiles[y][x+1].pieceonCell.enpassant==True):
                return[[y,x],'r']
            if(x-1>=0 and gametiles[y][x-1].pieceonCell.tostring()=='p' and gametiles[y][x-1].pieceonCell.enpassant==True):
                return[[y,x],'l']

        if(gametiles[y][x].pieceonCell.tostring()=='p' and y==3):
            if(x+1<8 and gametiles[y][x+1].pieceonCell.tostring()=='P' and gametiles[y][x+1].pieceonCell.enpassant==True):
                return[[y,x],'r']
            if(x-1>=0 and gametiles[y][x-1].pieceonCell.tostring()=='P' and gametiles[y][x-1].pieceonCell.enpassant==True):
                return[[y,x],'l']

        return []


    def pinnedb(self,gametiles,moves,y,x):
        movi=[]
        piece1=None
        for move in moves:
            m=move[0]
            k=move[1]
            piece1=gametiles[m][k].pieceonCell
            gametiles[m][k].pieceonCell=gametiles[y][x].pieceonCell
            gametiles[y][x].pieceonCell=nullpiece()
            if(self.checkb(gametiles)[0]=='notchecked'):
                movi.append(move)
            gametiles[y][x].pieceonCell=gametiles[m][k].pieceonCell
            gametiles[m][k].pieceonCell=piece1

        return movi

    def pinnedw(self,gametiles,moves,y,x):
        movi=[]
        piece1=None
        for move in moves:
            m=move[0]
            k=move[1]
            piece1=gametiles[m][k].pieceonCell
            gametiles[m][k].pieceonCell=gametiles[y][x].pieceonCell
            gametiles[y][x].pieceonCell=nullpiece()
            if(self.checkw(gametiles)[0]=='notchecked'):
                movi.append(move)
            gametiles[y][x].pieceonCell=gametiles[m][k].pieceonCell
            gametiles[m][k].pieceonCell=piece1

        return movi
























































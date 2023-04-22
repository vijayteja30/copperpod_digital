from random import randint
class TetrisGame:
    def __init__(self, size):
        self.size=size+1

        self.a=self.get_empty_board()
        
        # for i in range(self.size):
        #     tmp=[]
        #     for j in range(self.size):
        #         if (i==0 and j==0) or (i==0 and j==self.size-1) or (i==self.size-1) or (j==0 or j==self.size-1):
        #             ch="*"
        #         else:
        #             ch=' '
        #         tmp.append(ch)
        #     self.a.append(tmp)
        
        self.tetris_pieces = ["****","* \n* \n**"," *\n *\n**", " *\n**\n* ","**\n**"]
        self.current_piece = self.tetris_pieces[3] #self.tetris_pieces[randint(0,4)]
        temp=self.current_piece.split('\n')
        self.curr_piece_width, self.curr_piece_height = len(temp[0]), len(temp)
        self.space_curr_width, self.space_curr_height = 0,0
        # print(self.current_piece)
    
    def get_empty_board(self):
        arr=[]
        for i in range(self.size):
            tmp=[]
            for j in range(self.size):
                if (i==0 and j==0) or (i==0 and j==self.size-1) or (i==self.size-1) or (j==0 or j==self.size-1):
                    ch="*"
                else:
                    ch=' '
                tmp.append(ch)
            arr.append(tmp)
        return arr

    def rotate_90(self):
        curr_piece = self.current_piece.split('\n')
        t=''
        l=len(curr_piece[0])-1
        for i in range(len(curr_piece[0])):
            for j in range(len(curr_piece)-1, -1, -1):
                t+=curr_piece[j][i]
            if i!=l:
                t+='\n'
        
        self.current_piece=t
        self.curr_piece_width, self.curr_piece_height = len(curr_piece), len(curr_piece[0])
        # print(t, self.curr_piece_width, self.curr_piece_height)
        
    def rotate_all_angles(self, angle_count=4):
        for i in range(angle_count):
            print()
            self.rotate_90()
    
    def place_tetris(self):
        # print(self.space_curr_width, self.space_curr_height)
        w=self.space_curr_width
        arr=self.a.copy()

        for i in range(len(self.current_piece)):
            
            if self.current_piece[i]=='\n':
                self.space_curr_height+=1
                w=self.space_curr_width
            else:
                arr[self.space_curr_height][w]=self.current_piece[i]
                w+=1
        
        s=''
        for i in range(self.size):
            for j in range(self.size):
                s+=arr[i][j]
            if i!=self.size-1:
                s+='\n'

        print(s)
        
    def start_tetris(self):

        s=self.size-1
        self.space_curr_width=(s//2-self.curr_piece_width//2)

        self.place_tetris()
        while True:
            self.a=self.get_empty_board()
            inp=input("Enter input: ")
            w=self.space_curr_width
            if inp.lower()=='a':
                w=self.space_curr_width-1
                h=self.space_curr_height+1
            elif inp.lower()=='d':
                w=self.space_curr_width+1
                h=self.space_curr_height+1
            elif inp.lower()=='w':
                self.rotate_all_angles(3)
                h=self.space_curr_height+1
            elif inp.lower()=='s':
                self.rotate_all_angles(1)
                h=self.space_curr_height+1
            elif inp.lower()==' ':
                h=self.space_curr_height+1
            else:
                print("Please enter correct input as \"a/d/w/s/space(\' \')\"")
                continue
            # print(f"w==> {w}, h==> {h}")
            # if w+self.curr_piece_width>=self.size:
            #     w-=self.curr_piece_width-1
            # if h+self.curr_piece_height>=self.size:
            #     h-=self.curr_piece_height
            
            if w+self.curr_piece_width>=self.size:
                w=self.size-self.curr_piece_width-1
            if h+self.curr_piece_height>=self.size:
                h=self.size-self.curr_piece_height-1
            
            if w<=0:
                w=1
            
            self.space_curr_width, self.space_curr_height = w, h
            
            self.place_tetris()
            
                
                    
obj = TetrisGame(12)
# obj.rotate_all_angles()
# obj.rotate_90()
obj.start_tetris()
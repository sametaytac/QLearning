from copy import deepcopy
class vaction:
        def __init__(self, actionID,startnode,reward, acts):
              self.actionID = deepcopy(actionID);
              self.acts = deepcopy(acts);
              self.startnode =deepcopy(startnode);
              self.reward = deepcopy(reward);
def findmax(row):
        a=[];
        for i in row:
                if(i!='_'):
                        a.append(i);
        if(len(a)==0):
                return 0;
        else:
                return max(a);
def findmaxind(row):
        max1=[];
        temp=-999;
        for i in range(0,len(row)):
                if(row[i]=='_'):
                        continue;
                elif(row[i]>temp):
                        temp=row[i];
                        if(len(max1)!=0):
                                del max1[:];
                        max1.append(i);
                elif (row[i]==temp):
                        max1.append(i);
        return max1;
def findmaxind2(row):
        max1=[];
        temp=-999;
        for i in range(0,len(row)):
                if(row[i]=='_'):
                        continue;
                elif(row[i]>temp):
                        temp=row[i];
                        if(len(max1)!=0):
                                del max1[:];
                        max1.append(i);
        return max1;
def printtable(table):
        for i in table:
                print " ".join([str(x) for x in i] );
                print;
def duzelt(a):
	if(a=='_'):
		return 0;
	else:
		return a;
read1 = open("hw4.inp", "r")
nodes = str(read1.readline());
roundn = [];
vortex= [];
room = []
star = []
goal = []
for i in range(0,len(nodes)):
	if(nodes[i]=='R'):
		roundn.append(i);
	elif (nodes[i]=='V'):
		vortex.append(i);
	elif (nodes[i]=='O'):
		room.append(i);
	elif (nodes[i]=='S'):
		star.append(i);
	elif (nodes[i]=='G'):
		goal.append(i);

firstnodes=roundn+vortex+room;
tmp = str(read1.readline());
floats = [float(x) for x in tmp.split()]
alfa=floats[0];
gama=floats[1];
actcount = int(read1.readline());
actions = []
#take actions 
for i in range(0,actcount):
	tmp = str(read1.readline());
	tmpaction = [int(x) for x in tmp.split()]
	actions.append(tmpaction);
firstvort=[];
for a in actions:
	if a[1] not in roundn and a[1] not in firstvort and a[1] not in room:
		firstvort.append(a[1]);
secondvort=[];
for a in vortex:
	if a not in firstvort:
		secondvort.append(a);
firstnodes=roundn+firstvort+room;
#q ve r fonksiyonu initilazionu
Q=[[]];
R=[[]];
for i in firstnodes:
        Q.append([]);
        R.append([]);
        for j in firstnodes:
              Q[i].append('_');
              R[i].append('_');
Q=Q[0:-1];
R=R[0:-1];
for a in actions:
        R[a[0]][a[1]]=a[2];
#Q learning is starting
while(1):
        episode = raw_input();
        if(episode=="$"):
                break;
        else:
            episode = [int(x) for x in episode.split()];
        for n in range(0,len(episode)-1):
                Q[episode[n]][episode[n+1]]=(1-alfa)*duzelt(Q[episode[n]][episode[n+1]])+(alfa)*(R[episode[n]][episode[n+1]]+gama*findmax(Q[episode[n+1]]));
        printtable(Q);

#2.part basliyor,once input al

adactcount = int(read1.readline());
admissacts=[];
for i in range(0,adactcount):
        tmpa = str(read1.readline());
        tmpadaction = [int(x) for x in tmpa.split()];
        admissacts.append(tmpadaction);
actionlist=[];
counter=0;
while(1):
        tmp = str(read1.readline());
        if('E' in tmp):
                break;
        elif('#' in tmp):
                counter+=1;
                continue;
        elif('$' not in tmp):
                actid=tmp[-3];
        pers=0;
        tmact=[];
        snode1=str(read1.readline());
        if('#' in snode1):
                counter+=1;
                continue;
        else:
                snode=int(snode1);
        rew=float(read1.readline());
        while(pers!=100):
                tmpa = str(read1.readline());
                tmpadaction = [int(x) for x in tmpa.split()];
                #print tmpadaction;
                pers=pers+tmpadaction[-1];
                tmact.append(tmpadaction);
        act1=vaction(actid,snode,rew, tmact);
        actionlist.append(act1);
secondnodes=room+star+goal+secondvort;
#ikinci bolumde kullanilacak
V=[];
#initial V values are 0
for i in range(0,len(secondnodes)):
		V.append(0);



 #value iteration
while(1):

        Qsec=[[]];
        for i in range(0,len(secondnodes)):
                Qsec.append([]);
                for j in range(0,counter):
                        Qsec[i].append('_');
        Qsec=Qsec[0:-1];
        for s in secondnodes:
                 Q2=[];
                 flag=0;
                 for a in admissacts:
                         if(a[0]==s):
                                 flag=1;
                                 actofnodes=a;
                                 break;
                 if(len(actofnodes)!=0 and flag==1):
                                 for move in actionlist:
                                        if(move.startnode==s):
                                                val=move.reward;
                                                for ac in move.acts:
                                                        val=val+ac[1]*gama*V[ac[0]-len(roundn)-len(firstvort)]/100;
                                                        Q2.append(val);
                                                        Qsec[int(s)-len(roundn)-len(firstvort)][int(move.actionID)]=val;
                                                       
                 if(len(Q2)!=0):
                        V[s-len(roundn)-len(vortex)]=max(Q2);
        for i in Qsec:
                print " ".join([str(x) for x in i] );
                print;
	for i in range(0,len(Qsec)):
        	tempmax=findmaxind2(Qsec[i]);
		teemp=[];
        	if(len(tempmax)==0):
                	continue;
		for move in actionlist:
			if(move.startnode==secondnodes[i] and int(move.actionID)==tempmax[0]):
				for ac in move.acts:
					teemp.append(ac[0]);
        	print (str(secondnodes[i]) + " " + ",".join([str(x) for x in teemp] ));
	tmpas = raw_input();
        if(tmpas=='$'):
                break;




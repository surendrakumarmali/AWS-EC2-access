import boto
import boto.ec2
y = []
lines =[line.rstrip('\n') for line in open('4_temp_text_file.txt')]

for i in range(5,len(lines)):

#for i in range(len(lines[i])):

    x  = list([''.join( c for c in lines[i] if  c not in '[\']' )])
   # print i
    x =  x[0].replace('Volume:', '')
    #print x
    y = [x.rstrip().split(',')]
    #print "y[0][0]    : " ,y[0][0]
    #print "y[0][1]    : " ,y[0][1]
    #if (y[0][2] == "running(16)"):
    conn = boto.ec2.connect_to_region(y[0][0])
    print str(y[0][1])
    conn.delete_volume(str(y[0][1]))    
    #conn.stop_instances(instance_ids=y[0][1])
        #conn.terminate_instances(instance_ids=y[0][1])
    print ("\I am sure your Undo shortcut won't work,May GOD bless you ;)")


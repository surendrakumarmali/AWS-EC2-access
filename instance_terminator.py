import boto
import boto.ec2
y = []
lines =[line.rstrip('\n') for line in open('2_temp_text_file.txt')]

for i in range(6,len(lines)):
    
#for i in range(len(lines[i])):
    
    x  = list([''.join( c for c in lines[i] if  c not in '[\']' )])
    x =  x[0].replace(' ', '').replace('RegionInfo:','').replace('Region:','').replace('InstanceId:','').replace('Instancestate:','')
    y = [x.rstrip().split(',')]
    print y
    if (y[0][2] == "stopped(80)"):
        conn = boto.ec2.connect_to_region(y[0][0])
	conn.terminate_instances(instance_ids=y[0][1])
	#print ("\I am sure your Undo shortcut won't work,May GOD bless you ;)")

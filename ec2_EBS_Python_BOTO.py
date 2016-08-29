###____________________________###

'''
File name : ec2_EBS_Python_BOTO.py
Created By : Surendra Kumar Mali
Date : 29-July-2016
Mail Id :  surendrakumarmali@gmail.com
Summary: Genrate AWS EC2 and EBS usese report.
'''

from pprint import pprint
import boto
import boto.ec2
from boto.ec2.regioninfo import RegionInfo
import itertools
import sys
from boto import ec2
from itertools import chain


#to get the connection to specific resion
def get_conn(i,regions,endpoints):
    # first create a region object and connection
    region = RegionInfo(name=regions[i], endpoint=endpoints[i])

    # first create a connection to the appropriate host, using your credentials
    ec2conn =  boto.connect_ec2(region = region)
    reservations = ec2conn.get_all_instances()
    return reservations



def instance_data(reservations,target):
    summary_report = []
    #print "AWS untaged instance detail\n"	    
    #Fatching instance data from all resion collectivly
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        if i._state == "terminated(48)":
            print i._state
#           print i.id
	    continue

	if str(i.tags['Name']) == "" and i._state != "terminated(48)":
	    #pprint(i.__dict__) #uncomment if you want to see complate meta data of instance
            summary_report.append(["Region : " + str(i.region),"Instance Id : " + str(i.id),"Instance state : " + str(i._state)]) #,str(i.tags['Name'])])
	    #summary_report = list(chain.from_iterable(summary_report))        
	    print "___________________________"
            print('\n')
            print "dns_name         : ",i.dns_name
            print "id               : ",i.id
            print "image_id         : ",i.image_id
            print "ip_address       : ",i.ip_address
            print "key_name         : ",i.key_name
            print "launch_time      : ",i.launch_time
            print "public_dns_name  : ",i.public_dns_name
            print "private_dns_name : ",i.private_dns_name
            print "region           : ",i.region
            #print "tags             : ",i.tags['Name']
            print "state            : ",i._state,"\n"
	    
	
            target.write("\nRegion           : " + str(i.region) + "\n")
            target.write("______ \n")
            target.write('\n')
            target.write("Dns_name         : " + str(i.dns_name) + "\n")
            target.write("Id               : " + str(i.id) + "\n")
            target.write("Image_id         : " + str(i.image_id) + "\n")
            target.write("Ip_address       : " + str(i.ip_address) + "\n")
            target.write("Key_name         : " + str(i.key_name) + "\n")
            target.write("Launch_time      : " + str(i.launch_time) + "\n")
            target.write("Public_dns_name  : " + str(i.public_dns_name) + "\n")
            target.write("Private_dns_name : " + str(i.private_dns_name) + "\n")
            target.write("Region           : " + str(i.region) + "\n" )
            #target.write("Tags                        : " + str(i.tags['Name']) + "\n")
            target.write("State            : " + str(i._state) + "\n")
            target.write("\n")

    return summary_report
        

def aws_summary(summary_report):
    file_name_2 = "/home/ubuntu/aws_inspector/2_temp_text_file.txt"
    fd2 = open(file_name_2,'a')
    #fd2.write("\n")
    #fd2.write("AWS untaged instance detail\n")
    #fd2.write("---------------------------\n")
    for i in range(len(summary_report)):
    	fd2.write(str(summary_report[i]))
	fd2.write("\n")
    #fd.write("\n")
    #fd2.write("\n")
    fd2.close()



def vol_status(regions):

    fd4 = open("/home/ubuntu/aws_inspector/4_temp_text_file.txt", 'w')
    fd4.write("\n\n")
    #fd4.write("\n\n--------------------------\n")
    #fd..write("--------------------------\n")
    fd4.write("\nAws Untaged Unatteched EBS Volumes")
    fd4.write( "\n----------------------------------\n")
    print "\nAws Untaged Unatteched EBS Volumes"
    print "\n---------------------------------\n"

    for i in range(len(regions)):

        # first create a region object and connection
        connection=ec2.connect_to_region(regions[i])

        try:
            volumes=connection.get_all_volumes()
            #if volumes != []:
                #print regions[i]
		#fd4.write("\n")
	        #fd4.write("Region:" + regions[i])
		#fd4.write( "\n")

                #for vol in volumes:
                #print '\n'
                #print str(vol),"  ","Atteched Instance id : ",str(vol.attach_data.instance_id),"        ",\
                #       "Volum Status : ", str(vol.status), "  Volume Tag : ",str(vol.tags)
                #print str(vol.attehment_state())
            for vol in volumes:
                if str(vol.status) == 'available' and str(vol.tags) == '{}' and str(vol.attach_data.instance_id) == 'None':
                    #print "\n"
                    print vol," : is deletable"
		    #fd4.write(str(vol) + " is deletable\n")
                    fd4.write(str(regions[i]) + "," + str(vol) + "\n")
        except:
            print 'Some Error occurred :'
            print sys.exc_info()
	
	fd.close()


#Final Report genration
def final_report():
    f1 = open("/home/ubuntu/aws_inspector/1_temp_text_file.txt")
    f1_contents = f1.read()
    f1.close()

    f2 = open("/home/ubuntu/aws_inspector/2_temp_text_file.txt")
    f2_contents = f2.read()
    f2.close()

    f3 = open("/home/ubuntu/aws_inspector/3_temp_text_file.txt")
    f3_contents = f3.read()
    f3.close()

    f4 = open("/home/ubuntu/aws_inspector/4_temp_text_file.txt")
    f4_contents = f4.read()
    f4.close()
    
    f5 = open("final_report.txt", "w")
    f5.write(f1_contents + f2_contents + f4_contents + f3_contents) # concatenate the contents
    f4.close()



regions = ['us-east-1','us-west-1','us-west-2','ap-south-1','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-northeast-1','eu-central-1','eu-west-1','sa-east-1']
endpoints = ['ec2.us-east-1.amazonaws.com','ec2.us-west-1.amazonaws.com','ec2.us-west-2.amazonaws.com','ec2.ap-south-1.amazonaws.com','ec2.ap-northeast-2.amazonaws.com','ec2.ap-southeast-1.amazonaws.com','ec2.ap-southeast-2.amazonaws.com','ec2.ap-northeast-1.amazonaws.com','ec2.eu-central-1.amazonaws.com','ec2.eu-west-1.amazonaws.com','ec2.sa-east-1.amazonaws.com']

file_name_1 = "/home/ubuntu/aws_inspector/1_temp_text_file.txt"
fd = open(file_name_1,'w')

fd.write("\"\"\"From: From Person <abc@gmail.com>\n\
To: To Person <XYZ@gmail.com>\n\
Subject: AWS Usages Inspector\n\
\n\
Hello Team,\n\n\
	Please go through below report carefully. It has running/stopped EC2 instances which are untagged and EBS Volumes which are untagged and currently detached. \n\
Please note that untagged EC2 Instances will be stopped at 7:00PM IST and they will be terminated after 4 hours from the time you receive this email.\n\
Untagged and Detached EBS Volumes will be deleted after 2 hours after you receive this email. Please tag if you still need them.\n\
\n\n")
fd.close()



file_name_2 = "/home/ubuntu/aws_inspector/2_temp_text_file.txt"
fd = open(file_name_2,'w')
fd.write("________________\n")
fd.write("AWS Usage Summary:\n")
fd.write("________________\n")
fd.write("\n")
fd.write("AWS untaged instance detail\n")
fd.write("---------------------------\n")
fd.close()


file_name_3 = "/home/ubuntu/aws_inspector/3_temp_text_file.txt"
target = open(file_name_3, 'w')
target.write("\n\n---------------------------------\n")
target.write("Untaged Instances Detailed Summary:\n")
target.write("---------------------------------\n")

for i in range(len(regions)):cs
    reservations = get_conn(i,regions,endpoints)
    if reservations != []:
        summary_report = instance_data(reservations,target)
        #summary_report = list(chain.from_iterable(summary_report))
    #for j in range(len(summary_report)):
	#if j != []:
        #print summary_report 
        aws_summary(summary_report) 
    #print regions[i]
vol_status(regions)
target.write("This is auto generated mail, Do not reply.\nAny suggestion please write back to Surendra Kumar Mali <surendrakumarmali@gmail.com>\n")
target.close()
final_report()

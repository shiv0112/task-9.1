import os
import pyttsx3
import speech_recognition as speech
speak=pyttsx3.init()

print("\t\t\t\tWelcome welcome welcome")
speak.say("Hello!!!")

print("\t\t\t\tWelcome to my menu program")
print("\t\t\t\tI am your assistant AQUA")
speak.say("Welcome to my menu program")
speak.say("I am your assistant Aqua and I am here to guide you through")
speak.runAndWait() 

r = speech.Recognizer()

def listen():
    with speech.Microphone() as source:
        print("Give me a command...")
        audio = r.listen(source)
        print("Got ya Processing, please wait...")
        speek("Got ya, Processing, please wait")
        output = r.recognize_google(audio)
        print("You said, "+output)
        return(output.lower())
def speek(m):
    speak.say(m)
    speak.runAndWait()

m="""\nI can help u with:
1. Using common Linux commands.
2. Performing disk Operations.
3. Configuring a httpd or a haproxy server
4. Performing LVM operations
5. Configuring Hadoop """ 

print(m)
speek("""I can help u with:
Using common Linux commands.
Performing disk Operations.
Configuring a httpd or a haproxy server
Performing LVM operations
Configuring Hadoop""") 
ch=listen()

if ("linux commands" in ch) or ("commands" in ch) or ("linux command" in ch) or ("command" in ch) or ('linux' in ch):
    print("\nI can run several Linux commands for you")
    speek("I can run several Linux commands for you")
    print("""\nTell me what  do you want me to run...
    1. Show calender
    2. Show date
    3. Show RAM uses
    4. Show all the processes running
    5. Setup a yum repository
    """)
    speek("""Tell me what  do you want me to run...
    Show calender
    Show date
    Show RAM uses
    Show all the proccesses running 
    Setup a yum repository
    """)
    
    c=listen()
    if ("date" in c):
        speek("th date is")
        os.system("date")
    elif ("calender" in c) or ("cal" in c):
        speek("Here is this months calender for you")
        os.system("cal")
    elif ("ram" in c) or ("memory" in c):
        speek("The RAM stats are as follows")
        os.system("free -m")
    elif ("processes" in c) or ("process" in c):
        speek("here is the detailed list of the precess running right now")
        os.system("ps -aux")
    elif ("yum" in c):
        speek("Yo configuring YUM for you")
        os.system("cd /etc/yum.repos.d")
        f=open("/etc/yum.repos.d/yumc.repo", "w")	
        f.write("""[dvd1]
    baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
    gpgcheck=0

    [dvd2]
    baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
    pgcheck=0""")
        f.close()
        os.system("yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        os.system("yum repolist")

elif ("disk operations" in ch) or ("disk" in ch) or ("disk operation" in ch):
    print("disk\n")
    speek("What are you interested in, Creating a partition, Formatting the disk or Mounting")
    print("""\nWHat you want
    -Partition
    -Formatting
    -Mounting""")
    k=listen()
    if ("format" in k) or ("formatting" in k):
        speek("Formatting the disk for you, Enter the drive name via keyboard")
        f=input("Enter drive name")
        os.system("mkdir /"+f)
        os.system("lsblk")
        speek("Enter the partition name")
        p=input("Enter a partition name")
        os.system("mount /dev/"+p+" "+"/"+f)
        os.system("cd /"+f)
    elif ("mount" in k) or ("mounting" in k):
        speek("Mounting the disk for you, please enter the disk nme via keyboard")
        d=input("Enter disk name")
        os.system("mkfs.ext4 /dev/"+d)
    elif ("partition" in k):  
        speek("Creating the partition for you, enter the disk name via keyboard")
        d=input("Enter disk name")
        speek("Enter the partition size in GiB")
        s=input("Input partition size in GB")
        i="(echo 'n' ; echo 'p'; echo -ne '\n'; echo -ne '\n'; echo '+"+s+"G'; echo 'w')| fdisk /dev/"+d
        os.system(i)
        os.system("udevadm settle")
        os.system("lsblk")    

elif ("httpd" in ch) or ("webserver" in ch) or ("haproxy" in ch) or ("load balancer" in ch) or ('proxy' in ch) or ('server' in ch):
    print("httpd/haproxy")
    print("What do you want to configure: Webserver or LoadBalancer")
    speek("What do you want to configure: Webserver or LOad Balancer")
    k=listen()
    if ("webserver" in k) or ("Webserver" in k) or ('web' in k):
        speek("Starting httpd configuration")
        os.system("dnf install httpd -y")
        os.system("systemctl enable httpd")
        os.system("systemctl start httpd")
        speek("Successful")
        print("Done")
    elif ("load" in k) or ("load balancer" in k):
        speek("Starting load balancer")
        os.system("dnf install haproxy -y")
        os.system("systemctl enable haproxy")
        os.system("systemctl start haproxy")    
        speek("Done")
        print("Done")
elif ("lvm" in ch) or ("lvm operations" in ch) or ("lvm operation" in ch) or ("lbm" in ch) or ("aluminium" in ch):
    speek("LVM configuration beginning")
    speek("Enter the first disk name via keyboard")
    d1=input("Enter first disk name ")
    speek("Enter the second disk name")
    d2=input("Enter second disk name ")
    speek("Enter the name of the volume group")
    v=input("Enter the name of the volume group ")
    speek("Enter the name of the LVM")
    n=input("Enter the name of the LVM ")
    speek("Enter the size of the LVM")
    s=input("Enter the size of the LVM")
    speek("Input the LVM mountpoint name")
    dr=input("Input the LVM mountpoint name ")
    #pv creation
    os.system("pvcreate /dev/"+d1)
    os.system("pvcreate /dev/"+d2)
    #vg creation
    os.system("vgcreate "+v+" /dev/"+d1+" /dev/"+d2)
    os.system("vgdisplay "+v)
    #lvm creation
    os.system("lvcreate --size +"+s+"G --name "+n+" "+v)
    #formatting
    os.system("mkfs.ext4 /dev/"+v+"/"+n)
    #mounting
    os.system("mkdir /"+dr)
    os.system("mount /dev/"+v+"/"+n+" "+"/"+dr)
    os.system("cd /"+dr)

elif ("configure hadoop" in ch) or ("hadoop" in ch):
    speek("What do you want to configure name node or data node")
    h=listen()
    if ("name" in h) or ("namenode" in h) or ("master" in h) or ("masternode" in h):
        speek("Enter IP of master node")
        ip=input("Enter masternode enp0s3 IPv4 ")
        m=open("/etc/hadoop/hdfs-site.xml", "w")
        m.write("""<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>
    <property>
    <name>dfs.data.dir</name>
    <value>/data</value>
    </property>
    </configuration>""")
        m.close()
        os.system("mkdir /name")
        m=open("/etc/hadoop/core-site.xml", "w")
        m.write("""<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://"""+k+"""</value>
    </property>
    </configuration>""")
        m.close()
        os.system("systemctl stop firewalld")
        os.system("hadoop-daemon.sh start datanode")
        os.system("jps")
        os.system("hadoop dfsadmin -report")
    
    elif ("slave" in h) or ("worker" in h) or ("slave node" in h) or ("worker node" in h):
        speek("Enter the IP address of master node")
        k=input("Enter master node enp0s3 IPv4 ")
        m=open("/etc/hadoop/hdfs-site.xml", "w")
        m.write("""<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>

    </configuration>""")
        m.close()
        os.system("mkdir /name")
        m=open("/etc/hadoop/core-site.xml", "w")
        m.write("""<?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

    <!-- Put site-specific property overrides in this file. -->

    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://"""+k+"""</value>
    </property>
    </configuration>""")
        m.close()
        os.system("systemctl stop firewalld")
        os.system("hadoop dfsadmin -report")
        os.system("hadoop fs -ls /")
else:
    print("Either was not able to hear you or no matching case")
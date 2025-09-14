1)ZjLjJmM6FvvyRnrB2rfNW0ZOTa6ip5If
2]263JGJPfgU6LtdEvgfWU1XP5yac29mFx
3)2WnrDFRmJIq3IPxneAaMGhap0pFhF3NJ
4)4oQYVPkxzZOEO05pTW81FB8j8LxXGUQw
5)forgot to copy 
6)morbNTDKSW6jIlUc0ymOdMaLnOlFVAaj
7)forgot to copy 
8)dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
9)4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
10)FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
11)dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
12)7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
13)FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
14)MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
15)8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo


1] 

ssh bandit0@bandit.labs.overthewire.org -p 2220
what this means 
ssh → Secure Shell program (used to connect to another computer securely).
bandit0@... →
bandit0 → username you’re logging in as.
bandit.labs.overthewire.org → the remote host (domain name).
-p 2220 → option -p specifies the port number. Here, it’s 2220 (not the default port 22).

2]

ls -la and cat 


3]

you enter a file name with space in the form 
word1\ word2\ word3 if the name of file is word1 word2 word 3

4]

chmod → “change mode” (used to set file permissions).
+x → means “add execute permission”.
+ → add (instead of remove - or set exactly =).
x → execute permission.
chmod is used to set permissions (read, write, execute) for who can access a file or directory.

5]

find [path] [options] [expression]

path → where to search
. → current directory
/ → whole system
/home/user → specific directory

options like find by name type size etc

expression is like action taken 

find . -type f | xargs file(Find all files in the current directory and run the file command on each one to identify what type of file it is)
-type f → restrict results to files only.
| (pipe) Takes the output of the first command and sends it as input to the next command.
xargs file → takes that list of filenames and runs the file command on them.

6]
cat data.txt | grep 'millionare'

cat data.txt → prints the contents of the file data.txt.
| (pipe) → sends that output into the next command.
grep 'millionare' → searches for lines containing the word millionare.

7]
sort data.txt | uniq -u
sort data.txt

Sorts the lines of data.txt alphabetically (or numerically if numbers).
This step is important because uniq only works on consecutive duplicates.
| (pipe)
Sends the sorted output to the next command.
uniq -u
uniq removes duplicate lines.
The option -u means: print only the lines that are unique (appear exactly once).

8]
strings data.txt | grep '^=='
strings data.txt Extracts and prints all human-readable character sequences from data.txt.
grep '^=='
grep searches for lines matching a pattern.
^ → means start of the line.
== → means the line must begin with two equal signs.

9]
base64 -d data.txt
base64
A tool to encode or decode data in Base64 format.
-d means to decode 

10]
1. gzip
Purpose: Compresses individual files.
Extension: .gz
Command:
gzip file.txt       # makes file.txt.gz and removes file.txt
gunzip file.txt.gz  # decompresses back

2.tar

Purpose: Archive multiple files into one (doesn’t compress by itself).
Extension: .tar
Command examples:
tar -cvf archive.tar file1 file2 dir/   # create archive
tar -xvf archive.tar                    # extract archive
c → create
x → extract
v → verbose (show files)
f → file name follows

3.bzip2
Purpose: Compresses individual files (like gzip, but better compression, slower).
Extension: .bz2
Command:
bzip2 file.txt      # makes file.txt.bz2
bunzip2 file.txt.bz2

11]
nc host 3000
nc Stands for Netcat.Can be used to:Open TCP/UDP connections Send/receive data Act as a simple client or serverhost The hostname. 3000 is the port number on the host we want to connect to 



data=read.delim(file="distance_counts.txt",header=FALSE)

tcdr3=sum(as.numeric(data$V22))
gcdr3=sum(colSums(data))-tcdr3

sprintf("total currently counted:%e",tcdr3)
sprintf("L=22 %e :  %0.2f percent of total",gcdr3,100*gcdr3/tcdr3)

#seqs=read.table("seq_w_D.txt")
#numbSeqs=nrow(seqs[1])
#UnumbSeqs=nrow(unique(seqs))
d=read.table(file="linecount")
numbSeqs=d[1,1]
d=read.table(file="uniqlinecount")
UnumbSeqs=d[1,1]
sprintf("%0.2e sequences with correct D: %0.2f percent of L=22",numbSeqs,100*numbSeqs/gcdr3)
sprintf("%0.2e sequences with D with %0.2e unique (%0.2f)",numbSeqs,UnumbSeqs,UnumbSeqs/numbSeqs)

sprintf("D=0  %d : %0.2e percent of L=22 and correct D",sum(as.numeric(data$V1)),100*sum(as.numeric(data$V1))/numbSeqs)
sprintf("D=1  %d : %0.2e percent of L=22 and correct D",sum(as.numeric(data$V2)),100*sum(as.numeric(data$V2))/numbSeqs)
sprintf("D=2  %d : %0.2e percent of L=22 and correct D",sum(as.numeric(data$V3)),100*sum(as.numeric(data$V3))/numbSeqs)
sprintf("D=3  %d : %0.2e percent of L=22 and correct D",sum(as.numeric(data$V4)),100*sum(as.numeric(data$V4))/numbSeqs)
sprintf("D=4  %d : %0.2e percent of L=22 and correct D",sum(as.numeric(data$V5)),100*sum(as.numeric(data$V5))/numbSeqs)

sprintf("")
sprintf(" - calculated total number of sequences %e",numbSeqs/0.00022692)

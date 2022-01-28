 # library
library(ggplot2)
library(philentropy)
 
# create a dataset
I_score=read.delim("/work/jsmb/score/igor/igor_log2_scoring.c50k.txt",header=FALSE)
IV=I_score$V2
B_score=read.delim("/work/jsmb/score/Briney/Briney_log2_scoring.c50k.txt",header=FALSE)
BV=B_score$V2
BD_score=read.delim("/work/jsmb/score/Briney/Briney_log2_scoring_wD.c50k.txt",header=FALSE)
BDV=BD_score$V2

#I_score=read.delim("~/igor_scoring/igor_log2_scoring.subsample.txt",header=FALSE)
#IV=I_score$V2
#B_score=read.delim("~/igor_scoring/Briney_log2_scoring.txt",header=FALSE)
#BV=B_score$V2
#BD_score=read.delim("~/igor_scoring/Briney_log2_scoring_wD.txt",header=FALSE)
#BDV=BD_score$V2



I_hist=hist(IV,breaks=c(seq(-90,30,by=1)),plot=FALSE)
B_hist=hist(BV,breaks=c(seq(-90,30,by=1)),plot=FALSE)
BD_hist=hist(BDV,breaks=c(seq(-90,30,by=1)),plot=FALSE)


Gen<-c(rep("Igor",length(I_hist$mids)),rep("Briney",length(B_hist$mids)),rep("Briney D",length(BD_hist$mids)))
score<-c(I_hist$mids,B_hist$mids,BD_hist$mids)
density<-c(I_hist$density,B_hist$density,BD_hist$density)

D <- data.frame(score,Gen,density)
 
# Grouped
ggplot(D, aes(fill=Gen, y=density, x=score)) + geom_bar(position="dodge", stat="identity")+scale_fill_manual(values=c("#52853C","4E84C4","#D16103"))
ggsave("Scoring_histogram.pdf")


val=c(IV,BDV)
lab=c(rep("Igor",length(IV)),rep("Briney_D",length(BDV)))
D<-data.frame(val,lab)
wilcox.test(val~lab,data=D)

mean(IV);mean(BDV)

median(IV);median(BDV)


KL(rbind(I_hist$density,B_hist$density))
KL(rbind(I_hist$density,BD_hist$density))
KL(rbind(B_hist$density,BD_hist$density))

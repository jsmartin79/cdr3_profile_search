#!/usr/bin/perl

$size=1539150869*2/15;
 
$counter=0;
open($fh,'-|', "gunzip -c $ARGV[0]");
while($line=<$fh>)
{
    chomp $line;
    if ($line=~/^>/)
    {
	($name)=$line=~/^>(.*?)$/;
    }
    else
    {
	$dist=0;
	@seq=split(//, $line);
#	if ($counter%($size/1000)==0){$ticker++; print STDERR $ticker/1000, "\n";}
	if (@seq != 22){print "$name\t$line\tNA\n"; next;}
	if ($seq[1]!~/[SVTQMLICA]/){$dist++;}
	if ($seq[2]!~/[ACDEFGHIKLMNPQRSTVWY]/){$dist++;}
	if ($seq[3]!~/[SAG]/){$dist++;}
	if ($seq[4]!~/[SDAG]/){$dist++;}
	if ($seq[5]!~/[YFW]/){$dist++;}
	if ($seq[6]!~/[VSNLI]/){$dist++;}
	if ($seq[7]!~/[KMTS]/){$dist++;}
	if ($seq[8]!~/[WVMKIL]/){$dist++;}
	if ($seq[9]!~/[WFY]/){$dist++;}
	if ($seq[10]!~/Y/){$dist++;}
	if ($seq[11]!~/D/){$dist++;}
	if ($seq[12]!~/S/){$dist++;}
	if ($seq[13]!~/S/){$dist++;}
	if ($seq[14]!~/[SAG]/){$dist++;}
	if ($seq[15]!~/[FY]/){$dist++;}
	if ($seq[16]!~/[CTAP]/){$dist++;}
	if ($seq[17]!~/[SN]/){$dist++;}
	if ($seq[18]!~/[YWQNMLHCF]/){$dist++;}
	if ($seq[19]!~/[ND]/){$dist++;}
	if ($seq[20]!~/[ACDEFGHIKLMNPQRSTVWY]/){$dist++;}
	print "$name\t$line\t$dist\n"; 
    }
    $counter++;
}
close(FILE);

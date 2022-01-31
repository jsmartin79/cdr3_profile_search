#include <math.h>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include "utilities.hpp"
#include <boost/algorithm/string.hpp>

using namespace std;

struct multicolumn_sort
{
  multicolumn_sort(int column){this->column=column;}
  bool operator () (vector<string> &a, vector<string> &b)
  {
    return atof(a[column].c_str())>atof(b[column].c_str());
  }
  int column;
};

//functions
string sys_call(string);
string aa_convert_code(string);

int main(int argc, char *argv[])
{  
   if (argc <2){cout << "USAGE: ./findCDR -i [fasta] -o [outfile] -s [seqlogo] -p (printFlag) -nt (flag for nucleotides) -aa (flag for aa)\n"; exit(1);}
   //ARG HANDLING
   int i=0, frame=1;
   string fasta_filename="";
   string out_filename="out.txt";
   string seq_file="";
   bool printFlag=false;
   bool nucleotides=true;
   map<string,string> dna_to_aa_tranx_map;
   get_aa_tranx_map(dna_to_aa_tranx_map);
   
   while(i<argc)
     {
       string arg=argv[i];
       string next_arg;
       if (i<argc-1){next_arg=argv[i+1];}else{next_arg="";}
       
       if ((arg.substr(0,1)=="-")&&(next_arg.substr(0,1)=="-")){cerr << "incorrectly formatted cmdline\n"; exit(1);}
  
       if (arg == "-i")
	 {
	   fasta_filename=next_arg;
	 }
       if (arg == "-o")
	 {
	   out_filename=next_arg;
	 }
       if(arg == "-s")
	 {
	   seq_file=next_arg;
	 }
       if(arg=="-p")
	 {
	   printFlag=true;
	 }
       if(arg=="-nt")
	 {
	   nucleotides=true;
	 }
       if(arg=="-aa")
	 {
	   nucleotides=false;
	 }
     
       i++;
     }
   
   //read seq logos
   map<string, string> logo_hash;
   vector<string> logo_names;
   string name;
   string sequence_string;
   string aa_string;
   string file_str;
   int count=0;
   
   ifstream logofile(seq_file.c_str(), std::ios::in );
   if (!logofile.is_open()) {cerr << "ERROR reading logo file: could not open \"" << seq_file << "\"...exiting...\n"; exit(1);}

   while (!getline(logofile, file_str).eof())
     {
       name="logoline_"+to_string(count);
       chomp(file_str);
       sequence_string=file_str.substr(0,file_str.size());
       logo_hash[name]=sequence_string;
       logo_names.push_back(name);
       count++;
     }
   logofile.close();

   /*   for(int i=0;i<logo_names.size();i++)
     {
       cout << logo_names[i]<<"\t";
       cout << logo_hash[logo_names[i]]<<"\n";
       }*/

   ///OPEN SEQUENCE FILE AND PUT INTO MAP
  ifstream file(fasta_filename.c_str(), std::ios::in );
  if (!file.is_open()) {cerr << "ERROR reading fasta file: could not open \"" << fasta_filename << "\"...exiting...\n"; exit(1);}


  map<string,int> found_count;
  for (int i=0;i<=logo_names.size();i++)
    {
      name="d="+to_string(i);
      found_count[name]=0;
    }
  
  int seq_count=0;
  ofstream seq_fileout;
  seq_fileout.open("seq_wo_"+out_filename);

  ofstream seq_wd_fileout;
  seq_wd_fileout.open("seq_wd_"+out_filename);
  
  while (!getline(file, file_str).eof())
    {
      int dist=0;
      chomp(file_str);
      if (file_str.substr(0,1) == ">")
        {
          name=file_str.substr(1,file_str.size()-1);
	  continue;
          //sequence_names.push_back(name);
          //name_count++;
        }
      else
        {

	  sequence_string=file_str.substr(0,file_str.size());
	  //cout << sequence_string<<"\n";
	  //cout << "The size of str is " << sequence_string.length() << " bytes.\n";
	  if(sequence_string.length()<1)
	    continue;

	  if(nucleotides)
	    {
	      aa_string="";
	      translate_dna_to_aa(sequence_string,aa_string,1,dna_to_aa_tranx_map);
	      sequence_string=aa_string;
	      int wcardPOS=aa_string.find('*');
	      if(wcardPOS>=0)
		{
	      continue;
		}
	    }
	  seq_count++;
	  if(sequence_string.size()!=logo_names.size()+2)
	    {
	      dist=-1;
	      continue;
	    }

	  for(int i=1;i<logo_names.size();i++)
	    {
	      string nt=sequence_string.substr(i,1);
	      size_t found = logo_hash[logo_names[i-1]].find(nt);
	      if(found!=std::string::npos)
		{
		}
	      else
		dist++;
	    }
        }
      if(sequence_string.substr(10,4).compare("YDSS")==0)
	seq_wd_fileout<<sequence_string<<"\t"<<"D="<<dist<<"\n";
      else
	seq_fileout<<sequence_string<<"\t"<<"D="<<dist<<"\n";

      
      name="d="+to_string(dist);
      found_count[name]++;
    }
  seq_fileout.close();
  
  ofstream fileout;
  fileout.open(out_filename);
  //fileout << "found seqs" <<"\t"<<"Total seqs"<<"\n";
  for (int i=0;i<=logo_names.size();i++)
    {
      name="d="+to_string(i);
      fileout << name <<"\t";
      if(printFlag)
	cout << name << "\t";
    }
  fileout<<"total number" <<"\n";
  if(printFlag)
    cout<<"total number" <<"\n";
  for (int i=0;i<=logo_names.size();i++)
    {
      name="d="+to_string(i);
      found_count[name];
      fileout << found_count[name] <<"\t";
      if(printFlag)
	cout << found_count[name] <<"\t";
    }
  fileout<< seq_count<<"\n";
  if(printFlag)
    cout << seq_count<< "\n";
  //fileout << found_count <<"\t"<<seq_count<<"\n";
  fileout.close();
  
    return 0;
}

string sys_call(string cmd)
{
  string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");
  
  stream = popen(cmd.c_str(), "r");
  if (stream)
    {
      while (!feof(stream))
	if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
      pclose(stream);
    }
  return data;
}

/*
	if ($seq[0]!~/[SVTQMLICA]/){$dist++;}
	if ($seq[1]!~/[ACDEFGHIKLMNPQRSTVWY]/){$dist++;}
	if ($seq[2]!~/[SAG]/){$dist++;}
	if ($seq[3]!~/[SDAG]/){$dist++;}
	if ($seq[4]!~/[YFW]/){$dist++;}
	if ($seq[5]!~/[VSNLI]/){$dist++;}
	if ($seq[6]!~/[KMTS]/){$dist++;}
	if ($seq[7]!~/[WVMKIL]/){$dist++;}
	if ($seq[8]!~/[WFY]/){$dist++;}
	if ($seq[9]!~/Y/){$dist++;}
	if ($seq[10]!~/D/){$dist++;}
	if ($seq[11]!~/S/){$dist++;}
	if ($seq[12]!~/S/){$dist++;}
	if ($seq[13]!~/[SAG]/){$dist++;}
	if ($seq[14]!~/[FY]/){$dist++;}
	if ($seq[15]!~/[CTAP]/){$dist++;}
	if ($seq[16]!~/[SN]/){$dist++;}
	if ($seq[17]!~/[YWQNMLHCF]/){$dist++;}
	if ($seq[18]!~/[ND]/){$dist++;}
	if ($seq[19]!~/[ACDEFGHIKLMNPQRSTVWY]/){$dist++;}
*/

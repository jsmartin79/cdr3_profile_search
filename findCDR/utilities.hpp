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

using namespace std;

///functions
void chomp(string &);
void read_fasta_file(string, map<string, string> &, vector<string> &);
void read_fastq_file(string,vector<string> &,map<string, vector<int> >&, map<string,string> &);
void remove_duplicates(vector<vector<string> > &);
void tokenize(const string&, std::vector<string>&, const string& );
vector < vector <string> > read_delimited_file(string, string);
void pairwise_align_sequences_semiglobal_w_affine_gap(map<char, map<char, int> > &, string ,string ,double ,double ,string &, string &,double &);
void load_EDNAFULL_matrix(map<char, map<char,int> > &);
double Max(double, double, int &);
double Max(double, double, double, int &);
bool dna_sequence_has_stop_codon_in_reading_frame(string);
void expected_number_of_errors_from_fastq(vector< vector<int> > &, vector<double> & );
void sequence_identity(string, string, double &, double &);
void sequence_identity_semi_global(string, string, double &);
void print_pct_progress(int, int, int);
void pairwise_align_sequences_global_w_affine_gap(map<char, map<char, int> > &, string ,string ,double ,double ,string &, string &,double &);
void get_aa_tranx_map(map<string,string> &);
void translate_dna_to_aa(string &, string &, int, map<string,string> &);

void read_SMUA_file(string, vector<vector<string> > &);

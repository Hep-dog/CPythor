#include <iostream>
#include <fstream>
using namespace std;
void Get_WW()
{
	TChain *ee=new TChain("ntp");
	ee->Add("WW*.root");
	Int_t nentries=(Int_t)ee->GetEntries();
	int idx1;
	double raw_Px[100],raw_Py[100],raw_Pz[100],raw_En[100],pdgid[100];
	ntp->SetBranchAddress("idx1",&idx1);
	ntp->SetBranchAddress("raw_Px[100]",raw_Px);
	ntp->SetBranchAddress("raw_Py[100]",raw_Py);
	ntp->SetBranchAddress("raw_Pz[100]",raw_Pz);
	ntp->SetBranchAddress("raw_En[100]",raw_En);
	ntp->SetBranchAddress("idx2[100]",pdgid);
	ofstream f;
	f.open("ww.csv");
	for(int i=0;i<nentries;i++)
	{
		ee->GetEntry(i);
		f<<1<<','<<idx1;
		for(int j=0;j<100;j++)
		{
			f<<','<<pdgid[j];
			f<<','<<raw_Px[j];
			f<<','<<raw_Py[j];
			f<<','<<raw_Pz[j];
			f<<','<<raw_En[j];
		}
		f<<endl;
		
	}
	f.close();
}

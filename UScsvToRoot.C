#include "Riostream.h"
#include "TString.h"
#include "TFile.h"
#include "TTree.h"
#include "TSystem.h"
#include <vector>

void UScsvToRoot() {

    TString dir = gSystem->UnixPathName(__FILE__);
    dir.ReplaceAll("UScsvToRoot.C","");
    dir.ReplaceAll("/./","/");
    ifstream in;
    in.open(Form("%supdate_data.csv", dir.Data()));

    const int  n_index = 100;
    vector<double> V_temp;
    double pdgid[n_index], T_flag;
    double idx;
    double raw_Px[n_index], raw_Py[n_index], raw_Pz[n_index], raw_En[n_index], pdgid[n_index];
    double prob_1, prob_2;
    Int_t nlines = 0;
    TFile *f = new TFile("XGB_result.root","RECREATE");
    TTree *tree = new TTree("signal","data from csv file");

    tree->Branch("pdgid[100]" ,pdgid , "pdgid[100]/D");
    tree->Branch("raw_Px[100]",raw_Px, "raw_Px[100]/D");
    tree->Branch("raw_Py[100]",raw_Py, "raw_Py[100]/D");
    tree->Branch("raw_Pz[100]",raw_Pz, "raw_Pz[100]/D");
    tree->Branch("raw_En[100]",raw_En, "raw_En[100]/D");
    tree->Branch("prob_1",&prob_1,"prob_1/D");
    tree->Branch("prob_2",&prob_2,"prob_2/D");
    tree->Branch("idx"   ,&idx  , "idx/D");
    tree->Branch("T_flag",&T_flag,"T_flag/D");

    while (1) {
        in >> T_flag;
        in >> idx;
        for(int j=0; j<100; j++)
        {
            in >> pdgid[j];
            in >> raw_Px[j];
//            std::cout << "The raw_Px is: " << j << ",    " <<  raw_Px[j] << std::endl;
            in >> raw_Py[j];
            in >> raw_Pz[j];
            in >> raw_En[j];
        }
        in >> prob_1;
        in >> prob_2;
        if (!in.good()) break;
        tree->Fill();
        nlines++;
//        if(nlines>2) break;
    }

    std::cout << "There are total events: " << nlines << std::endl;
    in.close();

    f->Write();
}
